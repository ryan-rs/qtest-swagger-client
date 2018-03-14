# swagger_client.ReleaseApi

All URIs are relative to *https://apitryout.qtestnet.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ReleaseApi.md#create) | **POST** /api/v3/projects/{projectId}/releases | Creates a Release
[**delete**](ReleaseApi.md#delete) | **DELETE** /api/v3/projects/{projectId}/releases/{releaseId} | Delete a release
[**get**](ReleaseApi.md#get) | **GET** /api/v3/projects/{projectId}/releases/{releaseId} | Gets a Release
[**get_all**](ReleaseApi.md#get_all) | **GET** /api/v3/projects/{projectId}/releases | Gets multiple Releases
[**update**](ReleaseApi.md#update) | **PUT** /api/v3/projects/{projectId}/releases/{releaseId} | Updates a Release


# **create**
> ReleaseWithCustomFieldResource create(project_id, body)

Creates a Release

To create a Release  <strong>qTest Manager version:</strong> 4+

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
api_instance = swagger_client.ReleaseApi()
project_id = 789 # int | ID of the project
body = swagger_client.ReleaseWithCustomFieldResource() # ReleaseWithCustomFieldResource | The Release's properties

try: 
    # Creates a Release
    api_response = api_instance.create(project_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleaseApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **body** | [**ReleaseWithCustomFieldResource**](ReleaseWithCustomFieldResource.md)| The Release&#39;s properties | 

### Return type

[**ReleaseWithCustomFieldResource**](ReleaseWithCustomFieldResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> object delete(project_id, release_id)

Delete a release

To delete a Release

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
api_instance = swagger_client.ReleaseApi()
project_id = 789 # int | ID of the project
release_id = 789 # int | ID of the Release which needs to be deleted  <strong>qTest Manager version:</strong> 6+

try: 
    # Delete a release
    api_response = api_instance.delete(project_id, release_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleaseApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **release_id** | **int**| ID of the Release which needs to be deleted  &lt;strong&gt;qTest Manager version:&lt;/strong&gt; 6+ | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> ReleaseWithCustomFieldResource get(project_id, release_id)

Gets a Release

To retrieve a Release  <strong>qTest Manager version:</strong> 4+

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
api_instance = swagger_client.ReleaseApi()
project_id = 789 # int | ID of the project
release_id = 789 # int | ID of the Release

try: 
    # Gets a Release
    api_response = api_instance.get(project_id, release_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleaseApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **release_id** | **int**| ID of the Release | 

### Return type

[**ReleaseWithCustomFieldResource**](ReleaseWithCustomFieldResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all**
> list[ReleaseWithCustomFieldResource] get_all(project_id, include_closed=include_closed)

Gets multiple Releases

To retrieve Releases in a project  <strong>qTest Manager version:</strong> 4+

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
api_instance = swagger_client.ReleaseApi()
project_id = 789 # int | ID of the project
include_closed = true # bool | <em>includeClosed=false</em> - default value. <em>Closed</em> Releases are excluded from the response  <em>includeClosed=false</em> - Closed Release are included in the response (optional)

try: 
    # Gets multiple Releases
    api_response = api_instance.get_all(project_id, include_closed=include_closed)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleaseApi->get_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **include_closed** | **bool**| &lt;em&gt;includeClosed&#x3D;false&lt;/em&gt; - default value. &lt;em&gt;Closed&lt;/em&gt; Releases are excluded from the response  &lt;em&gt;includeClosed&#x3D;false&lt;/em&gt; - Closed Release are included in the response | [optional] 

### Return type

[**list[ReleaseWithCustomFieldResource]**](ReleaseWithCustomFieldResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> ReleaseWithCustomFieldResource update(project_id, release_id, body)

Updates a Release

To update a Release  <strong>qTest Manager version:</strong> 6+

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
api_instance = swagger_client.ReleaseApi()
project_id = 789 # int | ID of the project
release_id = 789 # int | ID of the Release which needs to be updated
body = swagger_client.ReleaseWithCustomFieldResource() # ReleaseWithCustomFieldResource | The Release's updated properties

try: 
    # Updates a Release
    api_response = api_instance.update(project_id, release_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReleaseApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **release_id** | **int**| ID of the Release which needs to be updated | 
 **body** | [**ReleaseWithCustomFieldResource**](ReleaseWithCustomFieldResource.md)| The Release&#39;s updated properties | 

### Return type

[**ReleaseWithCustomFieldResource**](ReleaseWithCustomFieldResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

