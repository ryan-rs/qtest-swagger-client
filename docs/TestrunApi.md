# swagger_client.TestrunApi

All URIs are relative to *https://apitryout.qtestnet.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_comment**](TestrunApi.md#add_comment) | **POST** /api/v3/projects/{projectId}/test-runs/{idOrKey}/comments | Adds a Comment to a Test Run
[**create**](TestrunApi.md#create) | **POST** /api/v3/projects/{projectId}/test-runs | Creates a Test Run
[**delete**](TestrunApi.md#delete) | **DELETE** /api/v3/projects/{projectId}/test-runs/{testRunId} | Deletes a Test Run
[**delete_comment**](TestrunApi.md#delete_comment) | **DELETE** /api/v3/projects/{projectId}/test-runs/{idOrKey}/comments/{commentId} | Deletes a Comment of a Test Run
[**get**](TestrunApi.md#get) | **GET** /api/v3/projects/{projectId}/test-runs/{testRunId} | Gets a Test Run
[**get_comment**](TestrunApi.md#get_comment) | **GET** /api/v3/projects/{projectId}/test-runs/{idOrKey}/comments/{commentId} | Gets a Comment from a Test Run
[**get_comments**](TestrunApi.md#get_comments) | **GET** /api/v3/projects/{projectId}/test-runs/{idOrKey}/comments | Gets all Comments of a Test Run
[**get_of**](TestrunApi.md#get_of) | **GET** /api/v3/projects/{projectId}/test-runs | Gets multiple Test Runs
[**get_status_valuable**](TestrunApi.md#get_status_valuable) | **GET** /api/v3/projects/{projectId}/test-runs/execution-statuses | Gets Test Run statuses
[**update**](TestrunApi.md#update) | **PUT** /api/v3/projects/{projectId}/test-runs/{testRunId} | Updates a Test Run
[**update_comment**](TestrunApi.md#update_comment) | **PUT** /api/v3/projects/{projectId}/test-runs/{idOrKey}/comments/{commentId} | Updates a Comment of a Test Run


# **add_comment**
> CommentResource add_comment(project_id, id_or_key, body)

Adds a Comment to a Test Run

To add a Comment to a Test Run  <strong>qTest Manager version:</strong> 7.5+

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
api_instance = swagger_client.TestrunApi()
project_id = 789 # int | ID of the project
id_or_key = 'id_or_key_example' # str | The PID or ID of the Test Run.
body = swagger_client.CommentResource() # CommentResource | The Comment's content

try: 
    # Adds a Comment to a Test Run
    api_response = api_instance.add_comment(project_id, id_or_key, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestrunApi->add_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **id_or_key** | **str**| The PID or ID of the Test Run. | 
 **body** | [**CommentResource**](CommentResource.md)| The Comment&#39;s content | 

### Return type

[**CommentResource**](CommentResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> TestRunWithCustomFieldResource create(project_id, body, parent_id=parent_id, parent_type=parent_type)

Creates a Test Run

To create a Test Run under root or a container (Release, Test Cycle or Test Suite)  <strong>qTest Manager version:</strong> 6+You can optionally specify a parent in the request parameter to create its test runs.  The associated Test Case is specified in the request body

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
api_instance = swagger_client.TestrunApi()
project_id = 789 # int | ID of the project
body = swagger_client.TestRunWithCustomFieldResource() # TestRunWithCustomFieldResource | The Test Run's properties and its associated Test Case
parent_id = 789 # int | ID of the container  Input 0 (zero) to get Test Runs directly under root (optional)
parent_type = 'parent_type_example' # str | Type of the container. Valid values include <em>root</em>, <em>release</em>, <em>test-cycle</em>, and <em>test-suite</em> (optional)

try: 
    # Creates a Test Run
    api_response = api_instance.create(project_id, body, parent_id=parent_id, parent_type=parent_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestrunApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **body** | [**TestRunWithCustomFieldResource**](TestRunWithCustomFieldResource.md)| The Test Run&#39;s properties and its associated Test Case | 
 **parent_id** | **int**| ID of the container  Input 0 (zero) to get Test Runs directly under root | [optional] 
 **parent_type** | **str**| Type of the container. Valid values include &lt;em&gt;root&lt;/em&gt;, &lt;em&gt;release&lt;/em&gt;, &lt;em&gt;test-cycle&lt;/em&gt;, and &lt;em&gt;test-suite&lt;/em&gt; | [optional] 

### Return type

[**TestRunWithCustomFieldResource**](TestRunWithCustomFieldResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> Message delete(project_id, test_run_id)

Deletes a Test Run

To delete a Test Run  <strong>qTest Manager version:</strong> 6+

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
api_instance = swagger_client.TestrunApi()
project_id = 789 # int | ID of the project
test_run_id = 789 # int | ID of the Test Run

try: 
    # Deletes a Test Run
    api_response = api_instance.delete(project_id, test_run_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestrunApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **test_run_id** | **int**| ID of the Test Run | 

### Return type

[**Message**](Message.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comment**
> object delete_comment(project_id, id_or_key, comment_id)

Deletes a Comment of a Test Run

To delete a Comment of a Test Run  <strong>qTest Manager version:</strong> 7.5+

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
api_instance = swagger_client.TestrunApi()
project_id = 789 # int | ID of the project
id_or_key = 'id_or_key_example' # str | PID or ID of the Test Run.
comment_id = 789 # int | ID of the comment which you want to delete.

try: 
    # Deletes a Comment of a Test Run
    api_response = api_instance.delete_comment(project_id, id_or_key, comment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestrunApi->delete_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **id_or_key** | **str**| PID or ID of the Test Run. | 
 **comment_id** | **int**| ID of the comment which you want to delete. | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> TestRunWithCustomFieldResource get(project_id, test_run_id, expand=expand)

Gets a Test Run

To retrieve a Test Run  <strong>qTest Manager version:</strong> 4+

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
api_instance = swagger_client.TestrunApi()
project_id = 789 # int | ID of the project
test_run_id = 789 # int | ID of the Test Run.
expand = 'expand_example' # str | Valid values include:   i)<em>testcase</em> - to expand the associated Test Case in the response;   ii) <em>testcase.teststep</em> - to expand the associated Test Case and its Test Steps in the response (optional)

try: 
    # Gets a Test Run
    api_response = api_instance.get(project_id, test_run_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestrunApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **test_run_id** | **int**| ID of the Test Run. | 
 **expand** | **str**| Valid values include:   i)&lt;em&gt;testcase&lt;/em&gt; - to expand the associated Test Case in the response;   ii) &lt;em&gt;testcase.teststep&lt;/em&gt; - to expand the associated Test Case and its Test Steps in the response | [optional] 

### Return type

[**TestRunWithCustomFieldResource**](TestRunWithCustomFieldResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comment**
> CommentResource get_comment(project_id, id_or_key, comment_id)

Gets a Comment from a Test Run

To retrieve a specific Comment from a Test Run  <strong>qTest Manager version:</strong> 7.5+

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
api_instance = swagger_client.TestrunApi()
project_id = 789 # int | ID of the project
id_or_key = 'id_or_key_example' # str | PID or ID of the Test Run.
comment_id = 789 # int | ID of the Comment

try: 
    # Gets a Comment from a Test Run
    api_response = api_instance.get_comment(project_id, id_or_key, comment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestrunApi->get_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **id_or_key** | **str**| PID or ID of the Test Run. | 
 **comment_id** | **int**| ID of the Comment | 

### Return type

[**CommentResource**](CommentResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comments**
> PagedResourceCommentResource get_comments(project_id, id_or_key)

Gets all Comments of a Test Run

To retrieve all Comments of a Test Run  <strong>qTest Manager version:</strong> 7.5+

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
api_instance = swagger_client.TestrunApi()
project_id = 789 # int | ID of the project
id_or_key = 'id_or_key_example' # str | PID or ID of the Test Run

try: 
    # Gets all Comments of a Test Run
    api_response = api_instance.get_comments(project_id, id_or_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestrunApi->get_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **id_or_key** | **str**| PID or ID of the Test Run | 

### Return type

[**PagedResourceCommentResource**](PagedResourceCommentResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_of**
> TestRunListResource get_of(project_id, parent_id=parent_id, parent_type=parent_type, expand=expand, page=page, page_size=page_size)

Gets multiple Test Runs

To retrieve all Test Runs under root or under a container (Release, Test Cycle or Test Suite)  <strong>qTest Manager version:</strong> 6+

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
api_instance = swagger_client.TestrunApi()
project_id = 789 # int | ID of the project
parent_id = 789 # int | ID of the container (Release, Test Cycle or Test Suite)  Input 0 (zero) to retrieve Test Runs directly under root (optional)
parent_type = 'parent_type_example' # str | Type of the container. Valid values include <em>root</em>, <em>release</em>, <em>test-cycle</em> and <em>test-suite</em> (optional)
expand = 'expand_example' # str | Specify <em>expand=descendants</em> to include all Test Runs which are directly or indirectly under the container (optional)
page = 1 # int | By default the first page is returned but you can specify any page number to retrieve objects (optional) (default to 1)
page_size = 100 # int | The result is paginated. By the default, the number of objects in each page is 100 if this is omitted. You can specify your custom number (up to 999) in this parameter (optional) (default to 100)

try: 
    # Gets multiple Test Runs
    api_response = api_instance.get_of(project_id, parent_id=parent_id, parent_type=parent_type, expand=expand, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestrunApi->get_of: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **parent_id** | **int**| ID of the container (Release, Test Cycle or Test Suite)  Input 0 (zero) to retrieve Test Runs directly under root | [optional] 
 **parent_type** | **str**| Type of the container. Valid values include &lt;em&gt;root&lt;/em&gt;, &lt;em&gt;release&lt;/em&gt;, &lt;em&gt;test-cycle&lt;/em&gt; and &lt;em&gt;test-suite&lt;/em&gt; | [optional] 
 **expand** | **str**| Specify &lt;em&gt;expand&#x3D;descendants&lt;/em&gt; to include all Test Runs which are directly or indirectly under the container | [optional] 
 **page** | **int**| By default the first page is returned but you can specify any page number to retrieve objects | [optional] [default to 1]
 **page_size** | **int**| The result is paginated. By the default, the number of objects in each page is 100 if this is omitted. You can specify your custom number (up to 999) in this parameter | [optional] [default to 100]

### Return type

[**TestRunListResource**](TestRunListResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status_valuable**
> list[StatusResource] get_status_valuable(project_id)

Gets Test Run statuses

Gets Test Run statuses

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
api_instance = swagger_client.TestrunApi()
project_id = 789 # int | ID of the project

try: 
    # Gets Test Run statuses
    api_response = api_instance.get_status_valuable(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestrunApi->get_status_valuable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 

### Return type

[**list[StatusResource]**](StatusResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> TestRunWithCustomFieldResource update(project_id, test_run_id, body, parent_id=parent_id, parent_type=parent_type)

Updates a Test Run

To update a Test Run or move it to another container  <strong>qTest Manager version:</strong> 6+

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
api_instance = swagger_client.TestrunApi()
project_id = 789 # int | ID of the project
test_run_id = 789 # int | ID of the Test Run.
body = swagger_client.TestRunWithCustomFieldResource() # TestRunWithCustomFieldResource | The Test Run's updated properties
parent_id = 789 # int | ID of the container (Release, Test Cycle or Test Suite)  Input 0 (zero) to move the test run to under root  <strong>Important:</strong> If you use the request parameters, the request body will be ignored. That means the test run is being moved but it will not be updated with the properties specify in the request body (optional)
parent_type = 'parent_type_example' # str | Type of the container. Valid values include <em>root</em>, <em>release</em>, <em>test-cycle</em> and <em>test-suite</em> (optional)

try: 
    # Updates a Test Run
    api_response = api_instance.update(project_id, test_run_id, body, parent_id=parent_id, parent_type=parent_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestrunApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **test_run_id** | **int**| ID of the Test Run. | 
 **body** | [**TestRunWithCustomFieldResource**](TestRunWithCustomFieldResource.md)| The Test Run&#39;s updated properties | 
 **parent_id** | **int**| ID of the container (Release, Test Cycle or Test Suite)  Input 0 (zero) to move the test run to under root  &lt;strong&gt;Important:&lt;/strong&gt; If you use the request parameters, the request body will be ignored. That means the test run is being moved but it will not be updated with the properties specify in the request body | [optional] 
 **parent_type** | **str**| Type of the container. Valid values include &lt;em&gt;root&lt;/em&gt;, &lt;em&gt;release&lt;/em&gt;, &lt;em&gt;test-cycle&lt;/em&gt; and &lt;em&gt;test-suite&lt;/em&gt; | [optional] 

### Return type

[**TestRunWithCustomFieldResource**](TestRunWithCustomFieldResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_comment**
> CommentResource update_comment(project_id, id_or_key, comment_id, body)

Updates a Comment of a Test Run

To update a Comment of a Test Run  <strong>qTest Manager version:</strong> 7.5+

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
api_instance = swagger_client.TestrunApi()
project_id = 789 # int | ID of the project
id_or_key = 'id_or_key_example' # str | PID or ID of the Test Run
comment_id = 789 # int | ID of the comment which you want to update.
body = swagger_client.CommentResource() # CommentResource | The Comment's updated content

try: 
    # Updates a Comment of a Test Run
    api_response = api_instance.update_comment(project_id, id_or_key, comment_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestrunApi->update_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **id_or_key** | **str**| PID or ID of the Test Run | 
 **comment_id** | **int**| ID of the comment which you want to update. | 
 **body** | [**CommentResource**](CommentResource.md)| The Comment&#39;s updated content | 

### Return type

[**CommentResource**](CommentResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

