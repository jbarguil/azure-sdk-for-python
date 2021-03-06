# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import ActionGroup
    from ._models_py3 import ActionGroupsInformation
    from ._models_py3 import ActionRule
    from ._models_py3 import ActionRuleProperties
    from ._models_py3 import ActionRulesList
    from ._models_py3 import Alert
    from ._models_py3 import AlertModification
    from ._models_py3 import AlertModificationItem
    from ._models_py3 import AlertModificationProperties
    from ._models_py3 import AlertProperties
    from ._models_py3 import AlertRule
    from ._models_py3 import AlertRulePatchObject
    from ._models_py3 import AlertRulesList
    from ._models_py3 import AlertsList
    from ._models_py3 import AlertsMetaData
    from ._models_py3 import AlertsMetaDataProperties
    from ._models_py3 import AlertsSummary
    from ._models_py3 import AlertsSummaryGroup
    from ._models_py3 import AlertsSummaryGroupItem
    from ._models_py3 import AzureResource
    from ._models_py3 import Condition
    from ._models_py3 import Conditions
    from ._models_py3 import Detector
    from ._models_py3 import Diagnostics
    from ._models_py3 import ErrorResponse
    from ._models_py3 import ErrorResponseAutoGenerated
    from ._models_py3 import ErrorResponseAutoGenerated2
    from ._models_py3 import ErrorResponseBody
    from ._models_py3 import ErrorResponseBodyAutoGenerated
    from ._models_py3 import ErrorResponseBodyAutoGenerated2
    from ._models_py3 import Essentials
    from ._models_py3 import ManagedResource
    from ._models_py3 import MonitorServiceDetails
    from ._models_py3 import MonitorServiceList
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationsList
    from ._models_py3 import PatchObject
    from ._models_py3 import Resource
    from ._models_py3 import Scope
    from ._models_py3 import SmartDetectorErrorResponse
    from ._models_py3 import SmartGroup
    from ._models_py3 import SmartGroupAggregatedProperty
    from ._models_py3 import SmartGroupModification
    from ._models_py3 import SmartGroupModificationItem
    from ._models_py3 import SmartGroupModificationProperties
    from ._models_py3 import SmartGroupsList
    from ._models_py3 import Suppression
    from ._models_py3 import SuppressionConfig
    from ._models_py3 import SuppressionSchedule
    from ._models_py3 import ThrottlingInformation
except (SyntaxError, ImportError):
    from ._models import ActionGroup  # type: ignore
    from ._models import ActionGroupsInformation  # type: ignore
    from ._models import ActionRule  # type: ignore
    from ._models import ActionRuleProperties  # type: ignore
    from ._models import ActionRulesList  # type: ignore
    from ._models import Alert  # type: ignore
    from ._models import AlertModification  # type: ignore
    from ._models import AlertModificationItem  # type: ignore
    from ._models import AlertModificationProperties  # type: ignore
    from ._models import AlertProperties  # type: ignore
    from ._models import AlertRule  # type: ignore
    from ._models import AlertRulePatchObject  # type: ignore
    from ._models import AlertRulesList  # type: ignore
    from ._models import AlertsList  # type: ignore
    from ._models import AlertsMetaData  # type: ignore
    from ._models import AlertsMetaDataProperties  # type: ignore
    from ._models import AlertsSummary  # type: ignore
    from ._models import AlertsSummaryGroup  # type: ignore
    from ._models import AlertsSummaryGroupItem  # type: ignore
    from ._models import AzureResource  # type: ignore
    from ._models import Condition  # type: ignore
    from ._models import Conditions  # type: ignore
    from ._models import Detector  # type: ignore
    from ._models import Diagnostics  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import ErrorResponseAutoGenerated  # type: ignore
    from ._models import ErrorResponseAutoGenerated2  # type: ignore
    from ._models import ErrorResponseBody  # type: ignore
    from ._models import ErrorResponseBodyAutoGenerated  # type: ignore
    from ._models import ErrorResponseBodyAutoGenerated2  # type: ignore
    from ._models import Essentials  # type: ignore
    from ._models import ManagedResource  # type: ignore
    from ._models import MonitorServiceDetails  # type: ignore
    from ._models import MonitorServiceList  # type: ignore
    from ._models import Operation  # type: ignore
    from ._models import OperationDisplay  # type: ignore
    from ._models import OperationsList  # type: ignore
    from ._models import PatchObject  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import Scope  # type: ignore
    from ._models import SmartDetectorErrorResponse  # type: ignore
    from ._models import SmartGroup  # type: ignore
    from ._models import SmartGroupAggregatedProperty  # type: ignore
    from ._models import SmartGroupModification  # type: ignore
    from ._models import SmartGroupModificationItem  # type: ignore
    from ._models import SmartGroupModificationProperties  # type: ignore
    from ._models import SmartGroupsList  # type: ignore
    from ._models import Suppression  # type: ignore
    from ._models import SuppressionConfig  # type: ignore
    from ._models import SuppressionSchedule  # type: ignore
    from ._models import ThrottlingInformation  # type: ignore

