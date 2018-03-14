# swagger_client.BuildApi

All URIs are relative to *https://apitryout.qtestnet.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](BuildApi.md#create) | **POST** /api/v3/projects/{projectId}/builds | Creates a Build
[**delete**](BuildApi.md#delete) | **DELETE** /api/v3/projects/{projectId}/builds/{buildId} | Deletes a Build
[**get**](BuildApi.md#get) | **GET** /api/v3/projects/{projectId}/builds/{buildId} | Gets a Build
[**get_builds**](BuildApi.md#get_builds) | **GET** /api/v3/projects/{projectId}/builds | Gets multiple Builds
[**update**](BuildApi.md#update) | **PUT** /api/v3/projects/{projectId}/builds/{buildId} | Updates a Build


# **create**
> BuildResource create(project_id, body)

Creates a Build

To create a Build under a parent Release  <strong>qTest Manager version:</strong> 4+

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
api_instance = swagger_client.BuildApi()
project_id = 789 # int | ID of the project
body = swagger_client.BuildResource() # BuildResource | <em>name (required):</em> Build name  <em>release (required):</em> The parent Release under which the Build will be located  <em>properties:</em> An array of field-value pairs

try: 
    # Creates a Build
    api_response = api_instance.create(project_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **body** | [**BuildResource**](BuildResource.md)| &lt;em&gt;name (required):&lt;/em&gt; Build name  &lt;em&gt;release (required):&lt;/em&gt; The parent Release under which the Build will be located  &lt;em&gt;properties:&lt;/em&gt; An array of field-value pairs | 

### Return type

[**BuildResource**](BuildResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> object delete(project_id, build_id)

Deletes a Build

To delete a Build  <strong>qTest Manager version:</strong> 6+

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
api_instance = swagger_client.BuildApi()
project_id = 789 # int | ID of the project
build_id = 789 # int | ID of the Build to delete

try: 
    # Deletes a Build
    api_response = api_instance.delete(project_id, build_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **build_id** | **int**| ID of the Build to delete | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> BuildResource get(project_id, build_id)

Gets a Build

To retrieve a Build<strong>qTest Manager version:</strong> 6+

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
api_instance = swagger_client.BuildApi()
project_id = 789 # int | ID of the project
build_id = 789 # int | ID of the Build

try: 
    # Gets a Build
    api_response = api_instance.get(project_id, build_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **build_id** | **int**| ID of the Build | 

### Return type

[**BuildResource**](BuildResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_builds**
> list[BuildResource] get_builds(project_id, release_id)

Gets multiple Builds

To retrieve all Builds under a Release  <strong>qTest Manager version:</strong> 6+

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
api_instance = swagger_client.BuildApi()
project_id = 789 # int | ID of the project
release_id = 789 # int | ID of the parent Release

try: 
    # Gets multiple Builds
    api_response = api_instance.get_builds(project_id, release_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildApi->get_builds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **release_id** | **int**| ID of the parent Release | 

### Return type

[**list[BuildResource]**](BuildResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> BuildResource update(project_id, build_id, body)

Updates a Build

To update a Build  <strong>qTest Manager version:</strong> 6+

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
api_instance = swagger_client.BuildApi()
project_id = 789 # int | ID of the project
build_id = 789 # int | ID of the Build
body = swagger_client.BuildResource() # BuildResource | The Build's updated properties

try: 
    # Updates a Build
    api_response = api_instance.update(project_id, build_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **build_id** | **int**| ID of the Build | 
 **body** | [**BuildResource**](BuildResource.md)| The Build&#39;s updated properties | 

### Return type

[**BuildResource**](BuildResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

