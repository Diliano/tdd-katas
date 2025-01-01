def is_isomorphic(s1, s2):
    if len(s1) != len(s2):
        return False

    s1_mappings = {}
    s2_mappings = {}

    for i in range(len(s1)):
        if s1[i] in s1_mappings and s1_mappings[s1[i]] != s2[i]:
            return False
        if s1[i] not in s1_mappings and s2[i] in s2_mappings:
            return False

        s1_mappings[s1[i]] = s2[i]
        s2_mappings[s2[i]] = s1[i]

    return True
