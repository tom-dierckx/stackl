# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import stackl_protos.agent_pb2 as agent__pb2


class StacklAgentStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.RegisterAgent = channel.unary_unary(
        '/StacklAgent/RegisterAgent',
        request_serializer=agent__pb2.AgentMetadata.SerializeToString,
        response_deserializer=agent__pb2.ConnectionResult.FromString,
        )
    self.GetJob = channel.unary_stream(
        '/StacklAgent/GetJob',
        request_serializer=agent__pb2.AgentMetadata.SerializeToString,
        response_deserializer=agent__pb2.Invocation.FromString,
        )
    self.ReportResult = channel.unary_unary(
        '/StacklAgent/ReportResult',
        request_serializer=agent__pb2.AutomationResult.SerializeToString,
        response_deserializer=agent__pb2.ConnectionResult.FromString,
        )


class StacklAgentServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def RegisterAgent(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetJob(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReportResult(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_StacklAgentServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'RegisterAgent': grpc.unary_unary_rpc_method_handler(
          servicer.RegisterAgent,
          request_deserializer=agent__pb2.AgentMetadata.FromString,
          response_serializer=agent__pb2.ConnectionResult.SerializeToString,
      ),
      'GetJob': grpc.unary_stream_rpc_method_handler(
          servicer.GetJob,
          request_deserializer=agent__pb2.AgentMetadata.FromString,
          response_serializer=agent__pb2.Invocation.SerializeToString,
      ),
      'ReportResult': grpc.unary_unary_rpc_method_handler(
          servicer.ReportResult,
          request_deserializer=agent__pb2.AutomationResult.FromString,
          response_serializer=agent__pb2.ConnectionResult.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'StacklAgent', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
