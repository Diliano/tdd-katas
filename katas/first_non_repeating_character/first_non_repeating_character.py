from collections import Counter


def first_non_repeating_character(s):
    if not s or len(s) == 1:
        return s

    counter = Counter(s)

    for c in s:
        if counter[c] == 1:
            return c
