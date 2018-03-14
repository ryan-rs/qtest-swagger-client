# coding: utf-8

"""
    qTest Manager API Version 8.6 - 9.0

    qTest Manager API Version 8.6 - 9.0

    OpenAPI spec version: 8.6 - 9.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.project_api import ProjectApi


class TestProjectApi(unittest.TestCase):
    """ ProjectApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.project_api.ProjectApi()

    def tearDown(self):
        pass

    def test_create_project(self):
        """
        Test case for create_project

        Creates a Project
        """
        pass

    def test_get_current_profile(self):
        """
        Test case for get_current_profile

        Gets current user Permissions in a Project
        """
        pass

    def test_get_project(self):
        """
        Test case for get_project

        Gets a Project
        """
        pass

    def test_get_projects(self):
        """
        Test case for get_projects

        Gets multiple Projects
        """
        pass

    def test_get_users(self):
        """
        Test case for get_users

        Gets all Users in a Project
        """
        pass


if __name__ == '__main__':
    unittest.main()
