# coding: utf-8

"""
    qTest Manager API Version 8.6 - 9.0

    qTest Manager API Version 8.6 - 9.0

    OpenAPI spec version: 8.6 - 9.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AutomationRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, skip_creating_automation_module=False, test_suite=None, parent_module=None, test_logs=None, execution_date=None, test_cycle=None):
        """
        AutomationRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'skip_creating_automation_module': 'bool',
            'test_suite': 'str',
            'parent_module': 'str',
            'test_logs': 'list[AutomationTestLogResource]',
            'execution_date': 'datetime',
            'test_cycle': 'str'
        }

        self.attribute_map = {
            'skip_creating_automation_module': 'skipCreatingAutomationModule',
            'test_suite': 'test_suite',
            'parent_module': 'parent_module',
            'test_logs': 'test_logs',
            'execution_date': 'execution_date',
            'test_cycle': 'test_cycle'
        }

        self._skip_creating_automation_module = skip_creating_automation_module
        self._test_suite = test_suite
        self._parent_module = parent_module
        self._test_logs = test_logs
        self._execution_date = execution_date
        self._test_cycle = test_cycle

    @property
    def skip_creating_automation_module(self):
        """
        Gets the skip_creating_automation_module of this AutomationRequest.

        :return: The skip_creating_automation_module of this AutomationRequest.
        :rtype: bool
        """
        return self._skip_creating_automation_module

    @skip_creating_automation_module.setter
    def skip_creating_automation_module(self, skip_creating_automation_module):
        """
        Sets the skip_creating_automation_module of this AutomationRequest.

        :param skip_creating_automation_module: The skip_creating_automation_module of this AutomationRequest.
        :type: bool
        """

        self._skip_creating_automation_module = skip_creating_automation_module

    @property
    def test_suite(self):
        """
        Gets the test_suite of this AutomationRequest.
        ID or PID of Test Suite

        :return: The test_suite of this AutomationRequest.
        :rtype: str
        """
        return self._test_suite

    @test_suite.setter
    def test_suite(self, test_suite):
        """
        Sets the test_suite of this AutomationRequest.
        ID or PID of Test Suite

        :param test_suite: The test_suite of this AutomationRequest.
        :type: str
        """

        self._test_suite = test_suite

    @property
    def parent_module(self):
        """
        Gets the parent_module of this AutomationRequest.
        ID or PID of Module

        :return: The parent_module of this AutomationRequest.
        :rtype: str
        """
        return self._parent_module

    @parent_module.setter
    def parent_module(self, parent_module):
        """
        Sets the parent_module of this AutomationRequest.
        ID or PID of Module

        :param parent_module: The parent_module of this AutomationRequest.
        :type: str
        """

        self._parent_module = parent_module

    @property
    def test_logs(self):
        """
        Gets the test_logs of this AutomationRequest.
        Array of Test Log

        :return: The test_logs of this AutomationRequest.
        :rtype: list[AutomationTestLogResource]
        """
        return self._test_logs

    @test_logs.setter
    def test_logs(self, test_logs):
        """
        Sets the test_logs of this AutomationRequest.
        Array of Test Log

        :param test_logs: The test_logs of this AutomationRequest.
        :type: list[AutomationTestLogResource]
        """
        if test_logs is None:
            raise ValueError("Invalid value for `test_logs`, must not be `None`")

        self._test_logs = test_logs

    @property
    def execution_date(self):
        """
        Gets the execution_date of this AutomationRequest.
        Execution Date

        :return: The execution_date of this AutomationRequest.
        :rtype: datetime
        """
        return self._execution_date

    @execution_date.setter
    def execution_date(self, execution_date):
        """
        Sets the execution_date of this AutomationRequest.
        Execution Date

        :param execution_date: The execution_date of this AutomationRequest.
        :type: datetime
        """

        self._execution_date = execution_date

    @property
    def test_cycle(self):
        """
        Gets the test_cycle of this AutomationRequest.
        ID or PID of Test Cycle

        :return: The test_cycle of this AutomationRequest.
        :rtype: str
        """
        return self._test_cycle

    @test_cycle.setter
    def test_cycle(self, test_cycle):
        """
        Sets the test_cycle of this AutomationRequest.
        ID or PID of Test Cycle

        :param test_cycle: The test_cycle of this AutomationRequest.
        :type: str
        """

        self._test_cycle = test_cycle

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, AutomationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other