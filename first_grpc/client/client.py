# coding: utf-8
import grpc
from helloworld import helloworld_pb2, helloworld_pb2_grpc


HOST = 'localhost'
PORT = '5001'

def run():
    with grpc.insecure_channel(HOST + ":" + PORT) as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
    print("over ---" + response.message)

if __name__== '__main__':
    run()