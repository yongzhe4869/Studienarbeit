import math
import numpy as np
import host 
from env import ProtoHostEnv
import env
import env_pb2

class data:

    def __init__(self):
        self.rsrp = []
        self.r = 0  

    def add_rsrp(self, time):
        self.rsrp=[]
        self.rsrp.append((-time+50)+np.sin(time+np.pi/2))
        self.rsrp.append(time+np.sin(time+np.pi/2))
        return self.rsrp
        # rsrp=[serving cell, neighbor cell]
    def reward(self,rsrp):
        self.r = 0.5*max(rsrp)
        return self.r   
    

def Action(HO,rsrp):
    # HO=1 Handover happen
    if HO:
        a=max(rsrp)
        rsrp[1]= rsrp[0]
        rsrp[0]=a
def serving_cell(rsrp):
    for i in range(2):
        if rsrp[i]==max(rsrp):
            return i
def handover(i):
    cell=data()
    cell.add_rsrp(i)
    cell_id=serving_cell(cell.rsrp)
    HO= 0
    if cell.rsrp[0] < max(cell.rsrp):
        HO= 1
        Action(HO,cell.rsrp)
    cell.r=cell.reward(cell.rsrp)
        
    return cell.rsrp,cell.r, HO, cell_id

        
def main():
    args = host.parse_args()
    host.set_logging_config(args.logging)
    host1 = host.ProtoHost()
    host1.connect(args.remote, args.port)
    init_state = env_pb2.State()
    [init_state.value.append(x) for x in range(10)]
    host1.send_proto(init_state)
    for i in range(10):
        host1.rcv_proto(env_pb2.Action)
        s = env_pb2.EnvState()
        state, reward, action, cell_id = handover(i)
        s.done = i == 9
        s.info.update(dict(iteration=str(i)))
        s.reward = reward
        [s.state.value.append(state[i]) for i in range(2)]
        host1.send_proto(s)
    

if __name__ == "__main__":
    main()


