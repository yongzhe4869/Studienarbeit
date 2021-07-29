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
