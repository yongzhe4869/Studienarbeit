import gym
import argparse
from stable_baselines3 import DQN
from stable_baselines3 import PPO
from gym import spaces
from stable_baselines3.common.env_checker import check_env
from stable_baselines3.common.callbacks import StopTrainingOnMaxEpisodes
from stable_baselines3.common.evaluation import evaluate_policy

import host
import env_pb2
import ns3_mock as ns
import numpy as np
class ProtoHostEnv(gym.core.Env):
    def __init__(self, _host, port):
        self.iface = host.ProtoHost()
        self.iface.listen_and_accept(_host, port)
        super(ProtoHostEnv, self).__init__()
        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Box(low=-10000.0, high=10000.0, shape= (11,),dtype=np.float32)
        self.num_episode=0
        
    def step(self, action):
        self.__send_action(action)
        state, reward, done, info = self.__rcv_env_state()
        return np.array(state), reward, done, dict(info)

    def render(self, mode="human", close="False"):
        return

    def close(self):
        pass

    def seed(self, seed=None):
        self.np_random, seed = gym.utils.seeding.np_random(seed)
        return [seed]

    def reset(self):
        state = self.__rcv_init_state()
        return np.array(state)

    def __rcv_env_state(self):
        s = self.iface.rcv_proto(env_pb2.EnvState, timeout=60)
        return s.state.value, s.reward, s.done, s.info

    def __rcv_init_state(self):
        s = self.iface.rcv_proto(env_pb2.State, timeout=60)
        return s.value

    def __send_action(self, a):
        action = env_pb2.Action()
        action.value = a
        self.iface.send_proto(action)


def parse_args():
    parser = argparse.ArgumentParser("ClientServerEnv")
    parser.add_argument(
            "--logging", type=str, default="INFO", help="Set log level")
    parser.add_argument(
            "--host",
            type=str,
            default="127.0.0.1",
            help="Host name")
    parser.add_argument(
            "--port", type=int, default=50001, help="Host port")
    args = parser.parse_args()
    assert args.port > 50000, "Port must be larger than 50000"
    return args


def main():
    args = parse_args()
    host.set_logging_config(args.logging)
    # Stops training when the model reaches the maximum number of episodes
    callback_max_episodes = StopTrainingOnMaxEpisodes(max_episodes=15000, verbose=1)
    env = ProtoHostEnv(args.host, args.port)
    #train a Agent#
    #model = DQN("MlpPolicy", env,learning_rate=0.001,learning_starts=1000,exploration_final_eps = 0.05,batch_size =128, gamma = 0.95, verbose=1)

    #model.learn(total_timesteps=900000, callback=callback_max_episodes, log_interval=2)
    
    #model.save("DQN_HO_4")
    #del model # remove to demonstrate saving and loading

    model = DQN.load("DQN_HO_4")   
    s = env.reset()
    print(f"init state: {s}")
    for i in range(40000):
        action ,_states = model.predict(s,deterministic=True)
        
        s, reward, done, info = env.step(action)
        print(s, reward, done, info)
        if done:
            s = env.reset()

if __name__ == "__main__":
    main()
    
