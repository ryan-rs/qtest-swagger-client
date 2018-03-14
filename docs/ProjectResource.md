# ProjectResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**list[Link]**](Link.md) |  | [optional] 
**id** | **int** | ID of the Project | [optional] 
**name** | **str** | Name of the Project | [optional] 
**description** | **str** | Description of the Project | [optional] 
**status_id** | **int** | Status of the Project | [optional] 
**start_date** | **datetime** | Start date of the Project | [optional] 
**end_date** | **datetime** | End date of the Project | [optional] 
**admins** | **list[str]** | Arrays of admin user | [optional] 
**sample** | **bool** | Is sample or not | [optional] [default to False]
**user_profile** | [**UserProfile**](UserProfile.md) | Arrays of User Profile in Project | [optional] 
**defect_tracking_systems** | [**list[DefectTrackingSystem]**](DefectTrackingSystem.md) | Arrays of External Defect Tracking Connection | [optional] 
**x_explorer_access_level** | **int** | Can access Explorer | [optional] 
**date_format** | **str** | Client date time format | [optional] 
**automation** | **bool** | Automation enabled or not | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


