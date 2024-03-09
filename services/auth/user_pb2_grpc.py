# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc

import user_pb2 as user__pb2


class UsersStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetUserList = channel.unary_unary(
            "/auth.Users/GetUserList",
            request_serializer=user__pb2.UserListRequest.SerializeToString,
            response_deserializer=user__pb2.UserListResponse.FromString,
        )
        self.GetUser = channel.unary_unary(
            "/auth.Users/GetUser",
            request_serializer=user__pb2.UserRequest.SerializeToString,
            response_deserializer=user__pb2.UserResponse.FromString,
        )
        self.CreateUser = channel.unary_unary(
            "/auth.Users/CreateUser",
            request_serializer=user__pb2.CreateUserRequest.SerializeToString,
            response_deserializer=user__pb2.CreateUserResponse.FromString,
        )
        self.UpdateUser = channel.unary_unary(
            "/auth.Users/UpdateUser",
            request_serializer=user__pb2.UpdateUserRequest.SerializeToString,
            response_deserializer=user__pb2.UpdateUserResponse.FromString,
        )
        self.DeleteUser = channel.unary_unary(
            "/auth.Users/DeleteUser",
            request_serializer=user__pb2.DeleteUserRequest.SerializeToString,
            response_deserializer=user__pb2.DeleteUserResponse.FromString,
        )


class UsersServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetUserList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CreateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_UsersServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "GetUserList": grpc.unary_unary_rpc_method_handler(
            servicer.GetUserList,
            request_deserializer=user__pb2.UserListRequest.FromString,
            response_serializer=user__pb2.UserListResponse.SerializeToString,
        ),
        "GetUser": grpc.unary_unary_rpc_method_handler(
            servicer.GetUser,
            request_deserializer=user__pb2.UserRequest.FromString,
            response_serializer=user__pb2.UserResponse.SerializeToString,
        ),
        "CreateUser": grpc.unary_unary_rpc_method_handler(
            servicer.CreateUser,
            request_deserializer=user__pb2.CreateUserRequest.FromString,
            response_serializer=user__pb2.CreateUserResponse.SerializeToString,
        ),
        "UpdateUser": grpc.unary_unary_rpc_method_handler(
            servicer.UpdateUser,
            request_deserializer=user__pb2.UpdateUserRequest.FromString,
            response_serializer=user__pb2.UpdateUserResponse.SerializeToString,
        ),
        "DeleteUser": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteUser,
            request_deserializer=user__pb2.DeleteUserRequest.FromString,
            response_serializer=user__pb2.DeleteUserResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "auth.Users", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Users(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetUserList(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/auth.Users/GetUserList",
            user__pb2.UserListRequest.SerializeToString,
            user__pb2.UserListResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetUser(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/auth.Users/GetUser",
            user__pb2.UserRequest.SerializeToString,
            user__pb2.UserResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def CreateUser(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/auth.Users/CreateUser",
            user__pb2.CreateUserRequest.SerializeToString,
            user__pb2.CreateUserResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def UpdateUser(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/auth.Users/UpdateUser",
            user__pb2.UpdateUserRequest.SerializeToString,
            user__pb2.UpdateUserResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def DeleteUser(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/auth.Users/DeleteUser",
            user__pb2.DeleteUserRequest.SerializeToString,
            user__pb2.DeleteUserResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )