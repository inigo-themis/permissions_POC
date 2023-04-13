
import pytest
from permissions.actions import comment, edit, invite, view
from permissions.main import themi_actions


@pytest.mark.parametrize(
    "user, action, expected",
    [
        ("OWNER", comment, "comment"),
        ("OWNER", view, "view"),
        ("OWNER", edit, "edit"),
        ("OWNER", invite, "invite"),
        ("EDITOR", comment, "comment"),
        ("EDITOR", view, "view"),
        ("EDITOR", edit, "edit"),
        ("EDITOR", invite, "invite"),
        ("COMMENTER", comment, "comment"),
        ("COMMENTER", view, "view"),
        ("VIEWER", view, "view"),
    ],
)
def test_roles_allowed_actions(user, action, expected):
    assert themi_actions(user, action) == expected


@pytest.mark.parametrize(
    "user, action",
    [
        ("OWNER", callable(1)),
        ("COMMENTER", invite),
        ("VIEWER", edit),
    ],
)
def test_roles_forbidden_actions(user, action):
    assert themi_actions(user, action) is None


@pytest.mark.parametrize("user",
                         [None, "MADE_UP_ROLE"])
def test_exception_no_user_provided(user):
    with pytest.raises(Exception):
        themi_actions(user)