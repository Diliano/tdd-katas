# Convert to Upper Camel Case

## Problem Statement
Write a function that takes a string of words separated by spaces and returns the string in "UpperCamelCase" format. Upper Camel Case means:
- The first letter of each word is capitalised.
- All words are joined together without spaces.

If the input string is empty or contains only spaces, return an empty string.

## Example Input/Output
| Input                      | Output                 |
|----------------------------|------------------------|
| `"hello world"`            | `"HelloWorld"`         |
| `"convert to upper case"`  | `"ConvertToUpperCase"` |
| `"    "`                   | `""`                   |
| `"Python"`                 | `"Python"`             |

## Edge Cases
1. Input string is empty → Output should be `""`.
2. Input string contains only spaces → Output should be `""`.
3. Input string has a single word → The word should be returned with the first letter capitalised.

