import math
import numpy as np
import host 
import env_pb2

class data:

    def __init__(self):
        self.rsrp = []
        self.snr= []
        self.r = 0
   

    def add_rsrp(self, time):
        self.rsrp=[]
        self.snr= []
        power_1, snr_1 = signal(time, 0,0)
        power_2, snr_2 = signal(time, 10,1)
        power_3, snr_3 = signal(time, 20,2)
        power_4, snr_4 = signal(time, 27,3)
        power_5, snr_5 = signal(time, 35,4)
        self.rsrp.append(power_1)
        self.rsrp.append(power_2)
        self.rsrp.append(power_3)
        self.rsrp.append(power_4)
        self.rsrp.append(power_5)
        self.snr.append(snr_1)
        self.snr.append(snr_2)
        self.snr.append(snr_3)
        self.snr.append(snr_4)
        self.snr.append(snr_5)
        return self.rsrp, self.snr
       

        
        
def signal(time, position,p):
    noise =  3*np.sin(time+p*np.pi/4)+np.random.normal(0,1)
    signal = -(time-position)*(time-position)+50
    power = signal + noise
    if power <=0:
        signal = 0.01*abs(noise)
        power = 0.01*abs(noise)
    snr = abs(signal/noise)
    return power,snr
 
 
 
def handover(i):
    cell=data()
    cell.add_rsrp(i)
    return cell.rsrp, cell.snr



            
def main():
    args = host.parse_args()
    host.set_logging_config(args.logging)
    host1 = host.ProtoHost()
    host1.connect(args.remote, args.port)
    
    state, snr = handover(0)
    init_state = env_pb2.State()
    [init_state.value.append(state[x]) for x in range(5)]
    host1.send_proto(init_state)
    
    for j in range(5):
        Action=[]
        cell=0
        for i in range(40):
            action=host1.rcv_proto(env_pb2.Action)
            Action.append(action.value)
           
            s = env_pb2.EnvState()
            state, snr= handover(i)
            print(state)
            print(snr)
            s.done = i == 39
            s.info.update(dict(iteration=str(i)))
            if action.value == 0:
                if state[cell]!=max(state):
                    s.reward = -100
                else:
                    s.reward = 10*abs(max(snr))
            if action.value == 1:
                if state[cell] != max(state):
                    s.reward= 10*abs(max(snr))
                    if cell !=4:
                        cell = cell+1
                else:
                    s.reward = -100
                    
            print(action)
            print(cell)
            [s.state.value.append(state[i]) for i in range(5)]
            print(np.array(s.state.value), s.reward, s.done, dict(s.info))
            host1.send_proto(s)
       
        print(Action)
        host1.send_proto(init_state)

    

	    

if __name__ == "__main__":
    main()



