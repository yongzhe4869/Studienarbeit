## Classic Handover
The classic Handover process is based on the transfer of message between UE, eNBs and MME. The whole Process is divided into 3 parts:
* Handover preparetion  
  Data flows between UE and serving eNB (measurement control and report)
* Handover execution  
  Handover Request to target eNB, Request Ack to serving eNB, Handover Command to UE,     Synchronisation and Handover Confirm to target eNB 
* Handover completion  
  Path Switch Request to MME, Request Ack to target eNB, Resource in serving eNB release  
### Handover Variable  
* Handover initiation threshold level RSRP and RSRQ   
  This threshold level is used for HO initiation. When the handover threshold decreases, the probability of a late handover decreases and the ping-pong effect increases.
* Hysteresis margin (HOM)  
  A3 event will be triggered if RSRQ(t) - RSRQ(s) >= Hysteresis. This Parameter is used to avoid ping-pong effect. But it also increase HO failure because it prevent necessary HO.
* Time-to-Trigger(TTT)  
 Time-to-trigger (TTT) is then required to satisfy event A3. During TTT, if RSRP in the serving cell becomes higher again than that in the target cell, “leaving event” occurs so that HO would not be executed. This parameter can decrease the number of unnecessary HO and avoid ping-pong effects, but it can delay the HO.  
 For example: Event A3 entering condition : RSRQ(t) - RSRQ(s) >= Hysteresis  
              Event A3 leaving condition :  RSRQ(t) - RSRQ(s) >= -Hysteresis      
