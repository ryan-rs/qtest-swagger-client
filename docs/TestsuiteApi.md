# swagger_client.TestsuiteApi

All URIs are relative to *https://apitryout.qtestnet.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_test_suite**](TestsuiteApi.md#create_test_suite) | **POST** /api/v3/projects/{projectId}/test-suites | Creates a Test Suite
[**delete**](TestsuiteApi.md#delete) | **DELETE** /api/v3/projects/{projectId}/test-suites/{testSuiteId} | Deletes a Test Suite
[**get**](TestsuiteApi.md#get) | **GET** /api/v3/projects/{projectId}/test-suites | Gets multiple Test Suite
[**get_test_suite**](TestsuiteApi.md#get_test_suite) | **GET** /api/v3/projects/{projectId}/test-suites/{testSuiteId} | Gets a Test Suite
[**update_test_suite**](TestsuiteApi.md#update_test_suite) | **PUT** /api/v3/projects/{projectId}/test-suites/{testSuiteId} | Updates a Test Suite


# **create_test_suite**
> TestSuiteWithCustomFieldResource create_test_suite(project_id, body, parent_id=parent_id, parent_type=parent_type)

Creates a Test Suite

To create a new Test Suite  <strong>qTest Manager version:</strong> 6+

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
api_instance = swagger_client.TestsuiteApi()
project_id = 789 # int | ID of the project
body = swagger_client.TestSuiteWithCustomFieldResource() # TestSuiteWithCustomFieldResource | The Test Suite's properties
parent_id = 789 # int | ID of the Release or Test Cycle under which the newly created Test Suites are located. Input 0 (zero) to create Test Suites directly under root (optional)
parent_type = 'parent_type_example' # str | Arifact type of the container. Valid values include <em>release</em>, <em>test-cycle</em> and <em>root</em> (optional)

try: 
    # Creates a Test Suite
    api_response = api_instance.create_test_suite(project_id, body, parent_id=parent_id, parent_type=parent_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestsuiteApi->create_test_suite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **body** | [**TestSuiteWithCustomFieldResource**](TestSuiteWithCustomFieldResource.md)| The Test Suite&#39;s properties | 
 **parent_id** | **int**| ID of the Release or Test Cycle under which the newly created Test Suites are located. Input 0 (zero) to create Test Suites directly under root | [optional] 
 **parent_type** | **str**| Arifact type of the container. Valid values include &lt;em&gt;release&lt;/em&gt;, &lt;em&gt;test-cycle&lt;/em&gt; and &lt;em&gt;root&lt;/em&gt; | [optional] 

### Return type

[**TestSuiteWithCustomFieldResource**](TestSuiteWithCustomFieldResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> object delete(project_id, test_suite_id)

Deletes a Test Suite

To delete a Test Suite  <strong>qTest Manager version:</strong> 6+

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
api_instance = swagger_client.TestsuiteApi()
project_id = 789 # int | ID of the project
test_suite_id = 789 # int | ID of the Test Suite.

try: 
    # Deletes a Test Suite
    api_response = api_instance.delete(project_id, test_suite_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestsuiteApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **test_suite_id** | **int**| ID of the Test Suite. | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> list[TestSuiteWithCustomFieldResource] get(project_id, parent_id=parent_id, parent_type=parent_type)

Gets multiple Test Suite

To retrieve Test Suites which located under a parent Release, Test Cycle or root  <strong>qTest Manager version:</strong> 6+

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
api_instance = swagger_client.TestsuiteApi()
project_id = 789 # int | ID of the project
parent_id = 789 # int | ID of the Release or Test Cycle under which the Test Suites are located. Input 0 (zero) to get Test Suites directly under root (optional)
parent_type = 'parent_type_example' # str | Arifact type of the container. Valid values include <em>release</em>, <em>test-cycle</em> and <em>root</em> (optional)

try: 
    # Gets multiple Test Suite
    api_response = api_instance.get(project_id, parent_id=parent_id, parent_type=parent_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestsuiteApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **parent_id** | **int**| ID of the Release or Test Cycle under which the Test Suites are located. Input 0 (zero) to get Test Suites directly under root | [optional] 
 **parent_type** | **str**| Arifact type of the container. Valid values include &lt;em&gt;release&lt;/em&gt;, &lt;em&gt;test-cycle&lt;/em&gt; and &lt;em&gt;root&lt;/em&gt; | [optional] 

### Return type

[**list[TestSuiteWithCustomFieldResource]**](TestSuiteWithCustomFieldResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_suite**
> TestSuiteWithCustomFieldResource get_test_suite(project_id, test_suite_id)

Gets a Test Suite

To retrieve a Test Suite  <strong>qTest Manager version:</strong> 6+

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
api_instance = swagger_client.TestsuiteApi()
project_id = 789 # int | ID of the project
test_suite_id = 789 # int | ID of the Test Suite

try: 
    # Gets a Test Suite
    api_response = api_instance.get_test_suite(project_id, test_suite_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestsuiteApi->get_test_suite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **test_suite_id** | **int**| ID of the Test Suite | 

### Return type

[**TestSuiteWithCustomFieldResource**](TestSuiteWithCustomFieldResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_test_suite**
> TestSuiteWithCustomFieldResource update_test_suite(project_id, test_suite_id, body, parent_id=parent_id, parent_type=parent_type, no_email=no_email)

Updates a Test Suite

To update an existing Test Suite or to move it to other container  <strong>Important:</strong> If you use the request parameters <em>parentId</em> and <em>parentType</em>, the request body will be ignore.   That means the Test Suite is being moved but it will not be updated with the properties specify in the request body

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
api_instance = swagger_client.TestsuiteApi()
project_id = 789 # int | ID of the project
test_suite_id = 789 # int | ID of the Test Suite
body = swagger_client.TestSuiteWithCustomFieldResource() # TestSuiteWithCustomFieldResource | The Test Suite's updated properties
parent_id = 789 # int | ID of the Release or Test Cycle which the Test Suite will be moved to. Input 0 (zero) to move the Test Suite to under root (optional)
parent_type = 'parent_type_example' # str | Artifact type of the parent container. Valid values include <em>release</em>, <em>test-cycle</em> and <em>root</em> (optional)
no_email = true # bool |  (optional)

try: 
    # Updates a Test Suite
    api_response = api_instance.update_test_suite(project_id, test_suite_id, body, parent_id=parent_id, parent_type=parent_type, no_email=no_email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestsuiteApi->update_test_suite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **test_suite_id** | **int**| ID of the Test Suite | 
 **body** | [**TestSuiteWithCustomFieldResource**](TestSuiteWithCustomFieldResource.md)| The Test Suite&#39;s updated properties | 
 **parent_id** | **int**| ID of the Release or Test Cycle which the Test Suite will be moved to. Input 0 (zero) to move the Test Suite to under root | [optional] 
 **parent_type** | **str**| Artifact type of the parent container. Valid values include &lt;em&gt;release&lt;/em&gt;, &lt;em&gt;test-cycle&lt;/em&gt; and &lt;em&gt;root&lt;/em&gt; | [optional] 
 **no_email** | **bool**|  | [optional] 

### Return type

[**TestSuiteWithCustomFieldResource**](TestSuiteWithCustomFieldResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

