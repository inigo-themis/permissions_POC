from typing import Optional, Callable

from permissions.actions import comment, edit, invite, view

ROLES = {"OWNER": 0, "EDITOR": 1, "COMMENTER": 2, "VIEWER": 99}
PERMISSIONS = {0: {view, edit, comment, invite},
               1: {view, edit, comment, invite},
               2: {view, comment},
               99: {view}}


def hierarchy_check(role1: int, role2: int) -> bool:
    # If action affects other user, compare roles to verify hierarchy is respected
    return (role2 == None) or (role1 <= role2)

def check_permission(role1: int, action: Callable) -> bool:
    return action in PERMISSIONS[role1]

def has_permission(role1: int, action: Callable, role2: Optional[int] = None) -> bool:
    return  hierarchy_check(role1, role2) and check_permission(role1, action)