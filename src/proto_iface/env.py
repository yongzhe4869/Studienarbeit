import gym
import argparse

import host
import env_pb2
import ns3_mock as ns
import RL_Agent as RL

class ProtoHostEnv(gym.core.Env):
    def __init__(self, _host, port):
        self.iface = host.ProtoHost()
        self.iface.listen_and_accept(_host, port)

    def step(self, action):
        self.__send_action(action)
        state, reward, done, info = self.__rcv_env_state()
        return (state, reward, done, info)

    def render(self, mode="human", close="False"):
        return

    def close(self):
        pass

    def seed(self, seed=None):
        self.np_random, seed = gym.utils.seeding.np_random(seed)
        return [seed]

    def reset(self):
        state = self.__rcv_init_state()
        return state

    def __rcv_env_state(self):
        s = self.iface.rcv_proto(env_pb2.EnvState, timeout=60)
        return s.state.value, s.reward, s.done, s.info

    def __rcv_init_state(self):
        s = self.iface.rcv_proto(env_pb2.State, timeout=60)
        return s

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
    env = ProtoHostEnv(args.host, args.port)
    s = env.reset()
    print(f"init state: {s.value}")
    Agent=RL.Qlearning([1,2])
    for j in range(10):
        for i in range(10):
            action =Agent.choose_action(i)
            state, r, done, info = env.step(action)
            Agent.learn(i,action,r,i+1)       
    #a=Action(Agent.q_table)
    #print(a)
            print(state, r, done, info)
    print(Agent.q_table)

if __name__ == "__main__":
    main()
