# swagger_client.ProjectApi

All URIs are relative to *https://apitryout.qtestnet.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project**](ProjectApi.md#create_project) | **POST** /api/v3/projects | Creates a Project
[**get_current_profile**](ProjectApi.md#get_current_profile) | **GET** /api/v3/projects/{projectId}/user-profiles/current | Gets current user Permissions in a Project
[**get_project**](ProjectApi.md#get_project) | **GET** /api/v3/projects/{projectId} | Gets a Project
[**get_projects**](ProjectApi.md#get_projects) | **GET** /api/v3/projects | Gets multiple Projects
[**get_users**](ProjectApi.md#get_users) | **GET** /api/v3/projects/{projectId}/users | Gets all Users in a Project


# **create_project**
> object create_project(body)

Creates a Project

To create a new Project  <strong>qTest Manager version:</strong> 4+

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
api_instance = swagger_client.ProjectApi()
body = swagger_client.ProjectResource() # ProjectResource | 

try: 
    # Creates a Project
    api_response = api_instance.create_project(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectResource**](ProjectResource.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_profile**
> UserProfile get_current_profile(project_id)

Gets current user Permissions in a Project

To retrieve your Permissions in a Project  <strong>qTest Manager version:</strong> 4+

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
api_instance = swagger_client.ProjectApi()
project_id = 789 # int | ID of the project

try: 
    # Gets current user Permissions in a Project
    api_response = api_instance.get_current_profile(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_current_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 

### Return type

[**UserProfile**](UserProfile.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> ProjectResource get_project(project_id, expand=expand)

Gets a Project

To retrieve a specific Project

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
api_instance = swagger_client.ProjectApi()
project_id = 789 # int | ID of the project
expand = 'expand_example' # str | <em>expand=userprofile</em> - include the your profile and permissions within the project in the response (optional)

try: 
    # Gets a Project
    api_response = api_instance.get_project(project_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **expand** | **str**| &lt;em&gt;expand&#x3D;userprofile&lt;/em&gt; - include the your profile and permissions within the project in the response | [optional] 

### Return type

[**ProjectResource**](ProjectResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects**
> list[ProjectResource] get_projects(expand=expand, assigned=assigned)

Gets multiple Projects

To retrieve all Projects which the requested qTest  Manager account can access to  <strong>qTest Manager version:</strong> 4+

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
api_instance = swagger_client.ProjectApi()
expand = 'expand_example' # str | <em>expand=userprofile</em> - to include your profile and permissions in each project (optional)
assigned = true # bool | <em>assigned=true</em> - default value. Only the projects which the requested user has access to  <em>assigned=false</em> - Users with admin profile can use this value to retrieve all projects, regardless of having access (optional)

try: 
    # Gets multiple Projects
    api_response = api_instance.get_projects(expand=expand, assigned=assigned)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **str**| &lt;em&gt;expand&#x3D;userprofile&lt;/em&gt; - to include your profile and permissions in each project | [optional] 
 **assigned** | **bool**| &lt;em&gt;assigned&#x3D;true&lt;/em&gt; - default value. Only the projects which the requested user has access to  &lt;em&gt;assigned&#x3D;false&lt;/em&gt; - Users with admin profile can use this value to retrieve all projects, regardless of having access | [optional] 

### Return type

[**list[ProjectResource]**](ProjectResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> list[UserResource] get_users(project_id, inactive=inactive)

Gets all Users in a Project

To retrieve all members in a qTest Manager Project  <strong>qTest Manager version:</strong> 8.4.2+

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
api_instance = swagger_client.ProjectApi()
project_id = 789 # int | ID of the project
inactive = true # bool | <em>inactive=false</em> - default value. Inactive users are excluded from the response  <em>inactive=true</em> - inactive users are included in the response (optional)

try: 
    # Gets all Users in a Project
    api_response = api_instance.get_users(project_id, inactive=inactive)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **inactive** | **bool**| &lt;em&gt;inactive&#x3D;false&lt;/em&gt; - default value. Inactive users are excluded from the response  &lt;em&gt;inactive&#x3D;true&lt;/em&gt; - inactive users are included in the response | [optional] 

### Return type

[**list[UserResource]**](UserResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

