import math
import matplotlib.pyplot as plt
import numpy as np

class data:

    def __init__(self):
        self.rsrp = []
  

    def add_rsrp(self, time):
        self.rsrp.append(time+np.sin(time+np.pi/2))
        self.rsrp.append((-time+50)+np.sin(time+np.pi/2))
        return self.rsrp

    def state(self,rsrp,position):
        self.state={'rsrp_all_BS': rsrp, 'position': position}
        return self.state
    def reward(self,rsrp):
        self.reward = max(rsrp)
        return self.reward
x = np.arange(50)
rsrp_cell_1=x+np.sin(x+np.pi/2)
rsrp_cell_2=(-x+50)+np.sin(x+np.pi/2)
plt.plot(x,rsrp_cell_1)
plt.plot(x,rsrp_cell_2)
plt.legend(['cell_1','cell_2'],loc='best')
plt.show()


t1=data()
t1.add_rsrp(1)
t1.state(t1.rsrp,[1,0,0])
t1.reward(t1.rsrp)
