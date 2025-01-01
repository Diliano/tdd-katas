def is_isomorphic(s1, s2):
    """
    Determines if two string are isomorphic

    Approach:
    1) If the strings have different lengths:
        - Return False
    2) Use two dictionaries to track mappings:
        - s1_char -> s2_char
        - s2_char -> s1_char
    3) Iterate over both strings:
        - If a character mapping conflict is found, return False
    4) If no conflicts are found after iteration:
        - Return True
    """
    if len(s1) != len(s2):
        return False

    s1_mappings = {}
    s2_mappings = {}

    for s1_c, s2_c in zip(s1, s2):
        if (s1_c in s1_mappings and s1_mappings[s1_c] != s2_c) or (
            s1_c not in s1_mappings and s2_c in s2_mappings
        ):
            return False

        s1_mappings[s1_c] = s2_c
        s2_mappings[s2_c] = s1_c

    return True
