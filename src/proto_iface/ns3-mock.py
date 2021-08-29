import math
import numpy as np
import RL_Agent as RL
import host 
import env_pb2

class data:

    def __init__(self):
        self.rsrp = []
        self.rsrp_next=[]
        self.r = 0  

    def add_rsrp(self, time):
        self.rsrp=[]
        self.rsrp.append((-time+10)+np.sin(time+np.pi/2))
        self.rsrp.append(time+np.sin(time+np.pi/2))
        return self.rsrp
        # rsrp=[serving cell, neighbor cell]
    def add_rsrp_next(self, time):
        self.rsrp_next=[]
        self.rsrp_next.append((-time+10)+np.sin(time+np.pi/2))
        self.rsrp_next.append(time+np.sin(time+np.pi/2))
        return self.rsrp
       
def change(HO,rsrp):
    # HO=1 Handover happen
    if HO:
        a=rsrp[1]
        rsrp[1]= rsrp[0]
        rsrp[0]=a    


        
def serving_cell(rsrp):
    for i in range(2):
        if rsrp[i]==max(rsrp):
            return i
            

       
def handover(i):
    cell=data()
    cell.add_rsrp(i)
    cell.add_rsrp_next(i+1)
    cell_id=serving_cell(cell.rsrp)
    HO= 0
    if cell.rsrp[0] < max(cell.rsrp):
        HO= 1
        #Action(HO,cell.rsrp)
    return cell.rsrp, cell_id, cell.rsrp_next

        

            
def main():
    args = host.parse_args()
    host.set_logging_config(args.logging)
    host1 = host.ProtoHost()
    host1.connect(args.remote, args.port)
    #state, cell_id, state_next = handover(0)
    state, cell_id, state_next = handover(0)
    init_state = env_pb2.State()
    [init_state.value.append(state[x]) for x in range(2)]
    host1.send_proto(init_state)
    
    for j in range(2):
        Action=[]
        for i in range(10):
            action=host1.rcv_proto(env_pb2.Action)
            Action.append(action.value)
            
            s = env_pb2.EnvState()
            state, cell_id, state_next = handover(i)
            s.done = i == 9
            s.info.update(dict(iteration=str(i)))
            #s.reward=0.5*max(state)
            if action.value == 0:
                if state[0]==max(state):
                    s.reward = 0.5*max(state)
                else:
                    s.reward = -0.1
            if action.value == 1:
                if state[1]==max(state):
                    s.reward= 0.5*max(state)
                else:
                    s.reward = -0.1
            #change(action,state)
            [s.state.value.append(state[i]) for i in range(2)]
            print(np.array(s.state), s.reward, s.done, dict(s.info))
            host1.send_proto(s)
        print(Action)
        host1.send_proto(init_state)

    
    #host1.send_proto(init_state)
    
	    

if __name__ == "__main__":
    main()



