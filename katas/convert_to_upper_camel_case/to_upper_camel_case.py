def to_upper_camel_case(string):
    if not string or all(c == " " for c in string):
        return ""

    return string.capitalize()
