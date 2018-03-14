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


class HistoryChange(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, field=None, old_value=None, new_value=None):
        """
        HistoryChange - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'field': 'str',
            'old_value': 'str',
            'new_value': 'str'
        }

        self.attribute_map = {
            'field': 'field',
            'old_value': 'old_value',
            'new_value': 'new_value'
        }

        self._field = field
        self._old_value = old_value
        self._new_value = new_value

    @property
    def field(self):
        """
        Gets the field of this HistoryChange.

        :return: The field of this HistoryChange.
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """
        Sets the field of this HistoryChange.

        :param field: The field of this HistoryChange.
        :type: str
        """

        self._field = field

    @property
    def old_value(self):
        """
        Gets the old_value of this HistoryChange.

        :return: The old_value of this HistoryChange.
        :rtype: str
        """
        return self._old_value

    @old_value.setter
    def old_value(self, old_value):
        """
        Sets the old_value of this HistoryChange.

        :param old_value: The old_value of this HistoryChange.
        :type: str
        """

        self._old_value = old_value

    @property
    def new_value(self):
        """
        Gets the new_value of this HistoryChange.

        :return: The new_value of this HistoryChange.
        :rtype: str
        """
        return self._new_value

    @new_value.setter
    def new_value(self, new_value):
        """
        Sets the new_value of this HistoryChange.

        :param new_value: The new_value of this HistoryChange.
        :type: str
        """

        self._new_value = new_value

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
        if not isinstance(other, HistoryChange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
