# swagger_client.DefectApi

All URIs are relative to *https://apitryout.qtestnet.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_comment**](DefectApi.md#add_comment) | **POST** /api/v3/projects/{projectId}/defects/{idOrKey}/comments | Adds a Comment to a Defect
[**delete_comment**](DefectApi.md#delete_comment) | **DELETE** /api/v3/projects/{projectId}/defects/{idOrKey}/comments/{commentId} | Deletes a Comment of a Defect
[**get_comment**](DefectApi.md#get_comment) | **GET** /api/v3/projects/{projectId}/defects/{idOrKey}/comments/{commentId} | Gets a Comment of a Defect
[**get_comments**](DefectApi.md#get_comments) | **GET** /api/v3/projects/{projectId}/defects/{idOrKey}/comments | Gets all Comments of a Defect
[**get_defect**](DefectApi.md#get_defect) | **GET** /api/v3/projects/{projectId}/defects/{defectId} | Gets a Defect
[**get_last_changed**](DefectApi.md#get_last_changed) | **GET** /api/v3/projects/{projectId}/defects/last-change | Gets recently updated Defects
[**submit_defect**](DefectApi.md#submit_defect) | **POST** /api/v3/projects/{projectId}/defects | Submit a Defect
[**update_comment**](DefectApi.md#update_comment) | **PUT** /api/v3/projects/{projectId}/defects/{idOrKey}/comments/{commentId} | Updates a Comment of a Defect
[**update_defect**](DefectApi.md#update_defect) | **PUT** /api/v3/projects/{projectId}/defects/{defectId} | Updates a Defect


# **add_comment**
> CommentResource add_comment(project_id, id_or_key, body)

Adds a Comment to a Defect

To add a Comment to a Defect  <strong>qTest Manager version:</strong> 7.5+

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
api_instance = swagger_client.DefectApi()
project_id = 789 # int | ID of the project
id_or_key = 'id_or_key_example' # str | PID or ID of the Defect
body = swagger_client.CommentResource() # CommentResource | The Comment's content

try: 
    # Adds a Comment to a Defect
    api_response = api_instance.add_comment(project_id, id_or_key, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefectApi->add_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **id_or_key** | **str**| PID or ID of the Defect | 
 **body** | [**CommentResource**](CommentResource.md)| The Comment&#39;s content | 

### Return type

[**CommentResource**](CommentResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comment**
> object delete_comment(project_id, id_or_key, comment_id)

Deletes a Comment of a Defect

To delete a specific Comment of a Defect  <strong>qTest Manager version:</strong> 7.5+

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
api_instance = swagger_client.DefectApi()
project_id = 789 # int | ID of the project
id_or_key = 'id_or_key_example' # str | PID or ID of the Defect whose Comment you want to delete
comment_id = 789 # int | ID of the comment.

try: 
    # Deletes a Comment of a Defect
    api_response = api_instance.delete_comment(project_id, id_or_key, comment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefectApi->delete_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **id_or_key** | **str**| PID or ID of the Defect whose Comment you want to delete | 
 **comment_id** | **int**| ID of the comment. | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comment**
> CommentResource get_comment(project_id, id_or_key, comment_id)

Gets a Comment of a Defect

To retrieve a specific Comment of a Defect  <strong>qTest Manager version:</strong> 7.5+

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
api_instance = swagger_client.DefectApi()
project_id = 789 # int | ID of the project
id_or_key = 'id_or_key_example' # str | PID or ID of the Defect whose comment you want to retrieve
comment_id = 789 # int | ID of the comment

try: 
    # Gets a Comment of a Defect
    api_response = api_instance.get_comment(project_id, id_or_key, comment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefectApi->get_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **id_or_key** | **str**| PID or ID of the Defect whose comment you want to retrieve | 
 **comment_id** | **int**| ID of the comment | 

### Return type

[**CommentResource**](CommentResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comments**
> PagedResourceCommentResource get_comments(project_id, id_or_key, page=page, page_size=page_size)

Gets all Comments of a Defect

To retrieve all Comments of a Defect  <strong>qTest Manager version:</strong> 7.5+

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
api_instance = swagger_client.DefectApi()
project_id = 789 # int | ID of the project
id_or_key = 'id_or_key_example' # str | PID or ID of the Defect whose comments you want to retrieve
page = 1 # int | By default the first page is returned but you can specify any page number to retrieve objects (optional) (default to 1)
page_size = 100 # int | The result is paginated. By the default, the number of objects in each page is 100 if this is omitted. You can specify your custom number (up to 999) in this parameter (optional) (default to 100)

try: 
    # Gets all Comments of a Defect
    api_response = api_instance.get_comments(project_id, id_or_key, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefectApi->get_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **id_or_key** | **str**| PID or ID of the Defect whose comments you want to retrieve | 
 **page** | **int**| By default the first page is returned but you can specify any page number to retrieve objects | [optional] [default to 1]
 **page_size** | **int**| The result is paginated. By the default, the number of objects in each page is 100 if this is omitted. You can specify your custom number (up to 999) in this parameter | [optional] [default to 100]

### Return type

[**PagedResourceCommentResource**](PagedResourceCommentResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_defect**
> DefectResource get_defect(project_id, defect_id)

Gets a Defect

To retrieve a Defect  <strong>qTest Manager version:</strong> 6+

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
api_instance = swagger_client.DefectApi()
project_id = 789 # int | ID of the project
defect_id = 'defect_id_example' # str | ID of the defect.

try: 
    # Gets a Defect
    api_response = api_instance.get_defect(project_id, defect_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefectApi->get_defect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **defect_id** | **str**| ID of the defect. | 

### Return type

[**DefectResource**](DefectResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_last_changed**
> list[DefectResource] get_last_changed(project_id, start_time, end_time=end_time, size=size, page=page)

Gets recently updated Defects

To retrieve Defects which have been recently updated after a specified time

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
api_instance = swagger_client.DefectApi()
project_id = 789 # int | ID of the project
start_time = 'start_time_example' # str | The specified time since when the Defects have been updated. It needs to be URL encoded: <em>yyyy-MM-dd'T'HH:mm:ss.SSSZ</em> or <em>yyyy-MM-dd'T'HH:mm:ssZZ</em>
end_time = 'end_time_example' # str | Do not support at this time. Use the current time only. (optional)
size = 20 # int | The result is paginated. By the default, the number of objects in each page is 100. You can specify your custom number in this parameter. The maximum page size is 999. (optional) (default to 20)
page = 1 # int | By default the first page is returned but you can specify any page number to retrieve objects (optional) (default to 1)

try: 
    # Gets recently updated Defects
    api_response = api_instance.get_last_changed(project_id, start_time, end_time=end_time, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefectApi->get_last_changed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **start_time** | **str**| The specified time since when the Defects have been updated. It needs to be URL encoded: &lt;em&gt;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ&lt;/em&gt; or &lt;em&gt;yyyy-MM-dd&#39;T&#39;HH:mm:ssZZ&lt;/em&gt; | 
 **end_time** | **str**| Do not support at this time. Use the current time only. | [optional] 
 **size** | **int**| The result is paginated. By the default, the number of objects in each page is 100. You can specify your custom number in this parameter. The maximum page size is 999. | [optional] [default to 20]
 **page** | **int**| By default the first page is returned but you can specify any page number to retrieve objects | [optional] [default to 1]

### Return type

[**list[DefectResource]**](DefectResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_defect**
> DefectResource submit_defect(project_id, body)

Submit a Defect

To submit an internal Defect

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
api_instance = swagger_client.DefectApi()
project_id = 789 # int | ID of the project
body = swagger_client.DefectResource() # DefectResource | <em>properties:</em> a JSONArray of field-value pairs  <em>attachments:</em> a JSONArray of Attachment objects

try: 
    # Submit a Defect
    api_response = api_instance.submit_defect(project_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefectApi->submit_defect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **body** | [**DefectResource**](DefectResource.md)| &lt;em&gt;properties:&lt;/em&gt; a JSONArray of field-value pairs  &lt;em&gt;attachments:&lt;/em&gt; a JSONArray of Attachment objects | 

### Return type

[**DefectResource**](DefectResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_comment**
> CommentResource update_comment(project_id, id_or_key, comment_id, body)

Updates a Comment of a Defect

To update a specific Comment of a Defect  <strong>qTest Manager version:</strong> 7.5+

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
api_instance = swagger_client.DefectApi()
project_id = 789 # int | ID of the project
id_or_key = 'id_or_key_example' # str | PID or ID of the defect whose comment you want to update
comment_id = 789 # int | ID of the comment
body = swagger_client.CommentResource() # CommentResource | Given resource to update a comment.

try: 
    # Updates a Comment of a Defect
    api_response = api_instance.update_comment(project_id, id_or_key, comment_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefectApi->update_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **id_or_key** | **str**| PID or ID of the defect whose comment you want to update | 
 **comment_id** | **int**| ID of the comment | 
 **body** | [**CommentResource**](CommentResource.md)| Given resource to update a comment. | 

### Return type

[**CommentResource**](CommentResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_defect**
> DefectResource update_defect(project_id, defect_id, body)

Updates a Defect

To update a Defect  <strong>qTest Manager version:</strong> 6+

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
api_instance = swagger_client.DefectApi()
project_id = 789 # int | ID of the project
defect_id = 789 # int | ID of the Defect which needs to be updated.
body = swagger_client.DefectResource() # DefectResource | The Defect's updated properties

try: 
    # Updates a Defect
    api_response = api_instance.update_defect(project_id, defect_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefectApi->update_defect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **defect_id** | **int**| ID of the Defect which needs to be updated. | 
 **body** | [**DefectResource**](DefectResource.md)| The Defect&#39;s updated properties | 

### Return type

[**DefectResource**](DefectResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

