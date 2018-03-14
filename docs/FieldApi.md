# swagger_client.FieldApi

All URIs are relative to *https://apitryout.qtestnet.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](FieldApi.md#create) | **POST** /api/v3/projects/{projectId}/settings/{objectType}/fields | Creates a Custom Field of an Object Type
[**get_fields**](FieldApi.md#get_fields) | **GET** /api/v3/projects/{projectId}/settings/{objectType}/fields | Gets all Fields of an Object Type


# **create**
> FieldResource create(project_id, body, object_type)

Creates a Custom Field of an Object Type

To create a new custom Field for Release, Build, Requirement, Test Case, Test Suite, Test Run, or Defect

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
api_instance = swagger_client.FieldApi()
project_id = 789 # int | ID of the project
body = swagger_client.FieldResource() # FieldResource | The field's properties and values  <strong>data_type (required):</strong> specify the field type. Its valid values include  - 1 - Text box  - 2 - Text area  - 3 - Combo box  - 4 - Date picker  - 5 - User list  - 6 - Rich text editor  - 7 - Number  - 8 - Check box  - 9 - Date time picker  - 12 - URL  - 17 - Multiple selection combobox  In case you are creating a multiple picklist typed field (data_type's value is 8 or 17), you will need to specify <em>multiple=true</em>  In case you are creating a picklist typed field, you can specify the field's values in the <em>allowed_values</em> array
object_type = 'object_type_example' # str | Valid values include releases, builds, requirements, test-cases, defects, test-suites and test-runs

try: 
    # Creates a Custom Field of an Object Type
    api_response = api_instance.create(project_id, body, object_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **body** | [**FieldResource**](FieldResource.md)| The field&#39;s properties and values  &lt;strong&gt;data_type (required):&lt;/strong&gt; specify the field type. Its valid values include  - 1 - Text box  - 2 - Text area  - 3 - Combo box  - 4 - Date picker  - 5 - User list  - 6 - Rich text editor  - 7 - Number  - 8 - Check box  - 9 - Date time picker  - 12 - URL  - 17 - Multiple selection combobox  In case you are creating a multiple picklist typed field (data_type&#39;s value is 8 or 17), you will need to specify &lt;em&gt;multiple&#x3D;true&lt;/em&gt;  In case you are creating a picklist typed field, you can specify the field&#39;s values in the &lt;em&gt;allowed_values&lt;/em&gt; array | 
 **object_type** | **str**| Valid values include releases, builds, requirements, test-cases, defects, test-suites and test-runs | 

### Return type

[**FieldResource**](FieldResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fields**
> list[FieldResource] get_fields(project_id, object_type, include_inactive=include_inactive)

Gets all Fields of an Object Type

To retrieve Fields of an Object Type  <strong>qTest Manager version:</strong> 4+

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
api_instance = swagger_client.FieldApi()
project_id = 789 # int | ID of the project
object_type = 'object_type_example' # str | valid values include releases, builds, requirements, test-cases, defects, test-suites and test-runs
include_inactive = true # bool | By default inactive Fields are excluded from the response. Specify <em>includeInactive=true</em> to include inactive fields (optional)

try: 
    # Gets all Fields of an Object Type
    api_response = api_instance.get_fields(project_id, object_type, include_inactive=include_inactive)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldApi->get_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **object_type** | **str**| valid values include releases, builds, requirements, test-cases, defects, test-suites and test-runs | 
 **include_inactive** | **bool**| By default inactive Fields are excluded from the response. Specify &lt;em&gt;includeInactive&#x3D;true&lt;/em&gt; to include inactive fields | [optional] 

### Return type

[**list[FieldResource]**](FieldResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

