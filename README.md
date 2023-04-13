## POC for managing permissions
This POC tries to provide a solution to managing roles and permissions for workspaces and themis dinamically.

The idea is to implement a generic logic that can be used for all places in which permissions might be integrated and to leave the decision of which roles exist, the hierarchy and allowed actions to the users.

This POC only considers the basic setup, there would be other logic that needs to be implemented for this to be usable in production. For example:
- Allow users to create roles -> Even if a user has a role that allows them to edit access, they can't create a role with higher access level (The allowed actions and access level are known for each role)
- List possible roles and permissions
- Logic to update existing roles. Users need to be able to rearrange the hierarchy of roles and this changes should propagate
