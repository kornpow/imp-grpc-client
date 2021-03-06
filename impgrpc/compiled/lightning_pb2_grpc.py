# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import lightning_pb2 as lightning__pb2


class LightningStub(object):
    """*
    Lightning service allows lightning actions on your underlying lightning node from the Impervious node.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GenerateInvoice = channel.unary_unary(
                '/lightning.Lightning/GenerateInvoice',
                request_serializer=lightning__pb2.GenerateInvoiceRequest.SerializeToString,
                response_deserializer=lightning__pb2.GenerateInvoiceResponse.FromString,
                )
        self.PayInvoice = channel.unary_unary(
                '/lightning.Lightning/PayInvoice',
                request_serializer=lightning__pb2.PayInvoiceRequest.SerializeToString,
                response_deserializer=lightning__pb2.PayInvoiceResponse.FromString,
                )
        self.CheckInvoice = channel.unary_unary(
                '/lightning.Lightning/CheckInvoice',
                request_serializer=lightning__pb2.CheckInvoiceRequest.SerializeToString,
                response_deserializer=lightning__pb2.CheckInvoiceResponse.FromString,
                )


class LightningServicer(object):
    """*
    Lightning service allows lightning actions on your underlying lightning node from the Impervious node.
    """

    def GenerateInvoice(self, request, context):
        """*
        GenerateInvoice allows you to generate an invoice for a specific payment amount from your lightning node.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PayInvoice(self, request, context):
        """*
        PayInvoice allows you to pay a specific invoice with your lightning node.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckInvoice(self, request, context):
        """*
        CheckInvoice allows you to check a specific invoice to see if it was paid.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LightningServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GenerateInvoice': grpc.unary_unary_rpc_method_handler(
                    servicer.GenerateInvoice,
                    request_deserializer=lightning__pb2.GenerateInvoiceRequest.FromString,
                    response_serializer=lightning__pb2.GenerateInvoiceResponse.SerializeToString,
            ),
            'PayInvoice': grpc.unary_unary_rpc_method_handler(
                    servicer.PayInvoice,
                    request_deserializer=lightning__pb2.PayInvoiceRequest.FromString,
                    response_serializer=lightning__pb2.PayInvoiceResponse.SerializeToString,
            ),
            'CheckInvoice': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckInvoice,
                    request_deserializer=lightning__pb2.CheckInvoiceRequest.FromString,
                    response_serializer=lightning__pb2.CheckInvoiceResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'lightning.Lightning', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Lightning(object):
    """*
    Lightning service allows lightning actions on your underlying lightning node from the Impervious node.
    """

    @staticmethod
    def GenerateInvoice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/lightning.Lightning/GenerateInvoice',
            lightning__pb2.GenerateInvoiceRequest.SerializeToString,
            lightning__pb2.GenerateInvoiceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PayInvoice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/lightning.Lightning/PayInvoice',
            lightning__pb2.PayInvoiceRequest.SerializeToString,
            lightning__pb2.PayInvoiceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckInvoice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/lightning.Lightning/CheckInvoice',
            lightning__pb2.CheckInvoiceRequest.SerializeToString,
            lightning__pb2.CheckInvoiceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
