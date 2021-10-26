import math
import numpy as np
import host 
import env_pb2


 
def mobility(speed,BS,time):
    # moving model with fixed speed
    d1=[]
    for i in range(5):
        d1.append(math.sqrt(100+abs(speed*time-BS[i])**2))  
    return d1

def SNR(d,t):
    noise = 0.5*abs(np.random.normal(0,1)) # Gauss noise
    Pt= 40 #W/46dBm
    Gt= 31.6 # 15 dB
    Gr =31.6 #15 dB
    snr=[]
    for i in range(5):
        Pr= Pt*Gt*Gr/((d[i])**2) # based on Friis transmission
        snr.append(Pr/noise)
    return snr
    
    
    
def throughput(snr, num, band):
    # throughput model based on SNR-MSC-CQI mapping
    total=[]
    a=0
    MCS=0
    mcs=[]
    print('num_UE:',num)
    for i in range(5):
        SNR=10*np.log10(snr[i])
        if SNR<=-6.7:
            a=0/(num[i]+1)
        if SNR>=-6.7 and SNR<=-4.7:
            a=2.792/(num[i]+1)
            MCS=1
        if SNR>=-4.7 and SNR<=-2.3:
            a=3.624/(num[i]+1)
            MCS=1
        if SNR>=-2.3 and SNR<=0.2:
            a=5.736/(num[i]+1)
            MCS=1
        if SNR>=0.2 and SNR<=2.4:
            a=12.216/(num[i]+1)
            MCS=1
        if SNR>=2.4 and SNR<=4.3:
            a=15.84/(num[i]+1)
            MCS=1
        if SNR>=4.3 and SNR<=5.9:
            a=19.848/(num[i]+1)
            MCS=1
        if SNR>=5.9 and SNR<=8.1:
            a=25.456/(num[i]+1)
            MCS=2
        if SNR>=8.1 and SNR<=10.3:
            a=30.576/(num[i]+1)
            MCS=2
        if SNR>=10.3 and SNR<=11.7:
            a=36.696/(num[i]+1)    
            MCS=2    
        if SNR>=11.7 and SNR<=14.1:
            a=46.888/(num[i]+1)
            MCS=3
        if SNR>=14.1 and SNR<=16.3:
            a=55.056/(num[i]+1)
            MCS=3
        if SNR>=16.3 and SNR<=18.7:
            a=61.664/(num[i]+1)
            MCS=3
        if SNR>=21:
            a=75.376/(num[i]+1)  
            MCS=3  
        mcs.append(MCS)
        total.append(a)
    return total,mcs
 
def move_model(speed,BS,t):
    distance= mobility(speed,BS,t)
    snr=SNR(distance,t)
    cell=snr.index(max(snr))
    return distance, snr, cell


def num_ue(speed,left,right,t,num_UE,BS,road):
    '''A vehicle reached model using poisson process
       By each episode vehicle will appear at both end of Highway
       Then they will move along the road with fixed speed'''
    speed_left=speed
    speed_right=speed
    index=0
    station=[]
    Index=4
    CELL=[]
    total=round(road/speed_left)
    left_num=np.random.poisson(lam=0.5,size=1)[0]
    num_UE[0]+=left_num
    left.append(left_num)
    right_num=np.random.poisson(lam=0.5,size=1)[0]
    num_UE[4]+=right_num
    right.append(right_num)
    # left road
    for j in range(t):
        distance, snr, cell=move_model(speed_left,BS,j)
        CELL.append(cell)
        #print('distance:',distance,'cell:',cell,'index:',index,'num:',left[j])
        if index!=cell:
            num_UE[cell]+=left[t-j]
            num_UE[cell-1]-=left[t-j]
            index=cell
    # right road
    for k in range(t):
        Distance, SNR, Cell=move_model(speed_right,BS,total-k)
        
        if Index!=Cell:
            num_UE[Cell]+=right[t-k]
            num_UE[Cell+1]-=right[t-k]
            Index=Cell
            
    return num_UE, CELL



def A3(snr,CELL):
    # insert Handover margin into PBGT
    cell=0
    Hys=0.01
    if snr.index(max(snr))!=0:
        cell=snr.index(max(snr))
        if snr[cell]-snr[cell-1]<=Hys:
            cell=cell-1
    return cell
    
def transmission(speed,t,num,BS):
    '''This function can regard as environment for DRL
       It will return SNR and throughput as state and reward to DRL agent'''
    num_UE= num
    band=20 #Mhz
    distance = mobility(speed,BS,t)
    print('distance:',distance)
    snr=SNR(distance,t)
    th,mcs=throughput(snr,num_UE,band)
    return snr,th,mcs,distance
    
def max_cell(th):
    for j in range(5):
        if th[j] == max(th):
            cell=j 
    return cell
   
def Reward(action,th,cell,index):
    '''reward function depends on throughput and
    it will be punished at unexpected situation'''
    reward=0
    if action == 0:
        if th[cell]!=max(th):
            reward = -100
        else:
            reward = abs(th[cell])                    
    if action == 1:
        if th[cell]!=max(th):
            cell = index
            # Handover cost
            th[cell]=(1-0.8)*th[cell] 
            reward= abs(th[cell])                 
        else:
            reward = -100    
    return reward, cell,th

            
def main():
    args = host.parse_args()
    host.set_logging_config(args.logging)
    host1 = host.ProtoHost()
    host1.connect(args.remote, args.port)
    BS=[13,524,1025,1454,1957]# BS position
    num=[0,0,0,0,0]# connected devices for each BS
    cell=0
    snr,th,mcs,distance=transmission(0,0,[0,0,0,0,0],BS)
    init_state = env_pb2.State()
    [init_state.value.append(snr[x]) for x in range(5)]
    [init_state.value.append(num[x]) for x in range(5)]
    init_state.value.append(cell)
    host1.send_proto(init_state)
    sum_th=[]
    thr_A2=[]

   
    for j in range(50):
        left=[]
        right=[]
        num=[0,0,0,0,0]
        CELL=0 # serving cell_id for PBGT
        road= 2000 #m
        speed=40 #m/s
        time=round(road/speed)  # total simulation time
        Action=[]
        cell=0 #serving cell_id for DRL 
        sum_thr=0    
        thr_a2=0
        TH=0
        HO=0
        D=[]
        sum_rl=[]
        sum_a2=[]
        MCS_RL=[]
        MCS_A3=[]
        ID_RL=[]
        ID_A3=[]
        SNR_RL=[]
        SNR_A3=[]
        CON_RL=[]
        CON_A3=[]
        for i in np.arange(time):
            action=host1.rcv_proto(env_pb2.Action)
            Action.append(action.value)
            num,cell_a2=num_ue(speed,left,right,i+1,num,BS,road)
            s = env_pb2.EnvState()
            snr,th,mcs,distance=transmission(speed,i,num,BS)
            print('snr:',snr)
            print('th:',th)
            TH=th
            index=max_cell(th)
            s.done = i == time-1
            s.info.update(dict(iteration=str(i)))
            s.reward,cell,th=Reward(action.value,th,cell,index)                    
            sum_thr+=th[cell]  
            print('th:',th)
            print(action)
            print('cell:',cell)
            sum_rl.append(th[cell])
            #CELL=snr.index(max(snr))
            # insert TTT to delay HO for one episode                               
            if HO!=CELL:
                if CELL!=4:
                    if snr[CELL+1]-snr[CELL]>=0.01:
                        CELL=CELL-1
                TH[CELL]=(1-0.8)*TH[CELL]
                                    
            print('cell_a3:',CELL)
            print('TH:',TH)

            thr_a2+=TH[CELL]
            HO=CELL
            #CELL=A3(snr,CELL)
            print('cell_a3:',CELL)
            print('ho:',HO)
            # collect data for one episode
            '''sum_a2.append(TH[HO])
            ID_RL.append(cell)
            ID_A3.append(HO)
            MCS_RL.append(mcs[cell])
            MCS_A3.append(mcs[HO])
            D.append(min(distance))
            SNR_RL.append(snr[cell])
            SNR_A3.append(snr[HO])
            CON_RL.append(num[cell])
            CON_A3.append(num[HO])'''
            [s.state.value.append(snr[i]) for i in range(5)]
            [s.state.value.append(num[i]) for i in range(5)]
            s.state.value.append(cell)
            print(np.array(s.state.value), s.reward, s.done, dict(s.info))
            host1.send_proto(s)
        sum_th.append(sum_thr/time) # DRL average throughput for 50 episode
        thr_A2.append(thr_a2/time)# PBGT average throughput for 50 episode
        print('th_rl:',sum_th)
        print('th_a2:',thr_A2)
        '''print('sum_rl=',sum_rl)
        print('sum_a2=',sum_a2)
        print('ID_RL=',ID_RL)
        print('ID_A3=',ID_A3)
        print('MCS_RL=',MCS_RL)
        print('MCS_A3=',MCS_A3)
        print('distance=',D)
        print('SNR_RL=',SNR_RL)
        print('SNR_A3=',SNR_A3)
        print('CON_RL=',CON_RL)
        print('CON_A3=',CON_A3)'''
        print(Action)# 1: handover 0: no Handover
        
        host1.send_proto(init_state)

    

	    

if __name__ == "__main__":
    main()



