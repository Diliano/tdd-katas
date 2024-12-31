# Isomorphic Strings

## Problem Statement
Write a function to determine if two strings are **isomorphic**.

Two strings are isomorphic if the characters in one string can be replaced to get the second string.  
- No two characters may map to the same character, but a character may map to itself.

## Example Input/Output
| Input                   | Output |
|-------------------------|--------|
| "egg", "add"            | True   |
| "foo", "bar"            | False  |
| "paper", "title"        | True   |
| "ab", "aa"              | False  |

## Edge Cases
1. If the strings are different lengths → Return `False`.  
2. Empty strings → Consider them isomorphic, return `True`.