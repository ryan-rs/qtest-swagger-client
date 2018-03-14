# swagger_client.TestlogApi

All URIs are relative to *https://apitryout.qtestnet.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_last_run_log**](TestlogApi.md#get_last_run_log) | **GET** /api/v3/projects/{projectId}/test-runs/{testRunId}/test-logs/last-run | Gets the latest Test Log of a Test Run
[**get_test_log**](TestlogApi.md#get_test_log) | **GET** /api/v3/projects/{projectId}/test-runs/{testRunId}/test-logs/{id} | Gets a Test Log of a Test Run
[**get_test_logs_list**](TestlogApi.md#get_test_logs_list) | **GET** /api/v3/projects/{projectId}/test-runs/{testRunId}/test-logs | Gets all Test Logs of a Test Run
[**submit_automation_log**](TestlogApi.md#submit_automation_log) | **POST** /api/v3/projects/{projectId}/test-runs/{testRunId}/auto-test-logs | Submits an Automation Test Log
[**submit_automation_test_logs**](TestlogApi.md#submit_automation_test_logs) | **POST** /api/v3.1/projects/{projectId}/test-runs/{testRunId}/auto-test-logs | Submits multiple test results
[**submit_automation_test_logs_0**](TestlogApi.md#submit_automation_test_logs_0) | **POST** /api/v3/projects/{projectId}/auto-test-logs | Submits multiple test results and specifies Test Design and Test Execution tree structures
[**submit_test_log**](TestlogApi.md#submit_test_log) | **POST** /api/v3/projects/{projectId}/test-runs/{testRunId}/test-logs | Submits a Manual Test Log
[**track**](TestlogApi.md#track) | **GET** /api/v3/projects/queue-processing/{id} | Gets a Batch Test Log Submission job&#39;s state


# **get_last_run_log**
> TestLogResource get_last_run_log(project_id, test_run_id, expand=expand)

Gets the latest Test Log of a Test Run

To retrieve a Test Run's latest test result  <strong>qTest Manager version:</strong> 4+

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
api_instance = swagger_client.TestlogApi()
project_id = 789 # int | ID of the project
test_run_id = 789 # int | ID of the Test Run
expand = 'expand_example' # str | Valid values include:   i)<em>testcase</em> - to expand the associated Test Case and its Test Steps in the response;   ii) <em>teststeplog.teststep</em> - to expand results of each Test Steps in the response (optional)

try: 
    # Gets the latest Test Log of a Test Run
    api_response = api_instance.get_last_run_log(project_id, test_run_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestlogApi->get_last_run_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **test_run_id** | **int**| ID of the Test Run | 
 **expand** | **str**| Valid values include:   i)&lt;em&gt;testcase&lt;/em&gt; - to expand the associated Test Case and its Test Steps in the response;   ii) &lt;em&gt;teststeplog.teststep&lt;/em&gt; - to expand results of each Test Steps in the response | [optional] 

### Return type

[**TestLogResource**](TestLogResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_log**
> TestLogResource get_test_log(project_id, id, test_run_id)

Gets a Test Log of a Test Run

To retrieve a specific Test Log of a Test Run

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
api_instance = swagger_client.TestlogApi()
project_id = 789 # int | ID of the project
id = 789 # int | ID of the Test Log
test_run_id = 789 # int | ID of the Test Run

try: 
    # Gets a Test Log of a Test Run
    api_response = api_instance.get_test_log(project_id, id, test_run_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestlogApi->get_test_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **id** | **int**| ID of the Test Log | 
 **test_run_id** | **int**| ID of the Test Run | 

### Return type

[**TestLogResource**](TestLogResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_logs_list**
> TestLogListResource get_test_logs_list(project_id, test_run_id, page_size=page_size, page=page)

Gets all Test Logs of a Test Run

To retrieve all Test Logs of a Test Run  <strong>qTest Manager version:</strong> 7.6

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
api_instance = swagger_client.TestlogApi()
project_id = 789 # int | ID of the project
test_run_id = 789 # int | ID of the Test Run
page_size = 100 # int | The result is paginated. By the default, the number of objects in each page is 100 if this is omitted. You can specify your custom number (up to 999) in this parameter (optional) (default to 100)
page = 1 # int | By default the first page is returned but you can specify any page number to retrieve objects (optional) (default to 1)

try: 
    # Gets all Test Logs of a Test Run
    api_response = api_instance.get_test_logs_list(project_id, test_run_id, page_size=page_size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestlogApi->get_test_logs_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **test_run_id** | **int**| ID of the Test Run | 
 **page_size** | **int**| The result is paginated. By the default, the number of objects in each page is 100 if this is omitted. You can specify your custom number (up to 999) in this parameter | [optional] [default to 100]
 **page** | **int**| By default the first page is returned but you can specify any page number to retrieve objects | [optional] [default to 1]

### Return type

[**TestLogListResource**](TestLogListResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_automation_log**
> AutomationTestLogResource submit_automation_log(project_id, body, test_run_id, suite_per_day=suite_per_day, suite_date=suite_date, encode_note=encode_note, force_update_version=force_update_version, user_id=user_id)

Submits an Automation Test Log

To submit test result of an Automation Test Run  <strong>qTest Manager version:</strong> 4+

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
api_instance = swagger_client.TestlogApi()
project_id = 789 # int | ID of the project
body = swagger_client.AutomationTestLogResource() # AutomationTestLogResource | <em>status (required):</em> automation status values which are mapped in qTest Manager's Automation Settings  <em>exe_start_date (required):</em> the execution's starting time  <em>exe_end_date (required)</em> the execution's ending time  <em>name (required)</em> name of the Test Run or Test Case  <em>automation_content (required):</em> a string that uniquely identifies an Automation Test Case  <em>attachments:</em> a JSONArray of Attachment objects  <em>note:</em> execution note  <em>test_case_version_id:</em> ID of the associated Test Case's version  <em>test_step_logs:</em> a JSONArray of TestStepLog objects
test_run_id = 789 # int | ID of the Test Run  1/ If it is greater than 0 (zero), test result will be submitted to the specific Test Run  If it is 0 (zero), test result will be submitted to a new Test Run
suite_per_day = 'suite_per_day_example' # str | <em>suitePerDay=true</em> - the newly created Test Run will be located under a Test Suite named under the execution date specified in parameter <em>suiteDate</em>, eg: <em>Automation 2014-12-09</em>  <em>suitePerDay=false</em> - the newly created Test Run will be located under <em>Automation Test Suite</em>  <strong>IMPORTANT:</strong> In case you update an existing Test Run, its Test Suite remains unchanged (optional)
suite_date = 'suite_date_example' # str | It is required if <em>suitePerDay</em> is true. Its format is <em>\"yyyymmdd\"</em>.   The newly created Test Run will be located under a Test Suite named \"Automation yyyy-mm-dd\", eg: Automation 2014-12-09 (optional)
encode_note = true # bool | Specify if the Test Log's Notes are in HTML format  <em>encodeNote=true</em> - default value. Notes are not in HTML format  <em>encodeNote=false:</em> Notes are in HTML format (optional)
force_update_version = true # bool |  (optional)
user_id = 'user_id_example' # str |  (optional)

try: 
    # Submits an Automation Test Log
    api_response = api_instance.submit_automation_log(project_id, body, test_run_id, suite_per_day=suite_per_day, suite_date=suite_date, encode_note=encode_note, force_update_version=force_update_version, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestlogApi->submit_automation_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **body** | [**AutomationTestLogResource**](AutomationTestLogResource.md)| &lt;em&gt;status (required):&lt;/em&gt; automation status values which are mapped in qTest Manager&#39;s Automation Settings  &lt;em&gt;exe_start_date (required):&lt;/em&gt; the execution&#39;s starting time  &lt;em&gt;exe_end_date (required)&lt;/em&gt; the execution&#39;s ending time  &lt;em&gt;name (required)&lt;/em&gt; name of the Test Run or Test Case  &lt;em&gt;automation_content (required):&lt;/em&gt; a string that uniquely identifies an Automation Test Case  &lt;em&gt;attachments:&lt;/em&gt; a JSONArray of Attachment objects  &lt;em&gt;note:&lt;/em&gt; execution note  &lt;em&gt;test_case_version_id:&lt;/em&gt; ID of the associated Test Case&#39;s version  &lt;em&gt;test_step_logs:&lt;/em&gt; a JSONArray of TestStepLog objects | 
 **test_run_id** | **int**| ID of the Test Run  1/ If it is greater than 0 (zero), test result will be submitted to the specific Test Run  If it is 0 (zero), test result will be submitted to a new Test Run | 
 **suite_per_day** | **str**| &lt;em&gt;suitePerDay&#x3D;true&lt;/em&gt; - the newly created Test Run will be located under a Test Suite named under the execution date specified in parameter &lt;em&gt;suiteDate&lt;/em&gt;, eg: &lt;em&gt;Automation 2014-12-09&lt;/em&gt;  &lt;em&gt;suitePerDay&#x3D;false&lt;/em&gt; - the newly created Test Run will be located under &lt;em&gt;Automation Test Suite&lt;/em&gt;  &lt;strong&gt;IMPORTANT:&lt;/strong&gt; In case you update an existing Test Run, its Test Suite remains unchanged | [optional] 
 **suite_date** | **str**| It is required if &lt;em&gt;suitePerDay&lt;/em&gt; is true. Its format is &lt;em&gt;\&quot;yyyymmdd\&quot;&lt;/em&gt;.   The newly created Test Run will be located under a Test Suite named \&quot;Automation yyyy-mm-dd\&quot;, eg: Automation 2014-12-09 | [optional] 
 **encode_note** | **bool**| Specify if the Test Log&#39;s Notes are in HTML format  &lt;em&gt;encodeNote&#x3D;true&lt;/em&gt; - default value. Notes are not in HTML format  &lt;em&gt;encodeNote&#x3D;false:&lt;/em&gt; Notes are in HTML format | [optional] 
 **force_update_version** | **bool**|  | [optional] 
 **user_id** | **str**|  | [optional] 

### Return type

[**AutomationTestLogResource**](AutomationTestLogResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_automation_test_logs**
> QueueProcessingResponse submit_automation_test_logs(project_id, body, type, test_run_id, escape_xml=escape_xml, user_id=user_id)

Submits multiple test results

To submit Automation Test Logs of multiple Test Runs  <strong>qTest Manager version:</strong> 8.0.2+

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
api_instance = swagger_client.TestlogApi()
project_id = 789 # int | ID of the project
body = swagger_client.AutomationRequest() # AutomationRequest | <em>test_suite:</em> ID of the Test Suite where the submitted Test Runs will be located  <em>parent_module:</em> In case there has been no Test Case associated with the submitted Test Run, a new automation Test Case will be created. The new Test Cases are located under a module named <em>Automation</em>. If you specify an ID for parent_module, the <em>Automation</em> module will be located under the specified module. Otherwise, the <em>Automation</em> module is located directly under root  <em>execution_date (required):</em> Execution date in <em>YYYY-mm-dd</em> format  <em>test_logs (required):</em> The array of TestLog objects. The below are TestLog attributes  <em>status (required):</em> The automation result values that were mapped with Test Run Result in qTest automation settings  <em>exe_start_date (required):</em> Execution start time  <em>exe_end_date (required):</em> Execution end time  <em>name (required):</em> Test Run name  <em>automation_content (required):</em> An XML formatted string that contains the class test/ group test/ package test  <em>attachments:</em> An array of the Attachment objects  <em>note:</em> Test Log note  <em>test_step_logs:</em> An of TestStepLog objects. You can specify Test Steps' order in the requrest. It must be continous series of numbers, starting from zero, or it will throw an error. The order will be used when the Test Case is created or updated in qTest. If the order is omitted, Test Steps will be alphabetically sorted when creating or updating Test Case
type = 'type_example' # str | Always input <em>automation</em> for this parameter
test_run_id = 789 # int | This should always be <strong>0 (zero)</strong> or else it will throw an exception
escape_xml = false # bool | <em>escapeXml=true</em> - default value. &gt and &lt in <em>Automation Content</em> field are encoded  <em>escapeXml=false</em> - the Automation Content field is not encoded (optional) (default to false)
user_id = 'user_id_example' # str |  (optional)

try: 
    # Submits multiple test results
    api_response = api_instance.submit_automation_test_logs(project_id, body, type, test_run_id, escape_xml=escape_xml, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestlogApi->submit_automation_test_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **body** | [**AutomationRequest**](AutomationRequest.md)| &lt;em&gt;test_suite:&lt;/em&gt; ID of the Test Suite where the submitted Test Runs will be located  &lt;em&gt;parent_module:&lt;/em&gt; In case there has been no Test Case associated with the submitted Test Run, a new automation Test Case will be created. The new Test Cases are located under a module named &lt;em&gt;Automation&lt;/em&gt;. If you specify an ID for parent_module, the &lt;em&gt;Automation&lt;/em&gt; module will be located under the specified module. Otherwise, the &lt;em&gt;Automation&lt;/em&gt; module is located directly under root  &lt;em&gt;execution_date (required):&lt;/em&gt; Execution date in &lt;em&gt;YYYY-mm-dd&lt;/em&gt; format  &lt;em&gt;test_logs (required):&lt;/em&gt; The array of TestLog objects. The below are TestLog attributes  &lt;em&gt;status (required):&lt;/em&gt; The automation result values that were mapped with Test Run Result in qTest automation settings  &lt;em&gt;exe_start_date (required):&lt;/em&gt; Execution start time  &lt;em&gt;exe_end_date (required):&lt;/em&gt; Execution end time  &lt;em&gt;name (required):&lt;/em&gt; Test Run name  &lt;em&gt;automation_content (required):&lt;/em&gt; An XML formatted string that contains the class test/ group test/ package test  &lt;em&gt;attachments:&lt;/em&gt; An array of the Attachment objects  &lt;em&gt;note:&lt;/em&gt; Test Log note  &lt;em&gt;test_step_logs:&lt;/em&gt; An of TestStepLog objects. You can specify Test Steps&#39; order in the requrest. It must be continous series of numbers, starting from zero, or it will throw an error. The order will be used when the Test Case is created or updated in qTest. If the order is omitted, Test Steps will be alphabetically sorted when creating or updating Test Case | 
 **type** | **str**| Always input &lt;em&gt;automation&lt;/em&gt; for this parameter | 
 **test_run_id** | **int**| This should always be &lt;strong&gt;0 (zero)&lt;/strong&gt; or else it will throw an exception | 
 **escape_xml** | **bool**| &lt;em&gt;escapeXml&#x3D;true&lt;/em&gt; - default value. &amp;gt and &amp;lt in &lt;em&gt;Automation Content&lt;/em&gt; field are encoded  &lt;em&gt;escapeXml&#x3D;false&lt;/em&gt; - the Automation Content field is not encoded | [optional] [default to false]
 **user_id** | **str**|  | [optional] 

### Return type

[**QueueProcessingResponse**](QueueProcessingResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_automation_test_logs_0**
> QueueProcessingResponse submit_automation_test_logs_0(project_id, body, type, escape_xml=escape_xml, user_id=user_id)

Submits multiple test results and specifies Test Design and Test Execution tree structures

This is the extended version of this API <strong>POST /api/v3.1/projects/{projectId}/test-runs/{testRunId}/auto-test-logs</strong>. It allows submitting multiple test logs in one API request, and creating Test Cases and Test Runs in hierarchical structure which is specified in the request body  <strong>Important:</strong> This API does not update names and locations of existing Test Cases and Test Runs

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
api_instance = swagger_client.TestlogApi()
project_id = 789 # int | ID of the project
body = swagger_client.AutomationRequest() # AutomationRequest | <em>test_cycle (required):</em> PID or ID of the parent Test Cycle in qTest Manager where submitted Test Runs will be located  <em>test_logs (required):</em> The array of TestLog objects. The below are TestLog attributes  <strong>TestLog attributes:</strong>  - <em>test_case_version_id:</em> ID of the associated Test Case's version. In case the Test Run has not existed, this field should not be included or it will cause an error  - <em>status (required):</em> The automation result values that were mapped with Test Run Result in qTest automation settings  - <em>exe_start_date (required):</em> Execution start time  - <em>exe_end_date (required):</em> Execution end time  - <em>module_names (required):</em> an array of folder names which will be used when creating hierarchical structure in Test Design and Test Execution trees. In Test Design tree, the first folder will be created as a Module directly under the tree root. Other folders will be created as sub-Modules under their preceding folders in the array. In Test Execution tree, the first folder will be created as a Test Cycle directly under the parent Test Cycle which is specified in the API request. Other folders will be created as sub Test Cycles under their preceding folders in the array. If there is a folder in the tree with matching name and location, the API will not create a duplicate one  - <em>name (required):</em> It will be used when <em>creating</em> Test Cases and Test Runs as their names. It will not be used for updating Test Case and Test Run names  - <em>automation_content (required):</em> Specify a unique string to each Test Case. It acts as Test Case fingerprint. Before adding a Test Log, qTest Manager will look up Automation Content of existing Test Cases. If it can find an existing Test Case, the Test Log will be associated with that Test Case. Otherwise, a new Test Case will be created with the submitted Test Log. It is also be used when creating Test Runs. If qTest Manager finds an existing Test Run with matching Automation Content and location in Test Execution tree, it will not create a duplicate one. If there is an existing Test Run with matching Automation Content but it is located in different Test Cycles, qTest Manager will create a new Test Run in the specified folder  - <em>attachments:</em> an array of the Attachment objects  - <em>test_step_logs:</em> an array of TestStepLog objects. You can specify Test Steps' order in the request. It must be continous series of numbers, starting from zero, or it will throw an error. The order will be used when the Test Case is created or updated in qTest. If the order is omitted, Test Steps will be alphabetically sorted when creating or updating Test Case  <strong>Test Step Log attributes</strong>  - <em>description (required):</em> Description of the Test Step  - <em>expected_result (required):</em> Expected result of the Test Step  - <em>actual_result (required):</em> Actual result of the Test Step  - <em>status (required):</em> The automation result values that were mapped with Test Run Result in qTest automation settings  - <em>order:</em> Specify the order of Test Steps. It must be continous series of numbers, starting from zero, or it will throw an error. The order will be used when the Test Case is created or updated in qTest. If the order is omitted, Test Steps will be alphabetically sorted when creating or updating Test Case
type = 'type_example' # str | always use <em>type=automation</em> for this parameter
escape_xml = true # bool | <em>escapeXml=true</em> - default value. &gt and &lt in <em>Automation Content</em> field are encoded  <em>escapeXml=false</em> - the Automation Content field is not encoded (optional)
user_id = 'user_id_example' # str |  (optional)

try: 
    # Submits multiple test results and specifies Test Design and Test Execution tree structures
    api_response = api_instance.submit_automation_test_logs_0(project_id, body, type, escape_xml=escape_xml, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestlogApi->submit_automation_test_logs_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **body** | [**AutomationRequest**](AutomationRequest.md)| &lt;em&gt;test_cycle (required):&lt;/em&gt; PID or ID of the parent Test Cycle in qTest Manager where submitted Test Runs will be located  &lt;em&gt;test_logs (required):&lt;/em&gt; The array of TestLog objects. The below are TestLog attributes  &lt;strong&gt;TestLog attributes:&lt;/strong&gt;  - &lt;em&gt;test_case_version_id:&lt;/em&gt; ID of the associated Test Case&#39;s version. In case the Test Run has not existed, this field should not be included or it will cause an error  - &lt;em&gt;status (required):&lt;/em&gt; The automation result values that were mapped with Test Run Result in qTest automation settings  - &lt;em&gt;exe_start_date (required):&lt;/em&gt; Execution start time  - &lt;em&gt;exe_end_date (required):&lt;/em&gt; Execution end time  - &lt;em&gt;module_names (required):&lt;/em&gt; an array of folder names which will be used when creating hierarchical structure in Test Design and Test Execution trees. In Test Design tree, the first folder will be created as a Module directly under the tree root. Other folders will be created as sub-Modules under their preceding folders in the array. In Test Execution tree, the first folder will be created as a Test Cycle directly under the parent Test Cycle which is specified in the API request. Other folders will be created as sub Test Cycles under their preceding folders in the array. If there is a folder in the tree with matching name and location, the API will not create a duplicate one  - &lt;em&gt;name (required):&lt;/em&gt; It will be used when &lt;em&gt;creating&lt;/em&gt; Test Cases and Test Runs as their names. It will not be used for updating Test Case and Test Run names  - &lt;em&gt;automation_content (required):&lt;/em&gt; Specify a unique string to each Test Case. It acts as Test Case fingerprint. Before adding a Test Log, qTest Manager will look up Automation Content of existing Test Cases. If it can find an existing Test Case, the Test Log will be associated with that Test Case. Otherwise, a new Test Case will be created with the submitted Test Log. It is also be used when creating Test Runs. If qTest Manager finds an existing Test Run with matching Automation Content and location in Test Execution tree, it will not create a duplicate one. If there is an existing Test Run with matching Automation Content but it is located in different Test Cycles, qTest Manager will create a new Test Run in the specified folder  - &lt;em&gt;attachments:&lt;/em&gt; an array of the Attachment objects  - &lt;em&gt;test_step_logs:&lt;/em&gt; an array of TestStepLog objects. You can specify Test Steps&#39; order in the request. It must be continous series of numbers, starting from zero, or it will throw an error. The order will be used when the Test Case is created or updated in qTest. If the order is omitted, Test Steps will be alphabetically sorted when creating or updating Test Case  &lt;strong&gt;Test Step Log attributes&lt;/strong&gt;  - &lt;em&gt;description (required):&lt;/em&gt; Description of the Test Step  - &lt;em&gt;expected_result (required):&lt;/em&gt; Expected result of the Test Step  - &lt;em&gt;actual_result (required):&lt;/em&gt; Actual result of the Test Step  - &lt;em&gt;status (required):&lt;/em&gt; The automation result values that were mapped with Test Run Result in qTest automation settings  - &lt;em&gt;order:&lt;/em&gt; Specify the order of Test Steps. It must be continous series of numbers, starting from zero, or it will throw an error. The order will be used when the Test Case is created or updated in qTest. If the order is omitted, Test Steps will be alphabetically sorted when creating or updating Test Case | 
 **type** | **str**| always use &lt;em&gt;type&#x3D;automation&lt;/em&gt; for this parameter | 
 **escape_xml** | **bool**| &lt;em&gt;escapeXml&#x3D;true&lt;/em&gt; - default value. &amp;gt and &amp;lt in &lt;em&gt;Automation Content&lt;/em&gt; field are encoded  &lt;em&gt;escapeXml&#x3D;false&lt;/em&gt; - the Automation Content field is not encoded | [optional] 
 **user_id** | **str**|  | [optional] 

### Return type

[**QueueProcessingResponse**](QueueProcessingResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_test_log**
> TestLogResource submit_test_log(project_id, body, test_run_id)

Submits a Manual Test Log

To submit test result of a <em>manual</em> Test Run  <strong>qTest Manager version:</strong> 4+

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
api_instance = swagger_client.TestlogApi()
project_id = 789 # int | ID of the project
body = swagger_client.TestLogResource() # TestLogResource | <em>status (required):</em> Status of the Test Log as defined in the project's Field Settings  <em>test_case_version_id:</em> ID of the associated Test Case's version.    If it is omitted, the submitted Test Log will be associated with the Test Case's latest approved version  <em>exe_start_date (required):</em> time when the test is executed  <em>exe_end_date (required):</em> time when the test is finished  <em>attachments:</em> the Test Log's attachments  <em>test_step_logs:</em >
test_run_id = 789 # int | ID of the Test Run

try: 
    # Submits a Manual Test Log
    api_response = api_instance.submit_test_log(project_id, body, test_run_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestlogApi->submit_test_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of the project | 
 **body** | [**TestLogResource**](TestLogResource.md)| &lt;em&gt;status (required):&lt;/em&gt; Status of the Test Log as defined in the project&#39;s Field Settings  &lt;em&gt;test_case_version_id:&lt;/em&gt; ID of the associated Test Case&#39;s version.    If it is omitted, the submitted Test Log will be associated with the Test Case&#39;s latest approved version  &lt;em&gt;exe_start_date (required):&lt;/em&gt; time when the test is executed  &lt;em&gt;exe_end_date (required):&lt;/em&gt; time when the test is finished  &lt;em&gt;attachments:&lt;/em&gt; the Test Log&#39;s attachments  &lt;em&gt;test_step_logs:&lt;/em &gt; | 
 **test_run_id** | **int**| ID of the Test Run | 

### Return type

[**TestLogResource**](TestLogResource.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **track**
> QueueProcessingResponse track(id)

Gets a Batch Test Log Submission job's state

To check the state of a Batch Test Log Submission job.   When you submit test results to qTest Manager using:  <strong>POST /api/v3.1/projects/{projectId}/test-runs/{testRunId}/auto-test-logs?type=automation</strong>  or <strong>POST /api/v3/projects/{projectId}/auto-test-logs?type=automation</strong>, their response include a job ID.  You will need to use this API and the returned ID to check if the submission job has completed.  Job states include <i>IN_WAITING</i>, <i>IN_PROCESSING</i>, <i>FAILED</i>, <i>PENDING</i> and <i>SUCCESS</i>

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
api_instance = swagger_client.TestlogApi()
id = 789 # int | The ID of the submission job.   It is included in the response of these 2 APIs:  <strong>POST /api/v3.1/projects/{projectId}/test-runs/{testRunId}/auto-test-logs?type=automation</strong>   or <strong>POST /api/v3/projects/{projectId}/auto-test-logs?type=automation</strong>

try: 
    # Gets a Batch Test Log Submission job's state
    api_response = api_instance.track(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestlogApi->track: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the submission job.   It is included in the response of these 2 APIs:  &lt;strong&gt;POST /api/v3.1/projects/{projectId}/test-runs/{testRunId}/auto-test-logs?type&#x3D;automation&lt;/strong&gt;   or &lt;strong&gt;POST /api/v3/projects/{projectId}/auto-test-logs?type&#x3D;automation&lt;/strong&gt; | 

### Return type

[**QueueProcessingResponse**](QueueProcessingResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

