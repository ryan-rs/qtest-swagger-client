# TestLogResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**list[Link]**](Link.md) |  | [optional] 
**id** | **int** |  | [optional] 
**test_case_version_id** | **int** |  | [optional] 
**exe_start_date** | **datetime** |  | 
**exe_end_date** | **datetime** |  | 
**note** | **str** |  | [optional] 
**attachments** | [**list[AttachmentResource]**](AttachmentResource.md) |  | [optional] 
**automation_content** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**test_case** | [**TestCaseWithCustomFieldResource**](TestCaseWithCustomFieldResource.md) |  | [optional] 
**defects** | [**list[LinkedDefectResource]**](LinkedDefectResource.md) |  | [optional] 
**planned_exe_time** | **int** |  | [optional] 
**actual_exe_time** | **int** |  | [optional] 
**build_number** | **str** |  | [optional] 
**build_url** | **str** |  | [optional] 
**properties** | [**list[PropertyResource]**](PropertyResource.md) |  | [optional] 
**status** | [**StatusResource**](StatusResource.md) |  | 
**result_number** | **int** |  | [optional] 
**test_step_logs** | [**list[TestStepLogResource]**](TestStepLogResource.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


