## Classic Handover
The classic Handover process is based on the transfer of message between UE, eNBs and MME. The whole Process is divided into 3 parts:
* Handover preparetion  
  Data flows between UE and serving eNB (measurement control and report)
* Handover execution  
  Handover Request to target eNB, Request Ack to serving eNB, Handover Command to UE,     Synchronisation and Handover Confirm to target eNB 
* Handover completion  
  Path Switch Request to MME, Request Ack to target eNB, Resource in serving eNB release  
### Handover Parameters  
* Reference Signal Received Power (RSRP)  
  This prarmeter provides cell-specific signal strength metric. It is used as an Input and decision criterion.
* Reference Signal Received Quality (RSRQ)  
  This prarmeter provides cell-specific signal quality metric. It is also used as an Input and decision criterion.  
  It is defined as: RSRQ = N*RSRP/RSSI
* Hysteresis margin (HOM)  
  Handover will be initiated if RSRQ(t) - RSRQ(s) = Hysteresis. This Parameter is used to avoid ping-pong effect. But it also increase HO failure because it prevent necessary HO.
* Time-to-Trigger(TTT)  
  HO will be initiated when the request of HO is over. It can decrease the number of unnecessary HO and avoid ping-pong effects. But it can delay the HO.  
Notice: Too low HO offset and TTT values cause ping-pong effect. Too high values result in call drops and bad transmission.  
### Handover Events  
  |Events|description|formula|  
  |----|----|-----|  
  |A1|Serving becomes better than threshold|RSRP(s)>threshold1|  
  |A2|Serving becomes worse than threshold|RSRP(s)<threshold2|  
  |A3|Neighbour becomes offset better than serving|RSRP(t)-RSRQ(S)>offset|  
  |A4|Neighbour becomes better than threshold|RSRP(t)>threshold3|  
### Optimization principles  
* Minimize the number of handover failures  
* Minimize the number of unnecessary handovers  
* Minimize handover delay  
* increasing system throughput  
## Handover using Reinforcement Learning
Because the HO parameter selection is a trade-off problem and it is hard to calculate the optimal Parameter of HO(such as TTT and HOM). In this case we can use Reinforcement Learning to find the best condition and maximize the throughput.  
### Reinforcement Learning
RL is a subclass of machine learning and it is different from supervised-and unsupervised learning, because RL don't require labelled input/output. However, the key point of RL is find the maximal reward based on trial and error in the environment.  
![](https://github.com/yongzhe4869/Studienarbeit/blob/main/RL.PNG)
