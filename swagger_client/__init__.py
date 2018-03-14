# coding: utf-8

"""
    qTest Manager API Version 8.6 - 9.0

    qTest Manager API Version 8.6 - 9.0

    OpenAPI spec version: 8.6 - 9.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into sdk package
from .models.admin_profile import AdminProfile
from .models.allowed_value_resource import AllowedValueResource
from .models.app_detail import AppDetail
from .models.artifact_history_resource import ArtifactHistoryResource
from .models.artifact_search_params import ArtifactSearchParams
from .models.assigned_project import AssignedProject
from .models.assigned_users_profile import AssignedUsersProfile
from .models.assigned_users_project import AssignedUsersProject
from .models.attachment_author import AttachmentAuthor
from .models.attachment_resource import AttachmentResource
from .models.automation_request import AutomationRequest
from .models.automation_schedule_creation_api import AutomationScheduleCreationAPI
from .models.automation_test_log_resource import AutomationTestLogResource
from .models.automation_test_step_log import AutomationTestStepLog
from .models.build_permission import BuildPermission
from .models.build_resource import BuildResource
from .models.comment_query_params import CommentQueryParams
from .models.comment_resource import CommentResource
from .models.defect_field_mapping import DefectFieldMapping
from .models.defect_mapping import DefectMapping
from .models.defect_permission import DefectPermission
from .models.defect_resource import DefectResource
from .models.defect_tracking_system import DefectTrackingSystem
from .models.field_resource import FieldResource
from .models.history_change import HistoryChange
from .models.history_query_params import HistoryQueryParams
from .models.history_resource import HistoryResource
from .models.link import Link
from .models.linked_artifact import LinkedArtifact
from .models.linked_artifact_container import LinkedArtifactContainer
from .models.linked_defect_resource import LinkedDefectResource
from .models.linked_object import LinkedObject
from .models.logged_user import LoggedUser
from .models.message import Message
from .models.module_permission import ModulePermission
from .models.module_resource import ModuleResource
from .models.o_auth_response import OAuthResponse
from .models.output_stream import OutputStream
from .models.paged_resource import PagedResource
from .models.paged_resource_attachment_resource import PagedResourceAttachmentResource
from .models.paged_resource_comment_resource import PagedResourceCommentResource
from .models.profile import Profile
from .models.project_admin_permission import ProjectAdminPermission
from .models.project_resource import ProjectResource
from .models.project_setting_permission import ProjectSettingPermission
from .models.property_resource import PropertyResource
from .models.query_comment_resource import QueryCommentResource
from .models.queue_processing_response import QueueProcessingResponse
from .models.release_permission import ReleasePermission
from .models.release_with_custom_field_resource import ReleaseWithCustomFieldResource
from .models.report_permission import ReportPermission
from .models.requirement_permission import RequirementPermission
from .models.requirement_resource import RequirementResource
from .models.resource_support import ResourceSupport
from .models.schedule_permission import SchedulePermission
from .models.search_user_resource import SearchUserResource
from .models.search_user_resource_extension_response import SearchUserResourceExtensionResponse
from .models.search_user_response import SearchUserResponse
from .models.session_manager_permission import SessionManagerPermission
from .models.status_resource import StatusResource
from .models.test_case_permission import TestCasePermission
from .models.test_case_with_custom_field_resource import TestCaseWithCustomFieldResource
from .models.test_cycle_permission import TestCyclePermission
from .models.test_cycle_resource import TestCycleResource
from .models.test_log_list_resource import TestLogListResource
from .models.test_log_resource import TestLogResource
from .models.test_run_list_resource import TestRunListResource
from .models.test_run_permission import TestRunPermission
from .models.test_run_with_custom_field_resource import TestRunWithCustomFieldResource
from .models.test_step_log_resource import TestStepLogResource
from .models.test_step_resource import TestStepResource
from .models.test_suite_permission import TestSuitePermission
from .models.test_suite_with_custom_field_resource import TestSuiteWithCustomFieldResource
from .models.traceability_requirement import TraceabilityRequirement
from .models.user_profile import UserProfile
from .models.user_profile_response import UserProfileResponse
from .models.user_resource import UserResource
from .models.user_resource_extension import UserResourceExtension

# import apis into sdk package
from .apis.attachment_api import AttachmentApi
from .apis.automationjob_api import AutomationjobApi
from .apis.build_api import BuildApi
from .apis.common_api import CommonApi
from .apis.defect_api import DefectApi
from .apis.field_api import FieldApi
from .apis.login_api import LoginApi
from .apis.module_api import ModuleApi
from .apis.objectlink_api import ObjectlinkApi
from .apis.project_api import ProjectApi
from .apis.release_api import ReleaseApi
from .apis.requirement_api import RequirementApi
from .apis.search_api import SearchApi
from .apis.testcase_api import TestcaseApi
from .apis.testcycle_api import TestcycleApi
from .apis.testlog_api import TestlogApi
from .apis.testrun_api import TestrunApi
from .apis.testsuite_api import TestsuiteApi
from .apis.user_api import UserApi
from .apis.userprofile_api import UserprofileApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

configuration = Configuration()
