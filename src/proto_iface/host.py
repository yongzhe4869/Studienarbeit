#!/usr/bin/env python3

import socket
import select
import time
import logging
import argparse


class ProtoHost:
    def __init__(self):
        pass

    def listen_and_accept(self, host, port):
        self.__accept_tcp_conn(host, port)
        logging.info(f"Connected with {(self.conn, self.addr)}")

    def connect(self, remote, port):
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.connect((remote, port))

    def rcv_proto(self, cls, timeout=60):
        proto = cls()
        logging.info(f"Trying to receive protobuf data of type {cls}.")
        start = time.time()
        try:
            size = self.__rcv_protobuf_size(timeout)
            data = self.__rcv_from_socket(size, timeout)
            t = time.time() - start
            logging.info(f"Rcv data (after {t} seconds)")
        except socket.timeout:
            return
        proto.ParseFromString(data)
        return proto

    def send_proto(self, proto):
        buf = proto.ByteSize().to_bytes(4, "little")
        buf += proto.SerializeToString()
        logging.info(f"Sending protobuf data of type {type(proto)}")
        self.conn.sendall(buf)

    def __accept_tcp_conn(self, host, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            s.listen()
            self.conn, self.addr = s.accept()
            return self.conn, self.addr

    def __rcv_from_socket(self, num_bytes, timeout):
        if num_bytes == 0:
            return b""
        read_sockets, _, _ = select.select([self.conn], [], [], timeout)
        if not read_sockets:
            logging.info(f"No data received in {timeout} seconds.")
            raise socket.timeout("timeout at read")
        data = self.conn.recv(num_bytes)
        if not data:
            raise RuntimeError("Socket connection closed")
        return data

    def __rcv_protobuf_size(self, timeout):
        """Receive the size of the next protobuf object.

        First four bytes are the length of the next protobuf object we want
        to receive.
        """
        size_bytestr = self.__rcv_from_socket(4, timeout)
        assert len(size_bytestr) == 4
        size = int.from_bytes(size_bytestr, 'little')
        return size


def set_logging_config(loglevel):
    num_level = getattr(logging, loglevel.upper())
    logging.basicConfig(format="%(asctime)s %(message)s", level=num_level)


def parse_args():
    parser = argparse.ArgumentParser("ProtoBuf Host")
    parser.add_argument(
            "--logging", type=str, default="INFO", help="Set log level")
    parser.add_argument(
            "--remote",
            type=str,
            default="127.0.0.1",
            help="Remote name")
    parser.add_argument(
            "--port", type=int, default=50001, help="Remote port")
    args = parser.parse_args()
    assert args.port > 50000, "Port must be larger than 50000"
    return args


def main():
    import env_pb2
    args = parse_args()
    set_logging_config(args.logging)
    host = ProtoHost()
    host.connect(args.remote, args.port)
    init_state = env_pb2.State()
    [init_state.value.append(x) for x in range(10)]
    host.send_proto(init_state)
    for i in range(10):
        host.rcv_proto(env_pb2.Action)
        s = env_pb2.EnvState()
        s.done = i == 9
        s.info.update(dict(iteration=str(i)))
        s.reward = 42 + i
        [s.state.value.append(i*x) for x in range(10)]
        host.send_proto(s)


if __name__ == "__main__":
    main()
