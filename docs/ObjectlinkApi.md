# swagger_client.ObjectlinkApi

All URIs are relative to *https://apitryout.qtestnet.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find**](ObjectlinkApi.md#find) | **GET** /api/v3/projects/{projectId}/linked-artifacts | Gets associated objects of given objects
[**link_artifacts**](ObjectlinkApi.md#link_artifacts) | **POST** /api/v3/projects/{projectId}/{objectType}/{objectId}/link | Creates links between objects
[**unlink_artifacts**](ObjectlinkApi.md#unlink_artifacts) | **DELETE** /api/v3/projects/{projectId}/{objectType}/{objectId}/link | Removes links between objects


# **find**
> list[LinkedArtifactContainer] find(project_id, type, ids=ids, pids=pids)

Gets associated objects of given objects

To retrieve associated objects of given objects  <strong>qTest Manager version:</strong> 7.5+

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
api_instance = swagger_client.ObjectlinkApi()
project_id = 789 # int | ID of the project
type = 'type_example' # str | Valid values include <em>releases</em>, <em>builds</em>, <em>requirements</em>,<em>test-cases</em>, <em>test-runs</em>, <em>test-logs</em>, <em>test-steps</em> or <em>defects</em>
ids = [56] # list[int] | IDs of objects whose links you want to retrieve (optional)
pids = ['pids_example'] # list[str] | In case of <em>type=defects</em>, you can specify a list of external defect id in this parameters.  It cannot be used for other types (optional)

try: 
    # Gets associated objects of given objects
    api_response = api_instance.find(project_id, type, ids=ids, pids=pids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectlinkApi->find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **type** | **str**| Valid values include &lt;em&gt;releases&lt;/em&gt;, &lt;em&gt;builds&lt;/em&gt;, &lt;em&gt;requirements&lt;/em&gt;,&lt;em&gt;test-cases&lt;/em&gt;, &lt;em&gt;test-runs&lt;/em&gt;, &lt;em&gt;test-logs&lt;/em&gt;, &lt;em&gt;test-steps&lt;/em&gt; or &lt;em&gt;defects&lt;/em&gt; | 
 **ids** | [**list[int]**](int.md)| IDs of objects whose links you want to retrieve | [optional] 
 **pids** | [**list[str]**](str.md)| In case of &lt;em&gt;type&#x3D;defects&lt;/em&gt;, you can specify a list of external defect id in this parameters.  It cannot be used for other types | [optional] 

### Return type

[**list[LinkedArtifactContainer]**](LinkedArtifactContainer.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_artifacts**
> list[LinkedArtifactContainer] link_artifacts(project_id, object_type, type, body, object_id)

Creates links between objects

To add associated objects to another object

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
api_instance = swagger_client.ObjectlinkApi()
project_id = 789 # int | ID of the project
object_type = 'object_type_example' # str | the object type of the source object. Valid values include requirements, builds, test-steps, test-logs, releases
type = 'type_example' # str | The object type of the associated objects which are being added to the source object.   Valid values include releases, builds, requirements, test-cases, test-runs, test-logs, test-steps or defects
body = [swagger_client.list[int]()] # list[int] | A JSONArray of associated object IDs which are being added to the source object
object_id = 789 # int | ID of the source object

try: 
    # Creates links between objects
    api_response = api_instance.link_artifacts(project_id, object_type, type, body, object_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectlinkApi->link_artifacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **object_type** | **str**| the object type of the source object. Valid values include requirements, builds, test-steps, test-logs, releases | 
 **type** | **str**| The object type of the associated objects which are being added to the source object.   Valid values include releases, builds, requirements, test-cases, test-runs, test-logs, test-steps or defects | 
 **body** | **list[int]**| A JSONArray of associated object IDs which are being added to the source object | 
 **object_id** | **int**| ID of the source object | 

### Return type

[**list[LinkedArtifactContainer]**](LinkedArtifactContainer.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlink_artifacts**
> object unlink_artifacts(project_id, object_type, type, body, object_id)

Removes links between objects

To remove associated objects from another object

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
api_instance = swagger_client.ObjectlinkApi()
project_id = 789 # int | ID of the project
object_type = 'object_type_example' # str | The object type of the source object. Valid values include requirements, builds, test-steps, test-logs, releases
type = 'type_example' # str | The object type of the associated objects which are being added to the source object.   Valid values include releases, builds, requirements, test-cases, test-runs, test-logs, test-steps or defects
body = [swagger_client.list[int]()] # list[int] | A JSONArray of associated object IDs which are being removed from the source object
object_id = 789 # int | ID of the source object

try: 
    # Removes links between objects
    api_response = api_instance.unlink_artifacts(project_id, object_type, type, body, object_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectlinkApi->unlink_artifacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **object_type** | **str**| The object type of the source object. Valid values include requirements, builds, test-steps, test-logs, releases | 
 **type** | **str**| The object type of the associated objects which are being added to the source object.   Valid values include releases, builds, requirements, test-cases, test-runs, test-logs, test-steps or defects | 
 **body** | **list[int]**| A JSONArray of associated object IDs which are being removed from the source object | 
 **object_id** | **int**| ID of the source object | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

