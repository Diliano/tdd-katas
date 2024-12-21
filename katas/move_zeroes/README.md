# Move Zeroes

## Problem Statement
Write a function that takes a list of integers and moves all the zeroes to the end of the list while maintaining the order of the non-zero elements.

The function should modify the list in-place (i.e., without creating a new list).

## Example Input/Output
| Input                  | Output                |
|------------------------|-----------------------|
| `[0, 1, 0, 3, 12]`     | `[1, 3, 12, 0, 0]`    |
| `[0, 0, 1]`            | `[1, 0, 0]`           |
| `[1, 2, 3]`            | `[1, 2, 3]`           |
| `[0, 0, 0]`            | `[0, 0, 0]`           |

## Edge Cases
1. The input list is empty → Output should be an empty list.
2. The input list contains only zeroes.
3. The input list contains no zeroes.