from collections import Counter


def first_non_repeating_character(s):
    """
    Returns the first non-repeating character in a string

    Approach:
    1) If the string is empty or has only one character:
        - Return the string
    2) Use `Counter` to count occurences of each character
    3) Iterate through the string:
        - Return the first character with a count of 1
    4) If a non-repeating character is not found:
        - Return an empty string
    """
    if not s or len(s) == 1:
        return s

    counter = Counter(s)

    for c in s:
        if counter[c] == 1:
            return c

    return ""
