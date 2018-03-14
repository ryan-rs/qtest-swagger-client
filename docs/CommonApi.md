# swagger_client.CommonApi

All URIs are relative to *https://apitryout.qtestnet.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edit_system_field**](CommonApi.md#edit_system_field) | **POST** /api/v3/projects/{projectId}/settings/{objectType}/system-fields/{fieldId} | Edit System Field of an Object Type by the field
[**update_custom_field**](CommonApi.md#update_custom_field) | **POST** /api/v3/projects/{projectId}/settings/{objectType}/custom-fields/active | field.updateCustomField


# **edit_system_field**
> FieldResource edit_system_field(project_id, field_id, body, object_type)

Edit System Field of an Object Type by the field

To edit System Field of an Object Type by the field

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
api_instance = swagger_client.CommonApi()
project_id = 789 # int | ID of the project
field_id = 789 # int | ID of the field.
body = swagger_client.FieldResource() # FieldResource | Given resource to edit a system field.
object_type = 'object_type_example' # str | The object type.

try: 
    # Edit System Field of an Object Type by the field
    api_response = api_instance.edit_system_field(project_id, field_id, body, object_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonApi->edit_system_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **field_id** | **int**| ID of the field. | 
 **body** | [**FieldResource**](FieldResource.md)| Given resource to edit a system field. | 
 **object_type** | **str**| The object type. | 

### Return type

[**FieldResource**](FieldResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_field**
> list[FieldResource] update_custom_field(project_id, object_type, body)

field.updateCustomField

Update active or inactive custom fields of an Object Type

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
api_instance = swagger_client.CommonApi()
project_id = 789 # int | ID of the project
object_type = 'object_type_example' # str | The object type
body = [swagger_client.FieldResource()] # list[FieldResource] | Given resource to update custom fields.

try: 
    # field.updateCustomField
    api_response = api_instance.update_custom_field(project_id, object_type, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonApi->update_custom_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **object_type** | **str**| The object type | 
 **body** | [**list[FieldResource]**](FieldResource.md)| Given resource to update custom fields. | 

### Return type

[**list[FieldResource]**](FieldResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

