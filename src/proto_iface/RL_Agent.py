import numpy as np
import pandas as pd

class Qlearning:
    def __init__(self,actions,learning_rate=0.01, reward_decay=0.9, e_greedy=0.9):
        self.actions=actions
        self.lr=learning_rate
        self.gamma=reward_decay
        self.epsilon=e_greedy
        self.q_table=pd.DataFrame(columns=self.actions, dtype=np.float64)

    def choose_action(self, observation):
        self.check_state_exist(observation)
        # action selection
        if np.random.uniform() < self.epsilon:
            # choose best action
            state_action = self.q_table.loc[observation, :]
            #print (state_action)
            # some actions may have the same value, randomly choose on in these actions
            action = np.random.choice(state_action[state_action == np.max(state_action)].index)
        else:
            # choose random action
            action = np.random.choice(self.actions)
        return action

    def learn(self, state, action, reward, state_next):
        self.check_state_exist(state_next)
        q_predict = self.q_table.loc[state, action]
        if state <= 10:
            q_target = reward + self.gamma * self.q_table.loc[state_next, :].max()  # next state is not terminal
        else:
            q_target = reward  # next state is terminal
        self.q_table.loc[state, action] += self.lr * (q_target - q_predict)  # update
        
    def check_state_exist(self, state):
        if state not in self.q_table.index:
            # append new state to q table
            self.q_table = self.q_table.append(
                pd.Series(
                    [0]*len(self.actions),
                    index=self.q_table.columns,
                    name=state,
                )
            )


            
def main():
    args = host.parse_args()
    host.set_logging_config(args.logging)
    host1 = host.ProtoHost()
    host1.connect(args.remote, args.port)
    state, cell_id, state_next = handover(0)
    init_state = env_pb2.State()
    [init_state.value.append(state[x]) for x in range(2)]
    host1.send_proto(init_state)
    for j in range(100):
        for i in range(10):
            action=host1.rcv_proto(env_pb2.Action)
            print(action)
            s = env_pb2.EnvState()
            state, cell_id, state_next = handover(i)
            s.done = i == 9
            s.info.update(dict(iteration=str(i)))
            s.reward =0.25*max(state)
            if action == 1:
                if state[0]!=max(state):
                    s.reward = -0.01
                else:
            	    s.reward = 0.5*max(state)
            if action == 2:
                if state[0]!=max(state):
                    s.reward= 0.5*max(state)
                else:
                    s.reward = -0.01
            print(s.reward)
            change(action,state)
            [s.state.value.append(state[i]) for i in range(2)]
            host1.send_proto(s)
	    
    
