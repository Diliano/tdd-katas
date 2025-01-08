def longest_common_prefix(strs):
    """
    Finds the longest common prefix among a list of strings

    Approach:
    1) If the list contains only one string:
        - Return the string
    2) Use zip() to compare characters at each position across all strings
    3) If all characters match at a position:
        - Add the character to the result
    4) Stop when a mismatch is found or iteration is complete
    5) Return the accumulated result as a string
    """
    if len(strs) == 1:
        return strs[0]

    result = []

    for chars in zip(*strs):
        if all(char == chars[0] for char in chars):
            result.append(chars[0])
        else:
            break

    return "".join(result)
