#!/usr/bin/env python
# coding: utf-8


class JsonRpcError(RuntimeError):
    """
    Represents a JSON-RPC-Error
    """

    code = None
    message = None


class ParseError(JsonRpcError):
    code = -32700
    message = u"Invalid JSON was received by the server."


class InvalidRequest(JsonRpcError):
    code = -32600
    message = u"The JSON sent is not a valid Request object."


class MethodNotFound(JsonRpcError):
    code = -32601
    message = u"The method does not exist / is not available."


class InvalidParams(JsonRpcError):
    code = -32602
    message = u"Invalid method parameter(s)."


class InternalError(JsonRpcError):
    code = -32603
    message = u"Internal JSON-RPC error."
