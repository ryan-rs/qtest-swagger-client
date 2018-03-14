# CommentQueryParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **datetime** | StartDate with format: yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ or yyyy-MM-dd&#39;T&#39;HH:mm:ssZZ\&quot; | [optional] 
**end** | **datetime** | EndDate with format: yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ or yyyy-MM-dd&#39;T&#39;HH:mm:ssZZ\&quot; | [optional] 
**object_type** | **str** | Only support comments for object types: [requirements, defects, test-cases, test-runs] | 
**fields** | **list[str]** | Specify which object fields you want to include in the response. If you omit it or specify an asterisk (*), all fields are included | [optional] 
**object** | **int** | Id of the object from which you want to retrieve comments | [optional] 
**author** | **int** | Id of the user who made the comments | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


