## Background
In 5G communication system, mm-Wave will be used, it means the frequency of 5G is obviously higher than 4G and other typical communication system. The result of it is the obviously decreased cover range of Base Stations and the increased density of BSs. So the number of unnecessary Handover will be distinctly increased. In addition, nowadays people always like to use mobil equipments on the Car or the train. The fast moving user equipments will also augment "ping-pong" effort and failure rate of Handover. In order to optimize the performance of Handover, we can utilize Reinforcement learning to look for the optimal parameter for Handover.
## System model  
Some paper have researched Handover of High speed UEs based on LTE Network. And some Study have showed Handover in mm-Wave Communication(5G). But there is no work related to Handover of fast-moving users in ultra-small cells. And the HO parameter optimization is complex trade-off, in this situation we can utilize Reinforcement learning.
* Scenario: UEs with high-speed (>120 km/h), small coverage area of BSs(radius:100-300m)
* Simulator: NS3
* RL algorithm: Q-learning/ deep Q-learning
* Goal: to maximize system throughput(Bit rate) and minimize Handover failure rate  
* possible state variables:  
1. RSRP/RSRQ 
2. SNR/SINR
3. HOM, TTT(A3 RSRP HO algorithm)
4. Threshold, offset(A2 A4 RSRQ HO algorithm)
5. UE speed
6. one hot-code of serving BS
7. the number of HO  
* Network topology:
    
          |     + ---------------------------------------------------------------------------->
          |     UE
          |
          |               d                   d                   d                  d
        y |     |-------------------x-------------------x-------------------x-----------------
          |     |                 eNodeB              eNodeB              eNodeB
          |   d |
          |     |
          |     |                                                          d = distance
                o (0, 0, 0)                                                y = yForUe
## Parameter in NS3  
|parameter|meaning|  
|-----|-------|  
|numberOfUes|the number of Users|  
|||
 
 

