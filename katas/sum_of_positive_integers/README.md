# Sum of Positive Integers

## Problem Statement
Write a function that takes a list of integers and returns the sum of all positive numbers in the list. If there are no positive numbers, or the list is empty, return `0`.

## Example Input/Output
| Input                   | Output |
|-------------------------|--------|
| `[1, 2, 3, 4, 5]`       | `15`   |
| `[-1, -2, -3, -4, -5]`  | `0`    |
| `[-1, 2, -3, 4, 5]`     | `11`   |
| `[]`                    | `0`    |

## Edge Cases
1. Input list is empty → Output should be `0`.
2. Input list contains all negative numbers → Output should be `0`.