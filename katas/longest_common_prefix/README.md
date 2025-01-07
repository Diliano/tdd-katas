# Longest Common Prefix

## Problem Statement
Write a function to find the longest common prefix among an array of strings.  

If there is no common prefix, return an empty string `""`.  

## Example Input/Output
| Input                                 | Output    |
|---------------------------------------|-----------|
| ["flower", "flow", "flight"]          | "fl"      |
| ["dog", "racecar", "car"]             | ""        |
| ["interview", "internet", "internal"] | "inter"   |
| ["apple", "ape", "april"]             | "ap"      |

### **Edge Cases**:
1. **Empty Input** – If the input list is empty, return `""`.  
2. **Single Word** – If the array has only one string, return that string.  
3. **No Common Prefix** – If no two strings share a common prefix, return `""`. 