def longest_consecutive_sequence(nums):
    if not nums:
        return 0

    if len(nums) == 1:
        return 1

    for i in range(1, len(nums)):
        if nums[i] != (nums[i - 1] + 1):
            return 1
