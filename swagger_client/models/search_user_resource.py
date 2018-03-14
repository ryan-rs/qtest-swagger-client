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


class SearchUserResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, links=None, id=None, username=None, email=None, password=None, first_name=None, last_name=None, status=None, avatar=None, ldap_username=None, timezone_offset=None, country_name=None, assigned_projects=None):
        """
        SearchUserResource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'links': 'list[Link]',
            'id': 'int',
            'username': 'str',
            'email': 'str',
            'password': 'str',
            'first_name': 'str',
            'last_name': 'str',
            'status': 'int',
            'avatar': 'str',
            'ldap_username': 'str',
            'timezone_offset': 'str',
            'country_name': 'str',
            'assigned_projects': 'list[int]'
        }

        self.attribute_map = {
            'links': 'links',
            'id': 'id',
            'username': 'username',
            'email': 'email',
            'password': 'password',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'status': 'status',
            'avatar': 'avatar',
            'ldap_username': 'ldap_username',
            'timezone_offset': 'timezone_offset',
            'country_name': 'country_name',
            'assigned_projects': 'assigned_projects'
        }

        self._links = links
        self._id = id
        self._username = username
        self._email = email
        self._password = password
        self._first_name = first_name
        self._last_name = last_name
        self._status = status
        self._avatar = avatar
        self._ldap_username = ldap_username
        self._timezone_offset = timezone_offset
        self._country_name = country_name
        self._assigned_projects = assigned_projects

    @property
    def links(self):
        """
        Gets the links of this SearchUserResource.
        Link to resource

        :return: The links of this SearchUserResource.
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this SearchUserResource.
        Link to resource

        :param links: The links of this SearchUserResource.
        :type: list[Link]
        """

        self._links = links

    @property
    def id(self):
        """
        Gets the id of this SearchUserResource.
        ID of the User

        :return: The id of this SearchUserResource.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SearchUserResource.
        ID of the User

        :param id: The id of this SearchUserResource.
        :type: int
        """

        self._id = id

    @property
    def username(self):
        """
        Gets the username of this SearchUserResource.
        Login username of the User

        :return: The username of this SearchUserResource.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this SearchUserResource.
        Login username of the User

        :param username: The username of this SearchUserResource.
        :type: str
        """

        self._username = username

    @property
    def email(self):
        """
        Gets the email of this SearchUserResource.
        Contact email of the User

        :return: The email of this SearchUserResource.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this SearchUserResource.
        Contact email of the User

        :param email: The email of this SearchUserResource.
        :type: str
        """

        self._email = email

    @property
    def password(self):
        """
        Gets the password of this SearchUserResource.

        :return: The password of this SearchUserResource.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this SearchUserResource.

        :param password: The password of this SearchUserResource.
        :type: str
        """

        self._password = password

    @property
    def first_name(self):
        """
        Gets the first_name of this SearchUserResource.
        First name of the User

        :return: The first_name of this SearchUserResource.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this SearchUserResource.
        First name of the User

        :param first_name: The first_name of this SearchUserResource.
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this SearchUserResource.
        Last name of the User

        :return: The last_name of this SearchUserResource.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this SearchUserResource.
        Last name of the User

        :param last_name: The last_name of this SearchUserResource.
        :type: str
        """

        self._last_name = last_name

    @property
    def status(self):
        """
        Gets the status of this SearchUserResource.
        Status of the User

        :return: The status of this SearchUserResource.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this SearchUserResource.
        Status of the User

        :param status: The status of this SearchUserResource.
        :type: int
        """

        self._status = status

    @property
    def avatar(self):
        """
        Gets the avatar of this SearchUserResource.
        Avatar URL of the User

        :return: The avatar of this SearchUserResource.
        :rtype: str
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        """
        Sets the avatar of this SearchUserResource.
        Avatar URL of the User

        :param avatar: The avatar of this SearchUserResource.
        :type: str
        """

        self._avatar = avatar

    @property
    def ldap_username(self):
        """
        Gets the ldap_username of this SearchUserResource.
        LDAP username

        :return: The ldap_username of this SearchUserResource.
        :rtype: str
        """
        return self._ldap_username

    @ldap_username.setter
    def ldap_username(self, ldap_username):
        """
        Sets the ldap_username of this SearchUserResource.
        LDAP username

        :param ldap_username: The ldap_username of this SearchUserResource.
        :type: str
        """

        self._ldap_username = ldap_username

    @property
    def timezone_offset(self):
        """
        Gets the timezone_offset of this SearchUserResource.
        Timezone offset

        :return: The timezone_offset of this SearchUserResource.
        :rtype: str
        """
        return self._timezone_offset

    @timezone_offset.setter
    def timezone_offset(self, timezone_offset):
        """
        Sets the timezone_offset of this SearchUserResource.
        Timezone offset

        :param timezone_offset: The timezone_offset of this SearchUserResource.
        :type: str
        """

        self._timezone_offset = timezone_offset

    @property
    def country_name(self):
        """
        Gets the country_name of this SearchUserResource.
        Country name of configured timezone

        :return: The country_name of this SearchUserResource.
        :rtype: str
        """
        return self._country_name

    @country_name.setter
    def country_name(self, country_name):
        """
        Sets the country_name of this SearchUserResource.
        Country name of configured timezone

        :param country_name: The country_name of this SearchUserResource.
        :type: str
        """

        self._country_name = country_name

    @property
    def assigned_projects(self):
        """
        Gets the assigned_projects of this SearchUserResource.
        Arrays of Project that user assigned to

        :return: The assigned_projects of this SearchUserResource.
        :rtype: list[int]
        """
        return self._assigned_projects

    @assigned_projects.setter
    def assigned_projects(self, assigned_projects):
        """
        Sets the assigned_projects of this SearchUserResource.
        Arrays of Project that user assigned to

        :param assigned_projects: The assigned_projects of this SearchUserResource.
        :type: list[int]
        """

        self._assigned_projects = assigned_projects

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
        if not isinstance(other, SearchUserResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
