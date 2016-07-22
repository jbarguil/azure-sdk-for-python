# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ZoneDeleteResult(Model):
    """The response to a Zone Delete operation.

    :param azure_async_operation: Users can perform a Get on
     Azure-AsyncOperation to get the status of their delete Zone operations
    :type azure_async_operation: str
    :param status: Possible values include: 'InProgress', 'Succeeded',
     'Failed'
    :type status: str or :class:`OperationStatus
     <azure.mgmt.dns.models.OperationStatus>`
    :param status_code: Possible values include: 'Continue',
     'SwitchingProtocols', 'OK', 'Created', 'Accepted',
     'NonAuthoritativeInformation', 'NoContent', 'ResetContent',
     'PartialContent', 'MultipleChoices', 'Ambiguous', 'MovedPermanently',
     'Moved', 'Found', 'Redirect', 'SeeOther', 'RedirectMethod',
     'NotModified', 'UseProxy', 'Unused', 'TemporaryRedirect',
     'RedirectKeepVerb', 'BadRequest', 'Unauthorized', 'PaymentRequired',
     'Forbidden', 'NotFound', 'MethodNotAllowed', 'NotAcceptable',
     'ProxyAuthenticationRequired', 'RequestTimeout', 'Conflict', 'Gone',
     'LengthRequired', 'PreconditionFailed', 'RequestEntityTooLarge',
     'RequestUriTooLong', 'UnsupportedMediaType',
     'RequestedRangeNotSatisfiable', 'ExpectationFailed', 'UpgradeRequired',
     'InternalServerError', 'NotImplemented', 'BadGateway',
     'ServiceUnavailable', 'GatewayTimeout', 'HttpVersionNotSupported'
    :type status_code: str or :class:`HtpStatusCode
     <azure.mgmt.dns.models.HtpStatusCode>`
    :param request_id:
    :type request_id: str
    """ 

    _attribute_map = {
        'azure_async_operation': {'key': 'azureAsyncOperation', 'type': 'str'},
        'status': {'key': 'status', 'type': 'OperationStatus'},
        'status_code': {'key': 'statusCode', 'type': 'HtpStatusCode'},
        'request_id': {'key': 'requestId', 'type': 'str'},
    }

    def __init__(self, azure_async_operation=None, status=None, status_code=None, request_id=None):
        self.azure_async_operation = azure_async_operation
        self.status = status
        self.status_code = status_code
        self.request_id = request_id
