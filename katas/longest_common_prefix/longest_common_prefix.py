def longest_common_prefix(strs):
    if len(strs) == 1:
        return strs[0]

    result = []

    for chars in zip(*strs):
        if all(char == chars[0] for char in chars):
            result.append(chars[0])
        else:
            break

    return "".join(result)
