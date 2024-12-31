def is_isomorphic(s1, s2):
    if not s1 and not s2:
        return True

    if len(s1) != len(s2):
        return False
