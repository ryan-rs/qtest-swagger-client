# swagger_client.AttachmentApi

All URIs are relative to *https://apitryout.qtestnet.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](AttachmentApi.md#delete) | **DELETE** /api/v3/projects/{projectId}/{objectType}/{objectId}/blob-handles/{blobHandleId} | Deletes an Attachment from an Object
[**get_attachment**](AttachmentApi.md#get_attachment) | **GET** /api/v3/projects/{projectId}/{objectType}/{objectId}/attachments/{attachmentId} | Gets an Attachment of an Object
[**get_attachments_of**](AttachmentApi.md#get_attachments_of) | **GET** /api/v3/projects/{projectId}/{objectType}/{objectId}/attachments | Gets all Attachments of an Object
[**search**](AttachmentApi.md#search) | **GET** /api/v3/projects/{projectId}/attachments | Searches for Attachments
[**upload**](AttachmentApi.md#upload) | **POST** /api/v3/projects/{projectId}/{objectType}/{objectId}/blob-handles | Uploads an Attachment to an Object


# **delete**
> Message delete(project_id, blob_handle_id, object_type, object_id)

Deletes an Attachment from an Object

To delete an Attachment from a Release, Build, Requirement, Test Case, Test Log, Test Step or Defect  <strong>qTest Manager version:</strong> 7.5+

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
api_instance = swagger_client.AttachmentApi()
project_id = 789 # int | ID of the project
blob_handle_id = 789 # int | ID of the Attachment
object_type = 'object_type_example' # str | Valid values include releases, builds, requirements, test-cases, test-logs, test-steps or defects  <strong>qTest Manager version:</strong> 4+
object_id = 789 # int | ID of the object (Release, Build, Requirement, Test Case, Test Log, Test Step or Defect)

try: 
    # Deletes an Attachment from an Object
    api_response = api_instance.delete(project_id, blob_handle_id, object_type, object_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **blob_handle_id** | **int**| ID of the Attachment | 
 **object_type** | **str**| Valid values include releases, builds, requirements, test-cases, test-logs, test-steps or defects  &lt;strong&gt;qTest Manager version:&lt;/strong&gt; 4+ | 
 **object_id** | **int**| ID of the object (Release, Build, Requirement, Test Case, Test Log, Test Step or Defect) | 

### Return type

[**Message**](Message.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachment**
> OutputStream get_attachment(project_id, attachment_id, object_type, object_id)

Gets an Attachment of an Object

To retrieve an Attachment from a Release, Build, Requirement, Test Case, Test Log, Test Step or Defect

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
api_instance = swagger_client.AttachmentApi()
project_id = 789 # int | ID of the project
attachment_id = 789 # int | ID of attachment
object_type = 'object_type_example' # str | Valid values include <em>release</em>, <em>build</em>, <em>requirements</em>, <em>test-cases</em>, <em>test-logs</em>, <em>test-steps</em>, or <em>defects</em>
object_id = 789 # int | ID of the object (Release, Build, Requirement, Test Case, Test Log, Test Step or Defect)

try: 
    # Gets an Attachment of an Object
    api_response = api_instance.get_attachment(project_id, attachment_id, object_type, object_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentApi->get_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **attachment_id** | **int**| ID of attachment | 
 **object_type** | **str**| Valid values include &lt;em&gt;release&lt;/em&gt;, &lt;em&gt;build&lt;/em&gt;, &lt;em&gt;requirements&lt;/em&gt;, &lt;em&gt;test-cases&lt;/em&gt;, &lt;em&gt;test-logs&lt;/em&gt;, &lt;em&gt;test-steps&lt;/em&gt;, or &lt;em&gt;defects&lt;/em&gt; | 
 **object_id** | **int**| ID of the object (Release, Build, Requirement, Test Case, Test Log, Test Step or Defect) | 

### Return type

[**OutputStream**](OutputStream.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachments_of**
> list[AttachmentResource] get_attachments_of(project_id, object_type, object_id)

Gets all Attachments of an Object

To retrieve all Attachments of a Release, Build, Requirement, Test Case, Test Log, Test Step or Defect

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
api_instance = swagger_client.AttachmentApi()
project_id = 789 # int | ID of the project
object_type = 'object_type_example' # str | Valid values include <em>release</em>, <em>build</em>, <em>requirements</em>, <em>test-cases</em>, <em>test-logs</em>, <em>test-steps</em>, or <em>defects</em>
object_id = 789 # int | ID of the object (Release, Build, Requirement, Test Case, Test Log, Test Step or Defect)

try: 
    # Gets all Attachments of an Object
    api_response = api_instance.get_attachments_of(project_id, object_type, object_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentApi->get_attachments_of: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **object_type** | **str**| Valid values include &lt;em&gt;release&lt;/em&gt;, &lt;em&gt;build&lt;/em&gt;, &lt;em&gt;requirements&lt;/em&gt;, &lt;em&gt;test-cases&lt;/em&gt;, &lt;em&gt;test-logs&lt;/em&gt;, &lt;em&gt;test-steps&lt;/em&gt;, or &lt;em&gt;defects&lt;/em&gt; | 
 **object_id** | **int**| ID of the object (Release, Build, Requirement, Test Case, Test Log, Test Step or Defect) | 

### Return type

[**list[AttachmentResource]**](AttachmentResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search**
> PagedResourceAttachmentResource search(project_id, type, ids=ids, author=author, created_date=created_date, page_size=page_size, page=page)

Searches for Attachments

To query for attachments of <em>Releases</em>, <em>Builds</em>, <em>Requirements</em>, <em>Test Cases</em>, <em>Test Logs</em>, <em>Test Steps</em> or <em>Defects</em>

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
api_instance = swagger_client.AttachmentApi()
project_id = 789 # int | ID of the project
type = 'type_example' # str | Its valid values include <em>releases</em>, <em>builds</em>, <em>requirements</em>, <em>test-cases</em>, <em>test-steps</em>, <em>test-logs</em> or <em>defects</em>
ids = [56] # list[int] | List of object IDs (of the same type as specified in the parameter above), separated by commas (optional)
author = 789 # int | ID of the user who created the attachment (optional)
created_date = 'created_date_example' # str | Its format is: <strong>{operator} {createdDate in timestamp or UTC}</strong>  The <em>operator</em> can be one of the following values:  <b>lt</b>: less than the given date  <b>gt</b>: greater than given date  <b>eq</b>: equal to the given date  <b>le</b>: less than or equal to the given date  <b>ge</b>: greater then or equal to the given date (optional)
page_size = 100 # int | The result is paginated. By the default, the number of objects in each page is 100 if this is omitted. You can specify your custom number (up to 999) in this parameter (optional) (default to 100)
page = 1 # int | By default, the first page is returned but you can specify any page number to retrieve attachments (optional) (default to 1)

try: 
    # Searches for Attachments
    api_response = api_instance.search(project_id, type, ids=ids, author=author, created_date=created_date, page_size=page_size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentApi->search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **type** | **str**| Its valid values include &lt;em&gt;releases&lt;/em&gt;, &lt;em&gt;builds&lt;/em&gt;, &lt;em&gt;requirements&lt;/em&gt;, &lt;em&gt;test-cases&lt;/em&gt;, &lt;em&gt;test-steps&lt;/em&gt;, &lt;em&gt;test-logs&lt;/em&gt; or &lt;em&gt;defects&lt;/em&gt; | 
 **ids** | [**list[int]**](int.md)| List of object IDs (of the same type as specified in the parameter above), separated by commas | [optional] 
 **author** | **int**| ID of the user who created the attachment | [optional] 
 **created_date** | **str**| Its format is: &lt;strong&gt;{operator} {createdDate in timestamp or UTC}&lt;/strong&gt;  The &lt;em&gt;operator&lt;/em&gt; can be one of the following values:  &lt;b&gt;lt&lt;/b&gt;: less than the given date  &lt;b&gt;gt&lt;/b&gt;: greater than given date  &lt;b&gt;eq&lt;/b&gt;: equal to the given date  &lt;b&gt;le&lt;/b&gt;: less than or equal to the given date  &lt;b&gt;ge&lt;/b&gt;: greater then or equal to the given date | [optional] 
 **page_size** | **int**| The result is paginated. By the default, the number of objects in each page is 100 if this is omitted. You can specify your custom number (up to 999) in this parameter | [optional] [default to 100]
 **page** | **int**| By default, the first page is returned but you can specify any page number to retrieve attachments | [optional] [default to 1]

### Return type

[**PagedResourceAttachmentResource**](PagedResourceAttachmentResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload**
> AttachmentResource upload(project_id, object_type, object_id, file_name, content_type, body)

Uploads an Attachment to an Object

To upload an Attachment to a Release, Build, Requirement, Test Case, Test Log, Test Step, or Defect

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
api_instance = swagger_client.AttachmentApi()
project_id = 789 # int | ID of the project
object_type = 'object_type_example' # str | Valid values include releases, builds, requirements, test-cases, test-logs, test-steps or defects  <strong>qTest Manager version:</strong> 4+
object_id = 789 # int | ID of the object (Release, Build, Requirement, Test Case, Test Log, Test Step or Defect)
file_name = 'file_name_example' # str | 
content_type = 'content_type_example' # str | 
body = 'body_example' # str | 

try: 
    # Uploads an Attachment to an Object
    api_response = api_instance.upload(project_id, object_type, object_id, file_name, content_type, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentApi->upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **object_type** | **str**| Valid values include releases, builds, requirements, test-cases, test-logs, test-steps or defects  &lt;strong&gt;qTest Manager version:&lt;/strong&gt; 4+ | 
 **object_id** | **int**| ID of the object (Release, Build, Requirement, Test Case, Test Log, Test Step or Defect) | 
 **file_name** | **str**|  | 
 **content_type** | **str**|  | 
 **body** | **str**|  | 

### Return type

[**AttachmentResource**](AttachmentResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

