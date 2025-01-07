def longest_common_prefix(strs):
    if not strs:
        return []

    if len(strs) == 1:
        return strs[0]
