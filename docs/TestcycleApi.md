# swagger_client.TestcycleApi

All URIs are relative to *https://apitryout.qtestnet.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cycle**](TestcycleApi.md#create_cycle) | **POST** /api/v3/projects/{projectId}/test-cycles | Create a Test Cycle
[**delete_cycle**](TestcycleApi.md#delete_cycle) | **DELETE** /api/v3/projects/{projectId}/test-cycles/{testCycleId} | Deletes a Test Cycle
[**get_test_cycle**](TestcycleApi.md#get_test_cycle) | **GET** /api/v3/projects/{projectId}/test-cycles/{testCycleId} | Gets a Test Cycle
[**get_test_cycles**](TestcycleApi.md#get_test_cycles) | **GET** /api/v3/projects/{projectId}/test-cycles | Gets multiple Test Cycles
[**update_cycle**](TestcycleApi.md#update_cycle) | **PUT** /api/v3/projects/{projectId}/test-cycles/{testCycleId} | Updates a Test Cycle


# **create_cycle**
> TestCycleResource create_cycle(project_id, body, parent_id=parent_id, parent_type=parent_type)

Create a Test Cycle

To create a Test Cycle  <strong>qTest Manager version:</strong> 6+

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
api_instance = swagger_client.TestcycleApi()
project_id = 789 # int | ID of the project
body = swagger_client.TestCycleResource() # TestCycleResource | Given resource to create a test cycle.
parent_id = 789 # int | ID of the Release or Test Cycle under which the newly created Test Cycle will be located.   Use 0 (zero) to create the Test Cycle under the root (optional)
parent_type = 'parent_type_example' # str | The artifact type of the parent folder. Valid values include <em>release</em>, <em>test-cycle</em> or <em>root</em> (optional)

try: 
    # Create a Test Cycle
    api_response = api_instance.create_cycle(project_id, body, parent_id=parent_id, parent_type=parent_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestcycleApi->create_cycle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **body** | [**TestCycleResource**](TestCycleResource.md)| Given resource to create a test cycle. | 
 **parent_id** | **int**| ID of the Release or Test Cycle under which the newly created Test Cycle will be located.   Use 0 (zero) to create the Test Cycle under the root | [optional] 
 **parent_type** | **str**| The artifact type of the parent folder. Valid values include &lt;em&gt;release&lt;/em&gt;, &lt;em&gt;test-cycle&lt;/em&gt; or &lt;em&gt;root&lt;/em&gt; | [optional] 

### Return type

[**TestCycleResource**](TestCycleResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cycle**
> Message delete_cycle(project_id, test_cycle_id, force=force)

Deletes a Test Cycle

To delete a Test Cycle  <strong>qTest Manager version:</strong> 6+

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
api_instance = swagger_client.TestcycleApi()
project_id = 789 # int | ID of the project
test_cycle_id = 789 # int | ID of the Test Cycle which needs to be deleted.
force = true # bool | The Test Cycle can only be deleted if it contains no children. Specify <em>force=true</em> to delete the Test Cycle and its children (optional)

try: 
    # Deletes a Test Cycle
    api_response = api_instance.delete_cycle(project_id, test_cycle_id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestcycleApi->delete_cycle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **test_cycle_id** | **int**| ID of the Test Cycle which needs to be deleted. | 
 **force** | **bool**| The Test Cycle can only be deleted if it contains no children. Specify &lt;em&gt;force&#x3D;true&lt;/em&gt; to delete the Test Cycle and its children | [optional] 

### Return type

[**Message**](Message.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_cycle**
> TestCycleResource get_test_cycle(project_id, test_cycle_id, expand=expand)

Gets a Test Cycle

To retrieve a Test Cycle  <strong>qTest Manager version:</strong> 6+

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
api_instance = swagger_client.TestcycleApi()
project_id = 789 # int | ID of the project
test_cycle_id = 789 # int | ID of the Test Cycle which you want to retrieve.
expand = 'expand_example' # str | Specify <em>expand=descendants</em> to include its sub and grand-sub Test Cycles and Test Suites in the response (optional)

try: 
    # Gets a Test Cycle
    api_response = api_instance.get_test_cycle(project_id, test_cycle_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestcycleApi->get_test_cycle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **test_cycle_id** | **int**| ID of the Test Cycle which you want to retrieve. | 
 **expand** | **str**| Specify &lt;em&gt;expand&#x3D;descendants&lt;/em&gt; to include its sub and grand-sub Test Cycles and Test Suites in the response | [optional] 

### Return type

[**TestCycleResource**](TestCycleResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_cycles**
> list[TestCycleResource] get_test_cycles(project_id, parent_id=parent_id, parent_type=parent_type, expand=expand)

Gets multiple Test Cycles

To retrieve Test Cycles which are located directly under root or a Release/Test Cycle

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
api_instance = swagger_client.TestcycleApi()
project_id = 789 # int | ID of the project
parent_id = 789 # int | ID of the Release or Test Cycle which directly contains the Test Cycles you are retrieving. Input 0 (zero) to get Test Cycles directly under root (optional)
parent_type = 'parent_type_example' # str | The artifact type of the parent folder. Valid values include <em>release</em>, <em>test-cycle</em> or <em>root</em> (optional)
expand = 'expand_example' # str | Specify <em>expand=descendants</em> to retrieve the Test Cycles' sub and grand-sub Cycles/Suites (optional)

try: 
    # Gets multiple Test Cycles
    api_response = api_instance.get_test_cycles(project_id, parent_id=parent_id, parent_type=parent_type, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestcycleApi->get_test_cycles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **parent_id** | **int**| ID of the Release or Test Cycle which directly contains the Test Cycles you are retrieving. Input 0 (zero) to get Test Cycles directly under root | [optional] 
 **parent_type** | **str**| The artifact type of the parent folder. Valid values include &lt;em&gt;release&lt;/em&gt;, &lt;em&gt;test-cycle&lt;/em&gt; or &lt;em&gt;root&lt;/em&gt; | [optional] 
 **expand** | **str**| Specify &lt;em&gt;expand&#x3D;descendants&lt;/em&gt; to retrieve the Test Cycles&#39; sub and grand-sub Cycles/Suites | [optional] 

### Return type

[**list[TestCycleResource]**](TestCycleResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cycle**
> TestCycleResource update_cycle(project_id, test_cycle_id, body, parent_id=parent_id, parent_type=parent_type)

Updates a Test Cycle

To update a Test Cycle or move it to another container  <strong>qTest Manager version:</strong> 6+

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
api_instance = swagger_client.TestcycleApi()
project_id = 789 # int | ID of the project
test_cycle_id = 789 # int | ID of the Test Cycle which needs to be updated.
body = swagger_client.TestCycleResource() # TestCycleResource | The Test Cycle's updated properties
parent_id = 789 # int | ID of a Release or parent Test Cycle which the updated Test Cycle will be moved to. Input 0 (zero) to move the Test Cycle to under root (optional)
parent_type = 'parent_type_example' # str | The artifact type of the parent folder to which the Test Cycle will be moved to. Valid values include <em>release</em>, <em>test-cycle</em> or <em>root</em> (optional)

try: 
    # Updates a Test Cycle
    api_response = api_instance.update_cycle(project_id, test_cycle_id, body, parent_id=parent_id, parent_type=parent_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestcycleApi->update_cycle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **test_cycle_id** | **int**| ID of the Test Cycle which needs to be updated. | 
 **body** | [**TestCycleResource**](TestCycleResource.md)| The Test Cycle&#39;s updated properties | 
 **parent_id** | **int**| ID of a Release or parent Test Cycle which the updated Test Cycle will be moved to. Input 0 (zero) to move the Test Cycle to under root | [optional] 
 **parent_type** | **str**| The artifact type of the parent folder to which the Test Cycle will be moved to. Valid values include &lt;em&gt;release&lt;/em&gt;, &lt;em&gt;test-cycle&lt;/em&gt; or &lt;em&gt;root&lt;/em&gt; | [optional] 

### Return type

[**TestCycleResource**](TestCycleResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

