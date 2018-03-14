# swagger_client.TestcaseApi

All URIs are relative to *https://apitryout.qtestnet.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_comment**](TestcaseApi.md#add_comment) | **POST** /api/v3/projects/{projectId}/test-cases/{idOrKey}/comments | Adds a Comment to a Test Case
[**add_test_step**](TestcaseApi.md#add_test_step) | **POST** /api/v3/projects/{projectId}/test-cases/{testCaseId}/test-steps | Creates a Test Step
[**approve_test_case**](TestcaseApi.md#approve_test_case) | **PUT** /api/v3/projects/{projectId}/test-cases/{testCaseId}/approve | Approves a Test Case
[**create_test_case**](TestcaseApi.md#create_test_case) | **POST** /api/v3/projects/{projectId}/test-cases | Creates a Test Case
[**delete_comment**](TestcaseApi.md#delete_comment) | **DELETE** /api/v3/projects/{projectId}/test-cases/{idOrKey}/comments/{commentId} | Deletes a Comment of a Test Case
[**delete_test_case**](TestcaseApi.md#delete_test_case) | **DELETE** /api/v3/projects/{projectId}/test-cases/{testCaseId} | Deletes a Test Case
[**delete_test_step**](TestcaseApi.md#delete_test_step) | **DELETE** /api/v3/projects/{projectId}/test-cases/{testCaseId}/test-steps/{stepId} | Deletes a Test Step
[**get_comment**](TestcaseApi.md#get_comment) | **GET** /api/v3/projects/{projectId}/test-cases/{idOrKey}/comments/{commentId} | Gets a Comment of a Test Case
[**get_comments**](TestcaseApi.md#get_comments) | **GET** /api/v3/projects/{projectId}/test-cases/{idOrKey}/comments | Gets all Comments of a Test Case
[**get_test_case**](TestcaseApi.md#get_test_case) | **GET** /api/v3/projects/{projectId}/test-cases/{testCaseId} | Gets a Test Case
[**get_test_case_0**](TestcaseApi.md#get_test_case_0) | **GET** /api/v3/projects/{projectId}/test-cases/{testCaseId}/versions/{versionId} | Gets a version of a Test Case
[**get_test_cases**](TestcaseApi.md#get_test_cases) | **GET** /api/v3/projects/{projectId}/test-cases | Gets multiple Test Cases
[**get_test_step**](TestcaseApi.md#get_test_step) | **GET** /api/v3/projects/{projectId}/test-cases/{testCaseId}/test-steps/{stepId} | Gets a Test Step
[**get_test_steps**](TestcaseApi.md#get_test_steps) | **GET** /api/v3/projects/{projectId}/test-cases/{testCaseId}/test-steps | Gets Test Steps of a Test Case
[**get_test_steps_by_version**](TestcaseApi.md#get_test_steps_by_version) | **GET** /api/v3/projects/{projectId}/test-cases/{testCaseId}/versions/{versionId}/test-steps | Gets Test Steps of a Test Case version
[**get_versions**](TestcaseApi.md#get_versions) | **GET** /api/v3/projects/{projectId}/test-cases/{testCaseId}/versions | Gets all versions of a Test Case
[**update_comment**](TestcaseApi.md#update_comment) | **PUT** /api/v3/projects/{projectId}/test-cases/{idOrKey}/comments/{commentId} | Updates a Comment of a Test Case
[**update_test_case**](TestcaseApi.md#update_test_case) | **PUT** /api/v3/projects/{projectId}/test-cases/{testCaseId} | Updates a Test Case
[**update_test_step**](TestcaseApi.md#update_test_step) | **PUT** /api/v3/projects/{projectId}/test-cases/{testCaseId}/test-steps/{stepId} | Update a Test Step


# **add_comment**
> CommentResource add_comment(project_id, id_or_key, body)

Adds a Comment to a Test Case

To add a Comment to a Test Case  <strong>qTest Manager version:</strong> 7.5+

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TestcaseApi()
project_id = 789 # int | ID of the project
id_or_key = 'id_or_key_example' # str | PID or ID of the Test Case
body = swagger_client.CommentResource() # CommentResource | The comment's properties and its content

try: 
    # Adds a Comment to a Test Case
    api_response = api_instance.add_comment(project_id, id_or_key, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestcaseApi->add_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **id_or_key** | **str**| PID or ID of the Test Case | 
 **body** | [**CommentResource**](CommentResource.md)| The comment&#39;s properties and its content | 

### Return type

[**CommentResource**](CommentResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_test_step**
> TestStepResource add_test_step(project_id, test_case_id, body)

Creates a Test Step

To add a Test Step to a Test Case's latest version  <strong>qTest Manager version:</strong> 6+

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TestcaseApi()
project_id = 789 # int | ID of the project
test_case_id = 789 # int | ID of the Test Case
body = swagger_client.TestStepResource() # TestStepResource | Given resource to add a test step.

try: 
    # Creates a Test Step
    api_response = api_instance.add_test_step(project_id, test_case_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestcaseApi->add_test_step: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **test_case_id** | **int**| ID of the Test Case | 
 **body** | [**TestStepResource**](TestStepResource.md)| Given resource to add a test step. | 

### Return type

[**TestStepResource**](TestStepResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **approve_test_case**
> TestCaseWithCustomFieldResource approve_test_case(project_id, test_case_id)

Approves a Test Case

To approve a Test Case  <strong>qTest Manager version:</strong> 7.4+

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TestcaseApi()
project_id = 789 # int | ID of the project
test_case_id = 789 # int | ID of the Test Case

try: 
    # Approves a Test Case
    api_response = api_instance.approve_test_case(project_id, test_case_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestcaseApi->approve_test_case: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **test_case_id** | **int**| ID of the Test Case | 

### Return type

[**TestCaseWithCustomFieldResource**](TestCaseWithCustomFieldResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_test_case**
> TestCaseWithCustomFieldResource create_test_case(project_id, body)

Creates a Test Case

To create a Test Case  <strong>qTest Manager version:</strong> 4+

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TestcaseApi()
project_id = 789 # int | ID of the project
body = swagger_client.TestCaseWithCustomFieldResource() # TestCaseWithCustomFieldResource | Test Case properties, Test Steps, Attachments and other information to create a Test Case.  If <em>parent_id</em> is omitted, the Test Case will be created under \"Created via API\" Module

try: 
    # Creates a Test Case
    api_response = api_instance.create_test_case(project_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestcaseApi->create_test_case: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **body** | [**TestCaseWithCustomFieldResource**](TestCaseWithCustomFieldResource.md)| Test Case properties, Test Steps, Attachments and other information to create a Test Case.  If &lt;em&gt;parent_id&lt;/em&gt; is omitted, the Test Case will be created under \&quot;Created via API\&quot; Module | 

### Return type

[**TestCaseWithCustomFieldResource**](TestCaseWithCustomFieldResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comment**
> object delete_comment(project_id, id_or_key, comment_id)

Deletes a Comment of a Test Case

To delete a comment of a Test Case  <strong>qTest Manager version:</strong> 7.5+

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TestcaseApi()
project_id = 789 # int | ID of the project
id_or_key = 'id_or_key_example' # str | PID or ID of the Test Case
comment_id = 789 # int | ID of the comment.

try: 
    # Deletes a Comment of a Test Case
    api_response = api_instance.delete_comment(project_id, id_or_key, comment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestcaseApi->delete_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **id_or_key** | **str**| PID or ID of the Test Case | 
 **comment_id** | **int**| ID of the comment. | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_test_case**
> delete_test_case(project_id, test_case_id)

Deletes a Test Case

To delete Test Case  <strong>qTest Manager version:</strong> 6+

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TestcaseApi()
project_id = 789 # int | ID of the project
test_case_id = 789 # int | ID of the Test Case which needs to be deleted.

try: 
    # Deletes a Test Case
    api_instance.delete_test_case(project_id, test_case_id)
except ApiException as e:
    print("Exception when calling TestcaseApi->delete_test_case: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **test_case_id** | **int**| ID of the Test Case which needs to be deleted. | 

### Return type

void (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_test_step**
> object delete_test_step(project_id, test_case_id, step_id, update_version=update_version)

Deletes a Test Step

To delete a test step of a Test Case  <strong>qTest Manager version:</strong> 6+

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TestcaseApi()
project_id = 789 # int | ID of the project
test_case_id = 789 # int | ID of the Test Case
step_id = 789 # int | ID of the Test Step
update_version = true # bool | If you specify updateVersion=true, the test case version will be updated when the test step deleted. (optional)

try: 
    # Deletes a Test Step
    api_response = api_instance.delete_test_step(project_id, test_case_id, step_id, update_version=update_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestcaseApi->delete_test_step: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **test_case_id** | **int**| ID of the Test Case | 
 **step_id** | **int**| ID of the Test Step | 
 **update_version** | **bool**| If you specify updateVersion&#x3D;true, the test case version will be updated when the test step deleted. | [optional] 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comment**
> CommentResource get_comment(project_id, id_or_key, comment_id)

Gets a Comment of a Test Case

To retrieve a comment of a Test Case  <strong>qTest Manager version:</strong> 7.5+

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TestcaseApi()
project_id = 789 # int | ID of the project
id_or_key = 'id_or_key_example' # str | PID or ID of the Test Case
comment_id = 789 # int | ID of the comment.

try: 
    # Gets a Comment of a Test Case
    api_response = api_instance.get_comment(project_id, id_or_key, comment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestcaseApi->get_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **id_or_key** | **str**| PID or ID of the Test Case | 
 **comment_id** | **int**| ID of the comment. | 

### Return type

[**CommentResource**](CommentResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comments**
> PagedResourceCommentResource get_comments(project_id, id_or_key, page=page, page_size=page_size)

Gets all Comments of a Test Case

To retrieve all comments of a Test Case  <strong>qTest Manager version:</strong> 7.5+

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TestcaseApi()
project_id = 789 # int | ID of the project
id_or_key = 'id_or_key_example' # str | PID or ID of the Test Case whose comments you want to retrieve
page = 1 # int | By default the first page is returned but you can specify any page number to retrieve objects (optional) (default to 1)
page_size = 100 # int | The result is paginated. By the default, the number of objects in each page is 100 if this is omitted. You can specify your custom number (up to 999) in this parameter (optional) (default to 100)

try: 
    # Gets all Comments of a Test Case
    api_response = api_instance.get_comments(project_id, id_or_key, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestcaseApi->get_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **id_or_key** | **str**| PID or ID of the Test Case whose comments you want to retrieve | 
 **page** | **int**| By default the first page is returned but you can specify any page number to retrieve objects | [optional] [default to 1]
 **page_size** | **int**| The result is paginated. By the default, the number of objects in each page is 100 if this is omitted. You can specify your custom number (up to 999) in this parameter | [optional] [default to 100]

### Return type

[**PagedResourceCommentResource**](PagedResourceCommentResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_case**
> TestCaseWithCustomFieldResource get_test_case(project_id, test_case_id, version_id=version_id, expand=expand)

Gets a Test Case

To retrieve a Test Case  <strong>qTest Manager version:</strong> 6+

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TestcaseApi()
project_id = 789 # int | ID of the project
test_case_id = 789 # int | ID of the Test Case
version_id = 789 # int | ID of the Test Case version (optional)
expand = 'expand_example' # str | By default, Test Steps are excluded from the response. Specify <em>expand=teststep</em> to include Test Steps (optional)

try: 
    # Gets a Test Case
    api_response = api_instance.get_test_case(project_id, test_case_id, version_id=version_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestcaseApi->get_test_case: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **test_case_id** | **int**| ID of the Test Case | 
 **version_id** | **int**| ID of the Test Case version | [optional] 
 **expand** | **str**| By default, Test Steps are excluded from the response. Specify &lt;em&gt;expand&#x3D;teststep&lt;/em&gt; to include Test Steps | [optional] 

### Return type

[**TestCaseWithCustomFieldResource**](TestCaseWithCustomFieldResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_case_0**
> TestCaseWithCustomFieldResource get_test_case_0(project_id, test_case_id, version_id)

Gets a version of a Test Case

To retrieve a specific version of a Test Case  <strong>qTest Manager version:</strong> 4+

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TestcaseApi()
project_id = 789 # int | ID of the project
test_case_id = 789 # int | ID of the Test Case
version_id = 789 # int | ID of the Test Case version

try: 
    # Gets a version of a Test Case
    api_response = api_instance.get_test_case_0(project_id, test_case_id, version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestcaseApi->get_test_case_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **test_case_id** | **int**| ID of the Test Case | 
 **version_id** | **int**| ID of the Test Case version | 

### Return type

[**TestCaseWithCustomFieldResource**](TestCaseWithCustomFieldResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_cases**
> list[TestCaseWithCustomFieldResource] get_test_cases(project_id, page, size, parent_id=parent_id, expand_props=expand_props, expand_steps=expand_steps)

Gets multiple Test Cases

To retrieve all Test Cases or Test Cases which are located directly under a Module

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TestcaseApi()
project_id = 789 # int | ID of the project
page = 1 # int | By default the first page is returned. However, you can specify any page number to retrieve test cases. (default to 1)
size = 20 # int | The result is paginated. By the default, the number of requirements in each page is 20.  You can specify your custom number in this parameter. (default to 20)
parent_id = 789 # int | Module ID (optional)
expand_props = true # bool | By default, Test Case properties are included in the response. specify <em>expandProps=false</em> to exclude them (optional)
expand_steps = true # bool | By default, Test Steps are excluded from the response body. Input <em>expandSteps=true</em> to include Test Steps (optional)

try: 
    # Gets multiple Test Cases
    api_response = api_instance.get_test_cases(project_id, page, size, parent_id=parent_id, expand_props=expand_props, expand_steps=expand_steps)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestcaseApi->get_test_cases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **page** | **int**| By default the first page is returned. However, you can specify any page number to retrieve test cases. | [default to 1]
 **size** | **int**| The result is paginated. By the default, the number of requirements in each page is 20.  You can specify your custom number in this parameter. | [default to 20]
 **parent_id** | **int**| Module ID | [optional] 
 **expand_props** | **bool**| By default, Test Case properties are included in the response. specify &lt;em&gt;expandProps&#x3D;false&lt;/em&gt; to exclude them | [optional] 
 **expand_steps** | **bool**| By default, Test Steps are excluded from the response body. Input &lt;em&gt;expandSteps&#x3D;true&lt;/em&gt; to include Test Steps | [optional] 

### Return type

[**list[TestCaseWithCustomFieldResource]**](TestCaseWithCustomFieldResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_step**
> TestStepResource get_test_step(project_id, test_case_id, step_id)

Gets a Test Step

To retrieve a Test Step of a Test Case's latest version  <strong>qTest Manager version:</strong> 6+

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TestcaseApi()
project_id = 789 # int | ID of the project
test_case_id = 789 # int | ID of the Test Case
step_id = 789 # int | ID of the test step.

try: 
    # Gets a Test Step
    api_response = api_instance.get_test_step(project_id, test_case_id, step_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestcaseApi->get_test_step: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **test_case_id** | **int**| ID of the Test Case | 
 **step_id** | **int**| ID of the test step. | 

### Return type

[**TestStepResource**](TestStepResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_steps**
> list[TestStepResource] get_test_steps(project_id, test_case_id)

Gets Test Steps of a Test Case

To retrieve all Test Steps of a Test Case's latest version  <strong>qTest Manager version:</strong> 6+

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TestcaseApi()
project_id = 789 # int | ID of the project
test_case_id = 789 # int | ID of the Test Case

try: 
    # Gets Test Steps of a Test Case
    api_response = api_instance.get_test_steps(project_id, test_case_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestcaseApi->get_test_steps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **test_case_id** | **int**| ID of the Test Case | 

### Return type

[**list[TestStepResource]**](TestStepResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_steps_by_version**
> list[TestStepResource] get_test_steps_by_version(project_id, test_case_id, version_id, expand=expand)

Gets Test Steps of a Test Case version

To retrieve all Test Steps of a specific Test Case version

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TestcaseApi()
project_id = 789 # int | ID of the project
test_case_id = 789 # int | ID of the Test Case
version_id = 789 # int | ID of the Test Case version
expand = 'expand_example' # str | Specify <em>expand=calledteststep</em> to include Test Steps of the called Test Cases (optional)

try: 
    # Gets Test Steps of a Test Case version
    api_response = api_instance.get_test_steps_by_version(project_id, test_case_id, version_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestcaseApi->get_test_steps_by_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **test_case_id** | **int**| ID of the Test Case | 
 **version_id** | **int**| ID of the Test Case version | 
 **expand** | **str**| Specify &lt;em&gt;expand&#x3D;calledteststep&lt;/em&gt; to include Test Steps of the called Test Cases | [optional] 

### Return type

[**list[TestStepResource]**](TestStepResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_versions**
> list[TestCaseWithCustomFieldResource] get_versions(project_id, test_case_id)

Gets all versions of a Test Case

To retrieve all versions of a Test Case  <strong>qTest Manager version:</strong> 7.4+

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TestcaseApi()
project_id = 789 # int | ID of the project
test_case_id = 789 # int | ID of the test case

try: 
    # Gets all versions of a Test Case
    api_response = api_instance.get_versions(project_id, test_case_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestcaseApi->get_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **test_case_id** | **int**| ID of the test case | 

### Return type

[**list[TestCaseWithCustomFieldResource]**](TestCaseWithCustomFieldResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_comment**
> CommentResource update_comment(project_id, id_or_key, comment_id, body)

Updates a Comment of a Test Case

To modify a comment of a Test Case  <strong>qTest Manager version:</strong> 7.5+

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TestcaseApi()
project_id = 789 # int | ID of the project
id_or_key = 'id_or_key_example' # str | PID or ID of the Test Case
comment_id = 789 # int | ID of the comment.
body = swagger_client.CommentResource() # CommentResource | The comment's updated content

try: 
    # Updates a Comment of a Test Case
    api_response = api_instance.update_comment(project_id, id_or_key, comment_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestcaseApi->update_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **id_or_key** | **str**| PID or ID of the Test Case | 
 **comment_id** | **int**| ID of the comment. | 
 **body** | [**CommentResource**](CommentResource.md)| The comment&#39;s updated content | 

### Return type

[**CommentResource**](CommentResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_test_case**
> TestCaseWithCustomFieldResource update_test_case(project_id, test_case_id, body)

Updates a Test Case

To update a Test Case  <strong>qTest Manager version:</strong> 6+

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TestcaseApi()
project_id = 789 # int | ID of the project
test_case_id = 789 # int | ID of the Test Case which needs to be updated.
body = swagger_client.TestCaseWithCustomFieldResource() # TestCaseWithCustomFieldResource | Test Case properties, Test Steps and other information to update the Test Case

try: 
    # Updates a Test Case
    api_response = api_instance.update_test_case(project_id, test_case_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestcaseApi->update_test_case: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **test_case_id** | **int**| ID of the Test Case which needs to be updated. | 
 **body** | [**TestCaseWithCustomFieldResource**](TestCaseWithCustomFieldResource.md)| Test Case properties, Test Steps and other information to update the Test Case | 

### Return type

[**TestCaseWithCustomFieldResource**](TestCaseWithCustomFieldResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_test_step**
> TestStepResource update_test_step(project_id, test_case_id, step_id, body)

Update a Test Step

To update a Test Step of a Test Case's latest version  <strong>qTest Manager version:</strong> 6+

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TestcaseApi()
project_id = 789 # int | ID of the project
test_case_id = 789 # int | ID of the Test Case
step_id = 789 # int | ID of the Test Step
body = swagger_client.TestStepResource() # TestStepResource | Updated content of the Test Step

try: 
    # Update a Test Step
    api_response = api_instance.update_test_step(project_id, test_case_id, step_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestcaseApi->update_test_step: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **test_case_id** | **int**| ID of the Test Case | 
 **step_id** | **int**| ID of the Test Step | 
 **body** | [**TestStepResource**](TestStepResource.md)| Updated content of the Test Step | 

### Return type

[**TestStepResource**](TestStepResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

