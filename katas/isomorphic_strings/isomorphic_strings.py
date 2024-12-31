def is_isomorphic(s1, s2):
    if not s1 and not s2:
        return True

    if len(s1) != len(s2):
        return False

    mappings = {}

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            mappings[s1[i]] = s2[i]

    return True
