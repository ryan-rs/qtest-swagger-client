# LoggedUser

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**list[Link]**](Link.md) |  | [optional] 
**id** | **int** | ID of the User | [optional] 
**user_name** | **str** | Login email of the User | [optional] 
**first_name** | **str** | First name | [optional] 
**last_name** | **str** | Last name | [optional] 
**client_id** | **int** | ID of qTest site that User logged in | [optional] 
**client_name** | **str** | qTest instance client site name | [optional] 
**client_site** | **str** | URL of qTest instance | [optional] 
**timezone_offset** | **str** | Timezone setting of User | [optional] 
**avatar** | **str** | URL to User&#39;s Avatar | [optional] 
**access_admin_page** | **bool** | Can access admin page or not | [optional] [default to False]
**client_site_name** | **str** | qTest instance sub domain name | [optional] 
**package_type** | **str** | Package type | [optional] 
**applications** | [**list[AppDetail]**](AppDetail.md) | List qTest products which User can access | [optional] 
**support_links** | **dict(str, str)** | Arrays of Supports link | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


