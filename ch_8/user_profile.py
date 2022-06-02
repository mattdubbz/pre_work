def build_profile(first, last, **user_info):
    profile = {"first_name": first, "last_name": last}
    for key, val in user_info.items():
        profile[key] = val
    return profile


user_profile = build_profile("matt", "whisman", wife="jess", dog="boomer", cat="never")
print(user_profile)
