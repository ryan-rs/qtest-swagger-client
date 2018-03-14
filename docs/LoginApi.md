# swagger_client.LoginApi

All URIs are relative to *https://apitryout.qtestnet.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_access_token**](LoginApi.md#post_access_token) | **POST** /oauth/token | Log in


# **post_access_token**
> OAuthResponse post_access_token(grant_type=grant_type, username=username, password=password, authorization=authorization)

Log in

To authenticate the API client against qTest Manager and acquire authorized access token

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LoginApi()
grant_type = 'password' # str | always use <em>grant_type=password</em> (optional) (default to password)
username = 'username_example' # str | Your qTest Manager username (optional)
password = 'password_example' # str | Your qTest Manager password (optional)
authorization = 'authorization_example' # str | Basic + [base64 string of \"your qTest Manager site name:\"]  Example: qTest Manager site is: apitryout.qtestnet.com then site name is: apitryout, then Authorization is: Basic YXBpdHJ5b3V0Og== (optional)

try: 
    # Log in
    api_response = api_instance.post_access_token(grant_type=grant_type, username=username, password=password, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginApi->post_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**| always use &lt;em&gt;grant_type&#x3D;password&lt;/em&gt; | [optional] [default to password]
 **username** | **str**| Your qTest Manager username | [optional] 
 **password** | **str**| Your qTest Manager password | [optional] 
 **authorization** | **str**| Basic + [base64 string of \&quot;your qTest Manager site name:\&quot;]  Example: qTest Manager site is: apitryout.qtestnet.com then site name is: apitryout, then Authorization is: Basic YXBpdHJ5b3V0Og&#x3D;&#x3D; | [optional] 

### Return type

[**OAuthResponse**](OAuthResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

