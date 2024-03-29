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
### A2A4 Handover algorithm  
Handover algorithm implementation based on RSRQ measurements, Event A2 and Event A4.  
Handover decision made by this algorithm is primarily based on Event A2 measurements (serving cell's RSRQ becomes worse than threshold). When the event is triggered, the first condition of handover is fulfilled.  
Event A4 measurements (neighbour cell's RSRQ becomes better than threshold) are used to detect neighbouring cells and their respective RSRQ. When a neighbouring cell's RSRQ is higher than the serving cell's RSRQ by a certain offset, then the second condition of handover is fulfilled. When the first and second conditions above are fulfilled, the algorithm informs the eNodeB RRC to trigger a handover.  
* The threshold for Event A2: `ServingCellThreshold`    
* The offset used in the second condition : `NeighbourCellOffset`  
* A2 Measurment report: `cellId`, `RSRP`,`RSRQ` of serving cell.  
* A4 Measurment report: `cellId`, `RSRP`,`RSRQ` of neighbor cell.  
* `void DoReportUeMeas (uint16_t rnti, LteRrcSap::MeasResults measResults)` is called whenever a handover event (A1-A4) happens  
    * `rnti` identifies UEs uniquely  
    * `MeasResults` contains `RSRP`, `RSRQ` values for the serving cell and neighbors  
* `void TriggerHandover (uint16_t rnti, uint16_t targetCellId)`  
    * Triggers handover of UE identified by `rnti` to cell with `targetCellId`
### Reinforcement learning architecture  
The NS3 will collect data of UE measurement during the whole simulation, such as RSRQ, RSRP of all cells and position of UE. According to these data included state and reward Agent should make a decision whether UE should make a Handover now and which BS should UE make contact.  
![](https://github.com/yongzhe4869/Studienarbeit/blob/main/Figure/system.jpg)   
 There are many UEs in the system, each UE will run the HO algorithm based on RL in the same time.
* Agent: UE 
* Action(a): whether Handover have triggered or not(ture or false), chosen target BS(cell ID) and HO event ID (A1, A2, A3, A4, A5) 
* State(s): Position of the UE, RSRP of all BS, `cellID` of serving BS
* Reward(r): 
    * system Throughout is defined as successful messages delivered by all users per second.  
    Throughput =  (Total delivered messages of all UEs ) / (Total duration of simulation)  
* some static parameter:
    * speed of UE
    * Threshold of HO event
    * offset for A3
    * HO margin
    * Time to Trigger 
* Deep Q-learning:  
    * e-greedy: The e-Greedy Algorithm makes use of the exploration-exploitation tradeoff.  
  for example: if e = 10%, agent will take random action with 10% possibility and find largest value in Q-table with 90% possibility.
 ![](https://github.com/yongzhe4869/Studienarbeit/blob/main/Figure/DQN.PNG)   
 

## Examples from Lte in NS3  
result of `lena-x2-handover.cc`  
 ![](https://github.com/yongzhe4869/Studienarbeit/blob/main/Figure/result2.PNG)  
 result of `lena-x2-handover-measures.cc`  
 ![](https://github.com/yongzhe4869/Studienarbeit/blob/main/Figure/result1.PNG)  
 result of `env.py`   
  ![](https://github.com/yongzhe4869/Studienarbeit/blob/main/Figure/env2.PNG)  
  result of `host.py`    
 ![](https://github.com/yongzhe4869/Studienarbeit/blob/main/Figure/host.PNG)   
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
 
 

