#!/usr/bin/env python3
"""Role-based access control demonstration."""

ROLES = {
    "guest": {"read_public"},
    "student": {"read_public", "read_own_profile", "submit_ticket"},
    "admin": {"read_public", "read_own_profile", "submit_ticket", "read_all_profiles", "delete_ticket"},
}

USERS = {
    "alice": {"role": "student", "profile_id": "alice"},
    "bob": {"role": "student", "profile_id": "bob"},
    "chen": {"role": "admin", "profile_id": "chen"},
    "visitor": {"role": "guest", "profile_id": None},
}


def has_permission(username, action, resource_owner=None):
    user = USERS[username]
    permissions = ROLES[user["role"]]

    if action in permissions:
        return True

    if action == "read_profile":
        if "read_all_profiles" in permissions:
            return True
        if "read_own_profile" in permissions and user["profile_id"] == resource_owner:
            return True

    return False


def run_tests():
    assert has_permission("alice", "read_public") is True
    assert has_permission("visitor", "submit_ticket") is False
    assert has_permission("alice", "read_profile", "alice") is True
    assert has_permission("alice", "read_profile", "bob") is False
    assert has_permission("chen", "read_profile", "bob") is True
    assert has_permission("bob", "delete_ticket") is False
    assert has_permission("chen", "delete_ticket") is True


def main():
    run_tests()
    checks = [
        ("visitor", "submit_ticket", None),
        ("alice", "read_profile", "alice"),
        ("alice", "read_profile", "bob"),
        ("chen", "read_profile", "bob"),
        ("bob", "delete_ticket", None),
        ("chen", "delete_ticket", None),
    ]

    for username, action, owner in checks:
        result = "allowed" if has_permission(username, action, owner) else "denied"
        print(f"{username} -> {action} ({owner or 'n/a'}): {result}")


if __name__ == "__main__":
    main()

