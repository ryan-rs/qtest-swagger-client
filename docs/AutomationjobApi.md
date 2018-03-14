# swagger_client.AutomationjobApi

All URIs are relative to *https://apitryout.qtestnet.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_schedule**](AutomationjobApi.md#create_schedule) | **POST** /api/v3/automation/jobs/schedule/create | Create a Schedule


# **create_schedule**
> int create_schedule(body)

Create a Schedule

To create a new Schedule which will be executed immediately  <strong>NOTE:</strong> Try It Out function will not work for this API  <strong>qTest Manager version:</strong> 6+\"

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
api_instance = swagger_client.AutomationjobApi()
body = swagger_client.AutomationScheduleCreationAPI() # AutomationScheduleCreationAPI | 

try: 
    # Create a Schedule
    api_response = api_instance.create_schedule(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutomationjobApi->create_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AutomationScheduleCreationAPI**](AutomationScheduleCreationAPI.md)|  | 

### Return type

**int**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

