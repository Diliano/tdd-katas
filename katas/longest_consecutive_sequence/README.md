# Longest Consecutive Sequence

## Problem Statement
Write a function that takes a list of integers and returns the length of the longest sequence of consecutive numbers. The sequence does not need to be contiguous in the original list, but the numbers must appear in order.

If the list is empty, return `0`.

## Example Input/Output
| Input                        | Output |
|------------------------------|--------|
| `[100, 4, 200, 1, 3, 2]`     | `4`    |
| `[10, 5, 12, 3, 55, 11]`     | `3`    |
| `[1, 2, 0, 1]`               | `3`    |
| `[]`                         | `0`    |

## Edge Cases
1. Empty list → Output should be `0`.
2. List with one number → Output should be `1`.
3. List with no consecutive sequence (e.g., `[10, 20, 30]`) → Output should be `1`.

