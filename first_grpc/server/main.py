# coding: utf-8
from concurrent import futures
import time

import grpc

from helloworld import helloworld_pb2, helloworld_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

HOST = 'localhost'
PORT = '5001'

#继承基类
class Greeter(helloworld_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        print('hahahha %s' % request.name)
        return helloworld_pb2.HelloReply(message='wocaocao, %s!' % request.name)


def serve():
    #定义服务器并设置最大连接数,corcurrent.futures是一个并发库，类似于线程池的概念
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    #添加一个服务
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    #设置服务器监听端口号
    server.add_insecure_port(HOST + ':' + PORT)
    server.start()
    print("......start......")
    try:
        while True:
          time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        print("error")
        server.stop(0)

if __name__ == '__main__':
    print("......start......")
    serve()


