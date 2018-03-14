# AutomationTestLogResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**list[Link]**](Link.md) |  | [optional] 
**id** | **int** |  | [optional] 
**test_case_version_id** | **int** | ID of the Test Case Version | [optional] 
**exe_start_date** | **datetime** | Execution start date | 
**exe_end_date** | **datetime** | Execution end date | 
**note** | **str** | Note | [optional] 
**attachments** | [**list[AttachmentResource]**](AttachmentResource.md) | Test Log attachments | [optional] 
**automation_content** | **str** | Test Case&#39;s automation content | [optional] 
**name** | **str** | Test Run&#39;s name | [optional] 
**test_case** | [**TestCaseWithCustomFieldResource**](TestCaseWithCustomFieldResource.md) | Test Case object | [optional] 
**defects** | [**list[LinkedDefectResource]**](LinkedDefectResource.md) | Array of Defect | [optional] 
**planned_exe_time** | **int** |  | [optional] 
**actual_exe_time** | **int** |  | [optional] 
**build_number** | **str** | Jenkins jobs build number | [optional] 
**build_url** | **str** | Jenkin jobs build URL | [optional] 
**properties** | [**list[PropertyResource]**](PropertyResource.md) |  | [optional] 
**system_name** | **str** |  | [optional] 
**status** | **str** | Test Log status | [optional] 
**order** | **int** |  | [optional] 
**test_step_logs** | [**list[AutomationTestStepLog]**](AutomationTestStepLog.md) | Arrays of Test Step Log | [optional] 
**module_names** | **list[str]** | Arrays of Modules | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


