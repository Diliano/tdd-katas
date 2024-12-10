def longest_consecutive_sequence(nums):
    if not nums:
        return 0

    if len(nums) == 1:
        return 1