Notice: Too low HO offset and TTT values cause ping-pong effect. Too high values result in call drops and bad transmission.  
### Handover Events  
 ![](https://github.com/yongzhe4869/Studienarbeit/blob/main/ho.PNG)  
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
### Handover performance metrics
* Average system Throughput
The system throughput is defined as the rate of successful messages delivered by all users per second. 
* Handover rate and HO success rate
* the number of Handover
* Reference Signal Received Power (RSRP)  
  This prarmeter provides cell-specific signal strength metric. It is used as an Input and decision criterion.
* Reference Signal Received Quality (RSRQ)  
  This prarmeter provides cell-specific signal quality metric. It is also used as an Input and decision criterion.  
  It is defined as: RSRQ = N*RSRP/RSSI  
* SNR/SINR  
  SNR is defined as the ratio of signal power and the noise power.  
  SINR is defined as the ratio of signal power to the combined noise and interference power  
## Two Handover algorithm in NS3  
### A2-A4-RSRQ HO algorithm
1. acquire RSRQ measurement from event A2 and A4.
2. compare RSRQ of serving cell with threshold.
3. if RSRQ(s)>=threshold of event A2, it means event A2 has been triggered, then look for the best neighbor cell.
4. if the best neighbor RSRQ - RSRQ(S) >= offset, it means event A3 has been triggered.
5. Then HO process should be triggered.  
### strongest cell handover algorithm
This Algorithm is to look for the best possible RSRP for UE, and the Handover will be implemented as soon as the stronger RSRP is detected. In this case event A3 should be observed. HOM and TTT should be used in order to decrease the impact of ping-pong effect.
## Handover using Reinforcement Learning
Because the HO parameter selection is a trade-off problem and it is hard to calculate the optimal Parameter of HO(such as TTT and HOM). In this case we can use Reinforcement Learning to find the best condition and maximize the throughput.  
### Reinforcement Learning
RL is a subclass of machine learning and it is different from supervised-and unsupervised learning, because RL don't require labelled input/output but it uses rewards and punishment as signals for positive and negative behavior. So the key point of RL is find the maximal reward based on trial and error in the environment. And it is based on Markov Decision Process(MDP) and the key terms of RL are Agent, Action, State, Reward, Policy and Environment.
![](https://github.com/yongzhe4869/Studienarbeit/blob/main/RL.PNG)  
### State of the art  
|Paper|Algorithm|Policy|reward|state|action|  
|------|------|-------|-------|-------|-------|
|5G Handover using Reinforcement learning|Q-Learning with e-greedy alogorithm for CMAB, HO Algorithm using Access-Beams|a RL agent replaced classic HO controller, handle the measurement report and choose action to maximize the throughput, compare RL alogorithm with classic Algorithm|received RSRP of link-beam after HO as reward|Access-beam reference signal received power(RSRP) from serving and neighbor cells|choose target BS to HO|  
|DRL based HO Management for mm Wave Communication|Deep Q-Learning, Deep Neural Network (DNN), rate based HO (RBH)|Optimal BS Selection based on DRL, one hot-code to describe BS, received SNR of all BSs is the important parameter for BS Selection, compare RBH with DQN| recevied SNR to bulid throughput as reward|received SNR of all BSs, one hot code vector of serving BS| the current serving BS|
|A Parameter Optimization Method for LTE-R HO based on RL|Q-Learning, situation maps, LTE-R system for high speed|find optimal HO parameter using RL in HO process, simulate HO with different UE moving speed,compare Performance of Q-Learning Alogorithm with 3GPP standard|HO success rate as reward function|A2A4:Threshold and offset, A3: TTT and HOM|The set of what parameters the UE chooses to handover at the current speed|  
|HO Optimization via Asynchronous Multi-User DRL|DNN, Advantage actor-critic(A3C), supervised learning(SL),upper conﬁdence bandit (UCB)|a number of UE and RL framework work at the same time in order to increase the algorithm performance, initiate DNN with SL,compare the averaged HO rates and throughputs of UCB, SL initialized A3C-online and A3C-ofﬂine RL methods | a weighted sum between the averaged throughput and the HO rate as reward|RSRQs from all BSs to a UE and one-Hot-code of serving BS|a(i, t) represent serving BS|  
|ML assisted HO and Resource Management for Cellular Connected Drones|Q-Learning with e-greedy, Deep Q-Learning|transform H-RRM optimization problem into ML problem amd solve in RL, consider more Variable (such as altitude, speed, path-loss) in the communication system|w(t) is inversely proportional to velocity v, buffer queue size q, interference to BS and indicator of HO |altitude h, velocity v, current serving BS , buffer queue size q, and the last path-loss measurements to neighbor BSs| transmit power P and radio resource allocation v| 
|Optimization of HO problem using Q-Learning for LTE network|Q-Learning, LTE Hard HO, RSS based TTT Window, Integrator HO, LTE Hard HO with average RSRP Constraint|use Q-learning to find the optimal parameter of HO, such as HOM, TTT, the number of HO and throughput. This work compare the performance of 4 standard LTE HO algorithm using optimal Parameter(HOM and TTT)| The reward function is related to the number of HO, system throughput and delay.| throughput and system delay and average numbers of handover|different combinations of HOM and TTT|
|Multi-Agent DRL for distributed HO Management in dense mm-wave Networks|Multi-Agent DRL, Deep recurrent Q network(DQRN)|each UE is modeled as an independent agent that learns in a distributed way its handover strategy with the goal of optimizing the network throughput,compare the performance(HO rate and throughput)of 2 reward function and RSS|fully cooperative RL HO: network throughput, self interest RL HO: perceived data rate| the RSS of the surrounding BSs, speed, ACK, perceived data rate and network sum-rate|associate with one BS in the network| 
|Learning-based Load Balancing HO in Mobile mm-Wave Networks|deep deterministic policy gradient(DDPG)|DDPG method is applied to the ofﬂine training phase to estimate the optimal policy. Then, the obtained policy is used to the online phase. The goal is to minimize rate requirement and the number of handovers.|the summation of the rates of UEs in time slot t minus the loss for the handovers and average rates getting less than the thresholds| the location and serving BS of UE i, the capacity of the channel between BS and UE, proportion of the resources of BS, last observation of achieved rate of UE|to determine a backup for each one of the UEs| 
|A DQN-based HO Management for SDN-Enabled Ultra-Dense Networks(UDN)|DQN, UDN, software defined network(SDN)| use SDN to build UDN structure, use RL framework to build control plane of SDN, compare the HO rate and Average throughput of traditional , UCB-based HO and DQN based HO, |the reward function is reated to throughput, the number of HO and HO failure|SINR of all note to UE, the access control rate of all note|index representing the node that maintains the UE’s activity|
