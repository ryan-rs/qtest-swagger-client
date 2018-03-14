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
from swagger_client.apis.build_api import BuildApi


class TestBuildApi(unittest.TestCase):
    """ BuildApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.build_api.BuildApi()

    def tearDown(self):
        pass

    def test_create(self):
        """
        Test case for create

        Creates a Build
        """
        pass

    def test_delete(self):
        """
        Test case for delete

        Deletes a Build
        """
        pass

    def test_get(self):
        """
        Test case for get

        Gets a Build
        """
        pass

    def test_get_builds(self):
        """
        Test case for get_builds

        Gets multiple Builds
        """
        pass

    def test_update(self):
        """
        Test case for update

        Updates a Build
        """
        pass


if __name__ == '__main__':
    unittest.main()
