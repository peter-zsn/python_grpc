# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from helloworld import helloworld_pb2 as helloworld__pb2


class GreeterStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SayHello = channel.unary_unary(
        '/helloworld.Greeter/SayHello',
        request_serializer=helloworld__pb2.HelloRequest.SerializeToString,
        response_deserializer=helloworld__pb2.HelloReply.FromString,
        )
    self.SayTest = channel.unary_unary(
        '/helloworld.Greeter/SayTest',
        request_serializer=helloworld__pb2.HelloRequest.SerializeToString,
        response_deserializer=helloworld__pb2.HelloReply.FromString,
        )


class GreeterServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def SayHello(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SayTest(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SayHello': grpc.unary_unary_rpc_method_handler(
          servicer.SayHello,
          request_deserializer=helloworld__pb2.HelloRequest.FromString,
          response_serializer=helloworld__pb2.HelloReply.SerializeToString,
      ),
      'SayTest': grpc.unary_unary_rpc_method_handler(
          servicer.SayTest,
          request_deserializer=helloworld__pb2.HelloRequest.FromString,
          response_serializer=helloworld__pb2.HelloReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'helloworld.Greeter', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))