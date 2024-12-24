from collections import Counter


def first_non_repeating_character(s):
    if not s or len(s) == 1:
        return s

    counter = Counter(s)

    if all(counter[count] > 1 for count in counter):
        return ""

    for c in s:
        if counter[c] == 1:
            return c
