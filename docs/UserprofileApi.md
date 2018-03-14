# swagger_client.UserprofileApi

All URIs are relative to *https://apitryout.qtestnet.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_assign_user_profile_in_client**](UserprofileApi.md#batch_assign_user_profile_in_client) | **POST** /api/v3/user-profiles/batch-assign-users | Assigns multiple Users to a Profile
[**batch_assign_user_profile_in_project**](UserprofileApi.md#batch_assign_user_profile_in_project) | **POST** /api/v3/user-profiles/{projectId}/batch-assign-users | Assigns multiple Users to a Profile in a Project
[**get_current**](UserprofileApi.md#get_current) | **GET** /api/v3/admin-profiles/current | Gets current User&#39;s Admin Profile
[**get_profiles_of_current_user**](UserprofileApi.md#get_profiles_of_current_user) | **GET** /api/v3/user-profiles/current | Gets current User&#39;s Profiles in different Projects
[**get_user_profiles**](UserprofileApi.md#get_user_profiles) | **GET** /api/v3/user-profiles | Gets available Profiles


# **batch_assign_user_profile_in_client**
> list[UserResourceExtension] batch_assign_user_profile_in_client(body)

Assigns multiple Users to a Profile

To batch assign users to a profile (as in qTest Manager <em>admin panel</em>). It requires that your qTest Manager profile is a site admin with <em>Manage Client Users</em> permissions  <strong>qTest Manager version:</strong> 8.4.2+

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
api_instance = swagger_client.UserprofileApi()
body = swagger_client.AssignedUsersProfile() # AssignedUsersProfile | An array of user IDs and admin and/or normal user profile

try: 
    # Assigns multiple Users to a Profile
    api_response = api_instance.batch_assign_user_profile_in_client(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserprofileApi->batch_assign_user_profile_in_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssignedUsersProfile**](AssignedUsersProfile.md)| An array of user IDs and admin and/or normal user profile | 

### Return type

[**list[UserResourceExtension]**](UserResourceExtension.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_assign_user_profile_in_project**
> list[UserResourceExtension] batch_assign_user_profile_in_project(project_id, body)

Assigns multiple Users to a Profile in a Project

To batch assign users to a profile (as a project's User Management page). It requires that your qTest Manager profile within the project is Project Admin  <strong>qTest Manager version:</strong> 8.4.2+

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
api_instance = swagger_client.UserprofileApi()
project_id = 789 # int | ID of the project
body = swagger_client.AssignedUsersProfile() # AssignedUsersProfile | An array of user IDs and a user profile

try: 
    # Assigns multiple Users to a Profile in a Project
    api_response = api_instance.batch_assign_user_profile_in_project(project_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserprofileApi->batch_assign_user_profile_in_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **body** | [**AssignedUsersProfile**](AssignedUsersProfile.md)| An array of user IDs and a user profile | 

### Return type

[**list[UserResourceExtension]**](UserResourceExtension.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current**
> AdminProfile get_current()

Gets current User's Admin Profile

To retrieve your Admin Profile  <strong>qTest Manager version:</strong> 4+

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
api_instance = swagger_client.UserprofileApi()

try: 
    # Gets current User's Admin Profile
    api_response = api_instance.get_current()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserprofileApi->get_current: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AdminProfile**](AdminProfile.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profiles_of_current_user**
> list[UserProfile] get_profiles_of_current_user()

Gets current User's Profiles in different Projects

To retrieve your User Profiles in different Projects

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
api_instance = swagger_client.UserprofileApi()

try: 
    # Gets current User's Profiles in different Projects
    api_response = api_instance.get_profiles_of_current_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserprofileApi->get_profiles_of_current_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UserProfile]**](UserProfile.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_profiles**
> UserProfileResponse get_user_profiles(type=type)

Gets available Profiles

To retrieve all available profiles in your qTest Manager instance. It requires that your qTest Manager profile is a site admin with <em>View User Profiles</em> permissions  <strong>qTest Manager version:</strong> 8.4.2+

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
api_instance = swagger_client.UserprofileApi()
type = 'type_example' # str | <em>type=admin</em> - to retrieve only admin profiles  <em>type=use</em> - to retrieve only normal user profiles  Omit this parameter to include both (optional)

try: 
    # Gets available Profiles
    api_response = api_instance.get_user_profiles(type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserprofileApi->get_user_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| &lt;em&gt;type&#x3D;admin&lt;/em&gt; - to retrieve only admin profiles  &lt;em&gt;type&#x3D;use&lt;/em&gt; - to retrieve only normal user profiles  Omit this parameter to include both | [optional] 

### Return type

[**UserProfileResponse**](UserProfileResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

