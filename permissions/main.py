from typing import Optional, Callable
from permissions.roles_logic import ROLES, has_permission


def themi_actions(user: str, action: Callable, user2: Optional[str] = None):
    role1 = ROLES.get(user)
    if role1 is None:
        raise Exception()
    role2 = ROLES.get(user2)
    if has_permission(role1, action, role2):
        return action()