from ._alerts_management_client_enums import (
    ActionRuleStatus,
    ActionRuleType,
    AlertModificationEvent,
    AlertRuleState,
    AlertState,
    AlertsSortByFields,
    AlertsSummaryGroupByFields,
    Enum11,
    Identifier,
    MetadataIdentifier,
    MonitorCondition,
    MonitorService,
    Operator,
    ScopeType,
    Severity,
    SignalType,
    SmartGroupModificationEvent,
    SmartGroupsSortByFields,
    State,
    SuppressionType,
    TimeRange,
)

__all__ = [
    'ActionGroup',
    'ActionGroupsInformation',
    'ActionRule',
    'ActionRuleProperties',
    'ActionRulesList',
    'Alert',
    'AlertModification',
    'AlertModificationItem',
    'AlertModificationProperties',
    'AlertProperties',
    'AlertRule',
    'AlertRulePatchObject',
    'AlertRulesList',
    'AlertsList',
    'AlertsMetaData',
    'AlertsMetaDataProperties',
    'AlertsSummary',
    'AlertsSummaryGroup',
    'AlertsSummaryGroupItem',
    'AzureResource',
    'Condition',
    'Conditions',
    'Detector',
    'Diagnostics',
    'ErrorResponse',
    'ErrorResponseAutoGenerated',
    'ErrorResponseAutoGenerated2',
    'ErrorResponseBody',
    'ErrorResponseBodyAutoGenerated',
    'ErrorResponseBodyAutoGenerated2',
    'Essentials',
    'ManagedResource',
    'MonitorServiceDetails',
    'MonitorServiceList',
    'Operation',
    'OperationDisplay',
    'OperationsList',
    'PatchObject',
    'Resource',
    'Scope',
    'SmartDetectorErrorResponse',
    'SmartGroup',
    'SmartGroupAggregatedProperty',
    'SmartGroupModification',
    'SmartGroupModificationItem',
    'SmartGroupModificationProperties',
    'SmartGroupsList',
    'Suppression',
    'SuppressionConfig',
    'SuppressionSchedule',
    'ThrottlingInformation',
    'ActionRuleStatus',
    'ActionRuleType',
    'AlertModificationEvent',
    'AlertRuleState',
    'AlertState',
    'AlertsSortByFields',
    'AlertsSummaryGroupByFields',
    'Enum11',
    'Identifier',
    'MetadataIdentifier',
    'MonitorCondition',
    'MonitorService',
    'Operator',
    'ScopeType',
    'Severity',
    'SignalType',
    'SmartGroupModificationEvent',
    'SmartGroupsSortByFields',
    'State',
    'SuppressionType',
    'TimeRange',
]
