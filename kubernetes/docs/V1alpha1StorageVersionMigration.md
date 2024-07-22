# V1alpha1StorageVersionMigration

StorageVersionMigration represents a migration of stored data to the latest storage version.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**spec** | [**V1alpha1StorageVersionMigrationSpec**](V1alpha1StorageVersionMigrationSpec.md) |  | [optional] 
**status** | [**V1alpha1StorageVersionMigrationStatus**](V1alpha1StorageVersionMigrationStatus.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1alpha1_storage_version_migration import V1alpha1StorageVersionMigration

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1StorageVersionMigration from a JSON string
v1alpha1_storage_version_migration_instance = V1alpha1StorageVersionMigration.from_json(json)
# print the JSON string representation of the object
print V1alpha1StorageVersionMigration.to_json()

# convert the object into a dict
v1alpha1_storage_version_migration_dict = v1alpha1_storage_version_migration_instance.to_dict()
# create an instance of V1alpha1StorageVersionMigration from a dict
v1alpha1_storage_version_migration_form_dict = v1alpha1_storage_version_migration.from_dict(v1alpha1_storage_version_migration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

