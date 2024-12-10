def longest_consecutive_sequence(nums):
    if not nums:
        return 0

    nums.sort()
    current, longest = 1, 1

    for i in range(1, len(nums)):
        if nums[i] == (nums[i - 1] + 1):
            current += 1
        else:
            if current > longest:
                longest = current
            current = 1

    if current > longest:
        longest = current

    return longest
