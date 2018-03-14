# swagger_client.ModuleApi

All URIs are relative to *https://apitryout.qtestnet.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_module**](ModuleApi.md#create_module) | **POST** /api/v3/projects/{projectId}/modules | Creates a Module
[**delete_module**](ModuleApi.md#delete_module) | **DELETE** /api/v3/projects/{projectId}/modules/{moduleId} | Deletes a Module
[**get_module**](ModuleApi.md#get_module) | **GET** /api/v3/projects/{projectId}/modules/{moduleId} | Gets a Module
[**get_sub_modules_of**](ModuleApi.md#get_sub_modules_of) | **GET** /api/v3/projects/{projectId}/modules | Gets multiple Modules
[**update_module**](ModuleApi.md#update_module) | **PUT** /api/v3/projects/{projectId}/modules/{moduleId} | Updates a Module


# **create_module**
> ModuleResource create_module(project_id, body, parent_id=parent_id)

Creates a Module

To create a Module under root or a sub-Module under a parent Module  <strong>qTest Manager version:</strong> 4+

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
api_instance = swagger_client.ModuleApi()
project_id = 789 # int | ID of the project
body = swagger_client.ModuleResource() # ModuleResource | <em>name (required):</em> the Module name  <em>shared:</em> Specify <em>shared=true</em> to share this Module to other projects. Only use it if Test Case Sharing feature is enabled in your project
parent_id = 789 # int | The parent Module which will contain the newly created one. If it is not specified, the newly created module is located under root  Use this parameter if your qTest Manager version is 6+. For older versions, use <em>parent_id</em> in the request body (optional)

try: 
    # Creates a Module
    api_response = api_instance.create_module(project_id, body, parent_id=parent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModuleApi->create_module: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **body** | [**ModuleResource**](ModuleResource.md)| &lt;em&gt;name (required):&lt;/em&gt; the Module name  &lt;em&gt;shared:&lt;/em&gt; Specify &lt;em&gt;shared&#x3D;true&lt;/em&gt; to share this Module to other projects. Only use it if Test Case Sharing feature is enabled in your project | 
 **parent_id** | **int**| The parent Module which will contain the newly created one. If it is not specified, the newly created module is located under root  Use this parameter if your qTest Manager version is 6+. For older versions, use &lt;em&gt;parent_id&lt;/em&gt; in the request body | [optional] 

### Return type

[**ModuleResource**](ModuleResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_module**
> Message delete_module(project_id, module_id, force=force)

Deletes a Module

To delete a Module  <strong>qTest Manager version:</strong> 6+

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
api_instance = swagger_client.ModuleApi()
project_id = 789 # int | ID of the project
module_id = 789 # int | ID of Module to delete
force = true # bool | <em>force=true</em> - delete the Module and its children  force=false - default value. Only delete the Module if it contains no sub Modules or Test Cases (optional)

try: 
    # Deletes a Module
    api_response = api_instance.delete_module(project_id, module_id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModuleApi->delete_module: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **module_id** | **int**| ID of Module to delete | 
 **force** | **bool**| &lt;em&gt;force&#x3D;true&lt;/em&gt; - delete the Module and its children  force&#x3D;false - default value. Only delete the Module if it contains no sub Modules or Test Cases | [optional] 

### Return type

[**Message**](Message.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_module**
> ModuleResource get_module(project_id, module_id, expand=expand)

Gets a Module

To retrieve a Module  <em>qTest Manager version:</em> 6+

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
api_instance = swagger_client.ModuleApi()
project_id = 789 # int | ID of the project
module_id = 789 # int | ID of the Module
expand = 'expand_example' # str | Specify <em>expand=descendants</em> to include the Module's sub and grand-sub Modules in the response (optional)

try: 
    # Gets a Module
    api_response = api_instance.get_module(project_id, module_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModuleApi->get_module: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **module_id** | **int**| ID of the Module | 
 **expand** | **str**| Specify &lt;em&gt;expand&#x3D;descendants&lt;/em&gt; to include the Module&#39;s sub and grand-sub Modules in the response | [optional] 

### Return type

[**ModuleResource**](ModuleResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sub_modules_of**
> list[ModuleResource] get_sub_modules_of(project_id, parent_id=parent_id, search=search, expand=expand)

Gets multiple Modules

To search for Modules under root or sub-Modules under a parent Module  <strong>qTest Manager version:</strong> 6+

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
api_instance = swagger_client.ModuleApi()
project_id = 789 # int | ID of the project
parent_id = 789 # int | ID of the parent Module. Leave it blank to retrieve Modules under root (optional)
search = 'search_example' # str | The free-text to search for Modules by names. You can utilize this parameter to search for Modules. Leave it blank to retrieve all Modules under root or the parent Module (optional)
expand = 'expand_example' # str |  (optional)

try: 
    # Gets multiple Modules
    api_response = api_instance.get_sub_modules_of(project_id, parent_id=parent_id, search=search, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModuleApi->get_sub_modules_of: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **parent_id** | **int**| ID of the parent Module. Leave it blank to retrieve Modules under root | [optional] 
 **search** | **str**| The free-text to search for Modules by names. You can utilize this parameter to search for Modules. Leave it blank to retrieve all Modules under root or the parent Module | [optional] 
 **expand** | **str**|  | [optional] 

### Return type

[**list[ModuleResource]**](ModuleResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_module**
> ModuleResource update_module(project_id, module_id, body, parent_id=parent_id)

Updates a Module

To update a Module or move it to another parent Module

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
api_instance = swagger_client.ModuleApi()
project_id = 789 # int | ID of the project
module_id = 789 # int | ID of the Module
body = swagger_client.ModuleResource() # ModuleResource | The Module's update properties
parent_id = 789 # int | ID of the parent Module which the Module will be moved to  <strong>Important:</strong> If you use this parameter, the request body will be ignored. That means the Module is being moved but it will not be updated with the properties specified in the request body (optional)

try: 
    # Updates a Module
    api_response = api_instance.update_module(project_id, module_id, body, parent_id=parent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModuleApi->update_module: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **module_id** | **int**| ID of the Module | 
 **body** | [**ModuleResource**](ModuleResource.md)| The Module&#39;s update properties | 
 **parent_id** | **int**| ID of the parent Module which the Module will be moved to  &lt;strong&gt;Important:&lt;/strong&gt; If you use this parameter, the request body will be ignored. That means the Module is being moved but it will not be updated with the properties specified in the request body | [optional] 

### Return type

[**ModuleResource**](ModuleResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

