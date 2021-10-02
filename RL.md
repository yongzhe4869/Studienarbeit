## Reinforcement learning  
Reinforcement learning(RL) is a subclass of machine learning, and the Agent of RL can learn to perform action in an environment in order to maximize the reward.
In the same time the environment will feedback reward and state to the agent.   
According to policy the RL can be divided into off-policy and on-policy algorithm.
* off-policy: the Agent will take random policy to exploration .(with help of e-greedy)  
* on-policy: the Agent will take the same policy to select actions.        

As a rule the RL will be devided into Model-free and Model-based methods. And Model-free methods are devided in value-based and policy-based algorithm.  
* value-based: learn the state or state-action value. Act by choosing the best action in the state. Exploration is necessary.  
* policy-based: learn directly the stochastic policy function that maps state to action. Act by sampling policy.  
* Model-Based: learn the model of the world, then plan using the model. Update and re-plan the model often.
![](https://github.com/yongzhe4869/Studienarbeit/blob/main/Figure/DRL.PNG)   
### Some popular RL algorithm(library: stable_baselines3)
|Algorithm|description|policy|value/policy|action space|state space|  
|-----|-----|-----|-----|------|------|   
|SAC|Soft Actor Critic|off-policy|value-based|Continuous|Continuous/Discrete|   
|DQN|Deep Q Network|off-policy|value-based|Discrete|Continuous/Discrete|   
|PPO| Proximal Policy Optimization|on-policy|policy-based|Continuous/Discrete|Continuous/Discrete|   
|DDPG|Deep Deterministic Policy Gradient|off-policy|policy-based|Continuous|Continuous/Discrete|   
|A3C| Asynchronous Advantage Actor Critic|on-policy|policy-&value-based|Continuous/Discrete|Continuous/Discrete|  
### A Simple example using Deep Q-learning Agent
The model of signal power for two cells:  
* cell_1 = -t+10+sin(t+pi/2)  
* cell_2 = t+sin(t+pi)  
![](https://github.com/yongzhe4869/Studienarbeit/blob/main/Figure/example.PNG)   
The output is a list of RSRPs as State. The first value is Rsrp for cell_1, the second one is Rsrp for cell_2  
![](https://github.com/yongzhe4869/Studienarbeit/blob/main/Figure/example5.PNG)   
Firstly we should train a Agent based on DQN.  
* `num_episodes`: 15000
* Policy: `Mlppolicy`
* learning rate: 0.001 
* gamma = 0.95    
![](https://github.com/yongzhe4869/Studienarbeit/blob/main/Figure/result3.PNG)     
After training the Agent can predict actions by itself and always want to keep the best Rsrp.  
![](https://github.com/yongzhe4869/Studienarbeit/blob/main/Figure/result4.PNG)   
 ### more sophisticated simulator for DRL agent
 * expand the number of BS from 2 to 5  
 * throughput as reward function is equal to shannon channel capacity and influenced by number of UEs.    
 shannon channel capacity is maximum of throughput. At predefined SNR it will switch to higher code scheme and throughput.      
  ![](https://github.com/yongzhe4869/Studienarbeit/blob/main/Figure/throughput.PNG)    
  ![](https://github.com/yongzhe4869/Studienarbeit/blob/main/Figure/throughput_snr.PNG)
  ![](https://github.com/yongzhe4869/Studienarbeit/blob/main/Figure/switch.PNG) 
 * The number of vehicles should be variable at any time.    
 At every moment the vehicles will be generated at both end of highway based on poisson process. These vehicles will move along the highway in both direction.    
 ![](https://github.com/yongzhe4869/Studienarbeit/blob/main/Figure/num_UE.PNG) 
 * mobility model for vehicle:   
 some vehicles are driving along a road with a fixed velocity so that the distance to a particular BS first gets smaller linearly, then has a minimum and then linearly increases again. Moreover, cars can move in two opposite directions.    
 * According to Friis Path loss model, SNR is inversely proportional to the square of distance (as state space).   
  ![](https://github.com/yongzhe4869/Studienarbeit/blob/main/Figure/formel.PNG)    
 * The noise level is increasing along with the road  
  ![](https://github.com/yongzhe4869/Studienarbeit/blob/main/Figure/distance.PNG)  
  ![](https://github.com/yongzhe4869/Studienarbeit/blob/main/Figure/model.PNG)
  ![](https://github.com/yongzhe4869/Studienarbeit/blob/main/Figure/train_1.PNG)   
 * compare the received total throughput of DRL algorithm and A2A4 algorithm (DRL has better performance)
  ![](https://github.com/yongzhe4869/Studienarbeit/blob/main/Figure/compare.PNG)  
 * expand state space: received SNR from each BS, the amount of connected devices for each BSs, current serving cell ID      
|parameters|value|    
|-------|------|   
|the number of Base Stations|5|  
|the distance between the BSs|500.0 m|  
|the speed of UEs|40m/s|  
|Total duration of the simulation|50.0 s|  
|Tx power used by BSs|20 w/43.0 dBm|  
 
