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
* `num_episodes`: 500
* Policy: `Mlppolicy`
* learning rate: 0.01 
* gamma = 0.99
![](https://github.com/yongzhe4869/Studienarbeit/blob/main/Figure/result3.PNG)   
After training the Agent can predict actions by itself and always want to keep the best Rsrp.  
![](https://github.com/yongzhe4869/Studienarbeit/blob/main/Figure/result4.PNG)   
 ### A expanded example using DQN  
 Compare with the previous example, there are following changes:   
 * expanded Basestation from 2 to 5 (The amount of Basestations can be expanded into random number)
 * add gauss noise into signal model(train phase: periodic noise based on sin waves,  test phase: AWGN)
 * use SNR as reward function (SNR is proportional to throughput)  
 Algorithm:  
 The Agent always want to keep connect with the highest RSRP.   
 When this situation does not happend, we will give a negative reward.  
 ![](https://github.com/yongzhe4869/Studienarbeit/blob/main/Figure/signal.PNG)   
 ![](https://github.com/yongzhe4869/Studienarbeit/blob/main/Figure/train.PNG)   
 ### more sophisticated simulator for DRL agent
 * throughput is equal to shannon channel capacity and influenced by number of UEs  
 $$softmax(x_i) = \frac {e^{x_i}}{\sum_{j=0}^N{e^x_j}}$$
