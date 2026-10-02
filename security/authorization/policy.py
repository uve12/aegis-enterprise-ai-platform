def is_allowed(user_groups: list[str], allowed_groups: list[str]) -> bool:
    return bool(set(user_groups).intersection(set(allowed_groups)))
