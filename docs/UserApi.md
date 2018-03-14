# swagger_client.UserApi

All URIs are relative to *https://apitryout.qtestnet.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_to_project**](UserApi.md#assign_to_project) | **POST** /api/v3/users/{userId}/projects | Assigns a User to a Project
[**assign_users_to_project**](UserApi.md#assign_users_to_project) | **POST** /api/v3/users/projects | Assigns multiple Users to a Project
[**create_user**](UserApi.md#create_user) | **POST** /api/v3/users | Invites a User
[**find_by_user_name_or_email**](UserApi.md#find_by_user_name_or_email) | **GET** /api/v3/users/search | Queries Users by Username
[**find_users_by_projects_name**](UserApi.md#find_users_by_projects_name) | **GET** /api/v3/search/user | Queries Users by Project Name
[**get_avatar**](UserApi.md#get_avatar) | **GET** /api/v3/users/{userId}/avatar | Gets a User&#39;s Avatar
[**get_user_by_id**](UserApi.md#get_user_by_id) | **GET** /api/v3/users/{userId} | Gets a User
[**reevaluate_token**](UserApi.md#reevaluate_token) | **GET** /api/v3/re-evaluation | Gets current user&#39;s information


# **assign_to_project**
> AssignedProject assign_to_project(user_id, body)

Assigns a User to a Project

To assign a User to a Project

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
api_instance = swagger_client.UserApi()
user_id = 789 # int | ID of the user.
body = swagger_client.AssignedProject() # AssignedProject | The project ID and the assigned user profile in the project. If the profile is not provided, profile Developer is used by default

try: 
    # Assigns a User to a Project
    api_response = api_instance.assign_to_project(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->assign_to_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ID of the user. | 
 **body** | [**AssignedProject**](AssignedProject.md)| The project ID and the assigned user profile in the project. If the profile is not provided, profile Developer is used by default | 

### Return type

[**AssignedProject**](AssignedProject.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_users_to_project**
> AssignedUsersProject assign_users_to_project(body)

Assigns multiple Users to a Project

To assign a list of Users to a Project  <strong>qTest Manager version:</strong> 4+

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
api_instance = swagger_client.UserApi()
body = swagger_client.AssignedUsersProject() # AssignedUsersProject | ID of the Project and an array of assigned Users' IDs. If the profile is not provided, Developer profile is used by default

try: 
    # Assigns multiple Users to a Project
    api_response = api_instance.assign_users_to_project(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->assign_users_to_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssignedUsersProject**](AssignedUsersProject.md)| ID of the Project and an array of assigned Users&#39; IDs. If the profile is not provided, Developer profile is used by default | 

### Return type

[**AssignedUsersProject**](AssignedUsersProject.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> UserResource create_user(body)

Invites a User

To invite a user to your qTest Manager instance and activate the account. If the password is omitted, the default \"<em>admin123</em>\" will be used  <strong>qTest Manager version:</strong> 4+

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
api_instance = swagger_client.UserApi()
body = swagger_client.UserResource() # UserResource | Invited user's information

try: 
    # Invites a User
    api_response = api_instance.create_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserResource**](UserResource.md)| Invited user&#39;s information | 

### Return type

[**UserResource**](UserResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_by_user_name_or_email**
> SearchUserResourceExtensionResponse find_by_user_name_or_email(username=username, include_inactive_users=include_inactive_users, pagination=pagination, page=page, page_size=page_size)

Queries Users by Username

To query for users by their username  <strong>qTest Manager version:</strong> 8.4.2+

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
api_instance = swagger_client.UserApi()
username = 'username_example' # str | Login names (qTest login email, LDAP or SSO username) of users you want to query for. The API will return users which have been added to projects whose names contain the text specified in this parameter  <strong>IMPORTANT:</strong> Login name is case sensitive (optional)
include_inactive_users = true # bool | <em>includeInactiveUsers=false</em> - default value. Inactive users are excluded from the response  <em>includeInactiveUsers=true</em> - inactive users are included in the response (optional)
pagination = true # bool | <em>pagination=true</em> - default value. The result is paginated  <em>pagination=false</em> - the result is not paginated (optional)
page = 1 # int | By default the first page is returned but you can specify any page number to retrieve objects (optional) (default to 1)
page_size = 100 # int | The result is paginated. By the default, the number of objects in each page is 100 if this is omitted. You can specify your custom number (up to 999) in this parameter (optional) (default to 100)

try: 
    # Queries Users by Username
    api_response = api_instance.find_by_user_name_or_email(username=username, include_inactive_users=include_inactive_users, pagination=pagination, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->find_by_user_name_or_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Login names (qTest login email, LDAP or SSO username) of users you want to query for. The API will return users which have been added to projects whose names contain the text specified in this parameter  &lt;strong&gt;IMPORTANT:&lt;/strong&gt; Login name is case sensitive | [optional] 
 **include_inactive_users** | **bool**| &lt;em&gt;includeInactiveUsers&#x3D;false&lt;/em&gt; - default value. Inactive users are excluded from the response  &lt;em&gt;includeInactiveUsers&#x3D;true&lt;/em&gt; - inactive users are included in the response | [optional] 
 **pagination** | **bool**| &lt;em&gt;pagination&#x3D;true&lt;/em&gt; - default value. The result is paginated  &lt;em&gt;pagination&#x3D;false&lt;/em&gt; - the result is not paginated | [optional] 
 **page** | **int**| By default the first page is returned but you can specify any page number to retrieve objects | [optional] [default to 1]
 **page_size** | **int**| The result is paginated. By the default, the number of objects in each page is 100 if this is omitted. You can specify your custom number (up to 999) in this parameter | [optional] [default to 100]

### Return type

[**SearchUserResourceExtensionResponse**](SearchUserResourceExtensionResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_users_by_projects_name**
> SearchUserResponse find_users_by_projects_name(project_name=project_name, inactive=inactive, pagination=pagination, page=page, page_size=page_size)

Queries Users by Project Name

To query for users by names of their assigned projects  - Admin users with <em>Manage Client Users</em> permission can query users in any projects  - For other users: the API only returns users within projects to which the requesting user is assigned

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
api_instance = swagger_client.UserApi()
project_name = 'project_name_example' # str | Name of the project whose users you want to query for. The API will return users which have been added to projects whose names contain the text specified in this parameter  <strong>IMPORTANT:</strong> Project name is case sensitive (optional)
inactive = true # bool | <em>inactive=false</em> - default value. Inactive users are excluded from the response  <em>inactive=true</em> - include inactive users (optional) (default to true)
pagination = true # bool | <em>pagination=true</em> - default value. The result is paginated  <em>pagination=false</em> - the result is not paginated (optional) (default to true)
page = 1 # int | By default the first page is returned but you can specify any page number to retrieve objects (optional) (default to 1)
page_size = 100 # int | The result is paginated. By the default, the number of objects in each page is 100 if this is omitted. You can specify your custom number (up to 999) in this parameter (optional) (default to 100)

try: 
    # Queries Users by Project Name
    api_response = api_instance.find_users_by_projects_name(project_name=project_name, inactive=inactive, pagination=pagination, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->find_users_by_projects_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| Name of the project whose users you want to query for. The API will return users which have been added to projects whose names contain the text specified in this parameter  &lt;strong&gt;IMPORTANT:&lt;/strong&gt; Project name is case sensitive | [optional] 
 **inactive** | **bool**| &lt;em&gt;inactive&#x3D;false&lt;/em&gt; - default value. Inactive users are excluded from the response  &lt;em&gt;inactive&#x3D;true&lt;/em&gt; - include inactive users | [optional] [default to true]
 **pagination** | **bool**| &lt;em&gt;pagination&#x3D;true&lt;/em&gt; - default value. The result is paginated  &lt;em&gt;pagination&#x3D;false&lt;/em&gt; - the result is not paginated | [optional] [default to true]
 **page** | **int**| By default the first page is returned but you can specify any page number to retrieve objects | [optional] [default to 1]
 **page_size** | **int**| The result is paginated. By the default, the number of objects in each page is 100 if this is omitted. You can specify your custom number (up to 999) in this parameter | [optional] [default to 100]

### Return type

[**SearchUserResponse**](SearchUserResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_avatar**
> OutputStream get_avatar(user_id)

Gets a User's Avatar

To retrieve a User's Avatar

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
api_instance = swagger_client.UserApi()
user_id = 789 # int | ID of the user.

try: 
    # Gets a User's Avatar
    api_response = api_instance.get_avatar(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_avatar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ID of the user. | 

### Return type

[**OutputStream**](OutputStream.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_id**
> UserResource get_user_by_id(user_id)

Gets a User

To retrieve a User's information

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
api_instance = swagger_client.UserApi()
user_id = 789 # int | ID of the user.

try: 
    # Gets a User
    api_response = api_instance.get_user_by_id(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ID of the user. | 

### Return type

[**UserResource**](UserResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reevaluate_token**
> LoggedUser reevaluate_token(include_inaccessible_apps=include_inaccessible_apps)

Gets current user's information

To retrieve your information such as username, email, first name, and last name

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
api_instance = swagger_client.UserApi()
include_inaccessible_apps = true # bool |  (optional)

try: 
    # Gets current user's information
    api_response = api_instance.reevaluate_token(include_inaccessible_apps=include_inaccessible_apps)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->reevaluate_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_inaccessible_apps** | **bool**|  | [optional] 

### Return type

[**LoggedUser**](LoggedUser.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

