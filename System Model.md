## Background
In 5G communication system, mm-Wave will be used, it means the frequency of 5G is obviously higher than 4G and other typical communication system. The result of it is the obviously decreased cover range of Base Stations and the increased density of BSs. So the number of unnecessary Handover will be distinctly increased. In addition, nowadays people always like to use mobil equipments on the Car or the train. The fast moving user equipments will also augment "ping-pong" effort and failure rate of Handover. In order to optimize the performance of Handover, we can utilize Reinforcement learning to look for the optimal parameter for Handover.
## System model  
Some paper have researched Handover of High speed UEs based on LTE Network. And some Study have showed Handover in mm-Wave Communication(5G). But there is no work related to Handover of fast-moving users in ultra-small cells. And the HO parameter optimization is complex trade-off, in this situation we can utilize Reinforcement learning.
* Scenario: UEs with high-speed (>120 km/h), small coverage area of BSs(radius:100m)
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
Parameter in `lena-x2-handover-measures.cc`
|parameter|meaning|default|    
|-----|-------|------|  
|`numberOfUes`|the number of Users|1|  
|`numberOfEnbs`|the number of Base Stations|2|  
|`distance`|the distance between the BSs|500.0 m|  
|`yForUe`|the position of y axis|500.0 m|  
|`speed`|the speed of UEs|20m/s|  
|`simTime`|Total duration of the simulation|75.0 s|  
|`enbTxPowerDbm`|Tx power used by BSs|46.0 dBm|  
|`ServingCellThreshold`|the Threshold of A2 event (A2A4)|30 dB|  
|`NeighbourCellOffset`|the offset for A3 event (A2A4)|1 dB|  
|`Hysteresis`| Handover margin (A3)|3.0 dB|  
|`TimeToTrigger`| Time to Trigger (A3)|256 ms|  
|`Interval`|The time to wait between packets|10ms|  
|`MaxPackets`| The maximum number of packets the application will send|1000000|  
|`DateRate`|the value of Date rate|100 Gb/s|  
|`Mtu`|Maximum Transmission units to device|1500 bytes|
|`Delay`| the delay of the system| 0.010 s|  
 
 

