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


class RequirementPermission(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, create=False, edit=False, delete=False, view=False, edit_assignment=False, export=False, _import=False):
        """
        RequirementPermission - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'create': 'bool',
            'edit': 'bool',
            'delete': 'bool',
            'view': 'bool',
            'edit_assignment': 'bool',
            'export': 'bool',
            '_import': 'bool'
        }

        self.attribute_map = {
            'create': 'create',
            'edit': 'edit',
            'delete': 'delete',
            'view': 'view',
            'edit_assignment': 'edit_assignment',
            'export': 'export',
            '_import': 'import'
        }

        self._create = create
        self._edit = edit
        self._delete = delete
        self._view = view
        self._edit_assignment = edit_assignment
        self._export = export
        self.__import = _import

    @property
    def create(self):
        """
        Gets the create of this RequirementPermission.
        Can create Requirement 

        :return: The create of this RequirementPermission.
        :rtype: bool
        """
        return self._create

    @create.setter
    def create(self, create):
        """
        Sets the create of this RequirementPermission.
        Can create Requirement 

        :param create: The create of this RequirementPermission.
        :type: bool
        """

        self._create = create

    @property
    def edit(self):
        """
        Gets the edit of this RequirementPermission.
        Can edit Requirement

        :return: The edit of this RequirementPermission.
        :rtype: bool
        """
        return self._edit

    @edit.setter
    def edit(self, edit):
        """
        Sets the edit of this RequirementPermission.
        Can edit Requirement

        :param edit: The edit of this RequirementPermission.
        :type: bool
        """

        self._edit = edit

    @property
    def delete(self):
        """
        Gets the delete of this RequirementPermission.
        Can delete Requirement

        :return: The delete of this RequirementPermission.
        :rtype: bool
        """
        return self._delete

    @delete.setter
    def delete(self, delete):
        """
        Sets the delete of this RequirementPermission.
        Can delete Requirement

        :param delete: The delete of this RequirementPermission.
        :type: bool
        """

        self._delete = delete

    @property
    def view(self):
        """
        Gets the view of this RequirementPermission.
        Can view Requirement

        :return: The view of this RequirementPermission.
        :rtype: bool
        """
        return self._view

    @view.setter
    def view(self, view):
        """
        Sets the view of this RequirementPermission.
        Can view Requirement

        :param view: The view of this RequirementPermission.
        :type: bool
        """

        self._view = view

    @property
    def edit_assignment(self):
        """
        Gets the edit_assignment of this RequirementPermission.
        Can assign user to Requirement

        :return: The edit_assignment of this RequirementPermission.
        :rtype: bool
        """
        return self._edit_assignment

    @edit_assignment.setter
    def edit_assignment(self, edit_assignment):
        """
        Sets the edit_assignment of this RequirementPermission.
        Can assign user to Requirement

        :param edit_assignment: The edit_assignment of this RequirementPermission.
        :type: bool
        """

        self._edit_assignment = edit_assignment

    @property
    def export(self):
        """
        Gets the export of this RequirementPermission.
        Can export Requirement

        :return: The export of this RequirementPermission.
        :rtype: bool
        """
        return self._export

    @export.setter
    def export(self, export):
        """
        Sets the export of this RequirementPermission.
        Can export Requirement

        :param export: The export of this RequirementPermission.
        :type: bool
        """

        self._export = export

    @property
    def _import(self):
        """
        Gets the _import of this RequirementPermission.
        Can import Requirement

        :return: The _import of this RequirementPermission.
        :rtype: bool
        """
        return self.__import

    @_import.setter
    def _import(self, _import):
        """
        Sets the _import of this RequirementPermission.
        Can import Requirement

        :param _import: The _import of this RequirementPermission.
        :type: bool
        """

        self.__import = _import

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
        if not isinstance(other, RequirementPermission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
