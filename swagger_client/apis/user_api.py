# coding: utf-8

"""
    qTest Manager API Version 8.6 - 9.0

    qTest Manager API Version 8.6 - 9.0

    OpenAPI spec version: 8.6 - 9.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class UserApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def assign_to_project(self, user_id, body, **kwargs):
        """
        Assigns a User to a Project
        To assign a User to a Project
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.assign_to_project(user_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int user_id: ID of the user. (required)
        :param AssignedProject body: The project ID and the assigned user profile in the project. If the profile is not provided, profile Developer is used by default (required)
        :return: AssignedProject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.assign_to_project_with_http_info(user_id, body, **kwargs)
        else:
            (data) = self.assign_to_project_with_http_info(user_id, body, **kwargs)
            return data

    def assign_to_project_with_http_info(self, user_id, body, **kwargs):
        """
        Assigns a User to a Project
        To assign a User to a Project
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.assign_to_project_with_http_info(user_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int user_id: ID of the user. (required)
        :param AssignedProject body: The project ID and the assigned user profile in the project. If the profile is not provided, profile Developer is used by default (required)
        :return: AssignedProject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method assign_to_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `assign_to_project`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `assign_to_project`")


        collection_formats = {}

        resource_path = '/api/v3/users/{userId}/projects'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = ['Authorization']

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='AssignedProject',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def assign_users_to_project(self, body, **kwargs):
        """
        Assigns multiple Users to a Project
        To assign a list of Users to a Project  <strong>qTest Manager version:</strong> 4+
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.assign_users_to_project(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param AssignedUsersProject body: ID of the Project and an array of assigned Users' IDs. If the profile is not provided, Developer profile is used by default (required)
        :return: AssignedUsersProject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.assign_users_to_project_with_http_info(body, **kwargs)
        else:
            (data) = self.assign_users_to_project_with_http_info(body, **kwargs)
            return data

    def assign_users_to_project_with_http_info(self, body, **kwargs):
        """
        Assigns multiple Users to a Project
        To assign a list of Users to a Project  <strong>qTest Manager version:</strong> 4+
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.assign_users_to_project_with_http_info(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param AssignedUsersProject body: ID of the Project and an array of assigned Users' IDs. If the profile is not provided, Developer profile is used by default (required)
        :return: AssignedUsersProject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method assign_users_to_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `assign_users_to_project`")


        collection_formats = {}

        resource_path = '/api/v3/users/projects'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = ['Authorization']

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='AssignedUsersProject',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def create_user(self, body, **kwargs):
        """
        Invites a User
        To invite a user to your qTest Manager instance and activate the account. If the password is omitted, the default \"<em>admin123</em>\" will be used  <strong>qTest Manager version:</strong> 4+
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_user(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param UserResource body: Invited user's information (required)
        :return: UserResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_user_with_http_info(body, **kwargs)
        else:
            (data) = self.create_user_with_http_info(body, **kwargs)
            return data

    def create_user_with_http_info(self, body, **kwargs):
        """
        Invites a User
        To invite a user to your qTest Manager instance and activate the account. If the password is omitted, the default \"<em>admin123</em>\" will be used  <strong>qTest Manager version:</strong> 4+
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_user_with_http_info(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param UserResource body: Invited user's information (required)
        :return: UserResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_user`")


        collection_formats = {}

        resource_path = '/api/v3/users'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = ['Authorization']

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='UserResource',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def find_by_user_name_or_email(self, **kwargs):
        """
        Queries Users by Username
        To query for users by their username  <strong>qTest Manager version:</strong> 8.4.2+
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.find_by_user_name_or_email(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str username: Login names (qTest login email, LDAP or SSO username) of users you want to query for. The API will return users which have been added to projects whose names contain the text specified in this parameter  <strong>IMPORTANT:</strong> Login name is case sensitive
        :param bool include_inactive_users: <em>includeInactiveUsers=false</em> - default value. Inactive users are excluded from the response  <em>includeInactiveUsers=true</em> - inactive users are included in the response
        :param bool pagination: <em>pagination=true</em> - default value. The result is paginated  <em>pagination=false</em> - the result is not paginated
        :param int page: By default the first page is returned but you can specify any page number to retrieve objects
        :param int page_size: The result is paginated. By the default, the number of objects in each page is 100 if this is omitted. You can specify your custom number (up to 999) in this parameter
        :return: SearchUserResourceExtensionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.find_by_user_name_or_email_with_http_info(**kwargs)
        else:
            (data) = self.find_by_user_name_or_email_with_http_info(**kwargs)
            return data

    def find_by_user_name_or_email_with_http_info(self, **kwargs):
        """
        Queries Users by Username
        To query for users by their username  <strong>qTest Manager version:</strong> 8.4.2+
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.find_by_user_name_or_email_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str username: Login names (qTest login email, LDAP or SSO username) of users you want to query for. The API will return users which have been added to projects whose names contain the text specified in this parameter  <strong>IMPORTANT:</strong> Login name is case sensitive
        :param bool include_inactive_users: <em>includeInactiveUsers=false</em> - default value. Inactive users are excluded from the response  <em>includeInactiveUsers=true</em> - inactive users are included in the response
        :param bool pagination: <em>pagination=true</em> - default value. The result is paginated  <em>pagination=false</em> - the result is not paginated
        :param int page: By default the first page is returned but you can specify any page number to retrieve objects
        :param int page_size: The result is paginated. By the default, the number of objects in each page is 100 if this is omitted. You can specify your custom number (up to 999) in this parameter
        :return: SearchUserResourceExtensionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['username', 'include_inactive_users', 'pagination', 'page', 'page_size']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method find_by_user_name_or_email" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/api/v3/users/search'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'username' in params:
            query_params['username'] = params['username']
        if 'include_inactive_users' in params:
            query_params['includeInactiveUsers'] = params['include_inactive_users']
        if 'pagination' in params:
            query_params['pagination'] = params['pagination']
        if 'page' in params:
            query_params['page'] = params['page']
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Authorization']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='SearchUserResourceExtensionResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def find_users_by_projects_name(self, **kwargs):
        """
        Queries Users by Project Name
        To query for users by names of their assigned projects  - Admin users with <em>Manage Client Users</em> permission can query users in any projects  - For other users: the API only returns users within projects to which the requesting user is assigned
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.find_users_by_projects_name(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str project_name: Name of the project whose users you want to query for. The API will return users which have been added to projects whose names contain the text specified in this parameter  <strong>IMPORTANT:</strong> Project name is case sensitive
        :param bool inactive: <em>inactive=false</em> - default value. Inactive users are excluded from the response  <em>inactive=true</em> - include inactive users
        :param bool pagination: <em>pagination=true</em> - default value. The result is paginated  <em>pagination=false</em> - the result is not paginated
        :param int page: By default the first page is returned but you can specify any page number to retrieve objects
        :param int page_size: The result is paginated. By the default, the number of objects in each page is 100 if this is omitted. You can specify your custom number (up to 999) in this parameter
        :return: SearchUserResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.find_users_by_projects_name_with_http_info(**kwargs)
        else:
            (data) = self.find_users_by_projects_name_with_http_info(**kwargs)
            return data

    def find_users_by_projects_name_with_http_info(self, **kwargs):
        """
        Queries Users by Project Name
        To query for users by names of their assigned projects  - Admin users with <em>Manage Client Users</em> permission can query users in any projects  - For other users: the API only returns users within projects to which the requesting user is assigned
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.find_users_by_projects_name_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str project_name: Name of the project whose users you want to query for. The API will return users which have been added to projects whose names contain the text specified in this parameter  <strong>IMPORTANT:</strong> Project name is case sensitive
        :param bool inactive: <em>inactive=false</em> - default value. Inactive users are excluded from the response  <em>inactive=true</em> - include inactive users
        :param bool pagination: <em>pagination=true</em> - default value. The result is paginated  <em>pagination=false</em> - the result is not paginated
        :param int page: By default the first page is returned but you can specify any page number to retrieve objects
        :param int page_size: The result is paginated. By the default, the number of objects in each page is 100 if this is omitted. You can specify your custom number (up to 999) in this parameter
        :return: SearchUserResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_name', 'inactive', 'pagination', 'page', 'page_size']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method find_users_by_projects_name" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/api/v3/search/user'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'project_name' in params:
            query_params['projectName'] = params['project_name']
        if 'inactive' in params:
            query_params['inactive'] = params['inactive']
        if 'pagination' in params:
            query_params['pagination'] = params['pagination']
        if 'page' in params:
            query_params['page'] = params['page']
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Authorization']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='SearchUserResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_avatar(self, user_id, **kwargs):
        """
        Gets a User's Avatar
        To retrieve a User's Avatar
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_avatar(user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int user_id: ID of the user. (required)
        :return: OutputStream
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_avatar_with_http_info(user_id, **kwargs)
        else:
            (data) = self.get_avatar_with_http_info(user_id, **kwargs)
            return data

    def get_avatar_with_http_info(self, user_id, **kwargs):
        """
        Gets a User's Avatar
        To retrieve a User's Avatar
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_avatar_with_http_info(user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int user_id: ID of the user. (required)
        :return: OutputStream
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_avatar" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_avatar`")


        collection_formats = {}

        resource_path = '/api/v3/users/{userId}/avatar'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Authorization']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='OutputStream',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_user_by_id(self, user_id, **kwargs):
        """
        Gets a User
        To retrieve a User's information
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_user_by_id(user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int user_id: ID of the user. (required)
        :return: UserResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_user_by_id_with_http_info(user_id, **kwargs)
        else:
            (data) = self.get_user_by_id_with_http_info(user_id, **kwargs)
            return data

    def get_user_by_id_with_http_info(self, user_id, **kwargs):
        """
        Gets a User
        To retrieve a User's information
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_user_by_id_with_http_info(user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int user_id: ID of the user. (required)
        :return: UserResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_user_by_id`")


        collection_formats = {}

        resource_path = '/api/v3/users/{userId}'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Authorization']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='UserResource',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def reevaluate_token(self, **kwargs):
        """
        Gets current user's information
        To retrieve your information such as username, email, first name, and last name
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.reevaluate_token(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param bool include_inaccessible_apps:
        :return: LoggedUser
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.reevaluate_token_with_http_info(**kwargs)
        else:
            (data) = self.reevaluate_token_with_http_info(**kwargs)
            return data

    def reevaluate_token_with_http_info(self, **kwargs):
        """
        Gets current user's information
        To retrieve your information such as username, email, first name, and last name
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.reevaluate_token_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param bool include_inaccessible_apps:
        :return: LoggedUser
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['include_inaccessible_apps']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reevaluate_token" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/api/v3/re-evaluation'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'include_inaccessible_apps' in params:
            query_params['includeInaccessibleApps'] = params['include_inaccessible_apps']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Authorization']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='LoggedUser',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
