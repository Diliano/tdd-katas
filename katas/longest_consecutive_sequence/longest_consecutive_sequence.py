def longest_consecutive_sequence(nums):
    if not nums:
        return 0

    nums.sort()
    consecutive_seq_len = 1

    for i in range(1, len(nums)):
        if nums[i] == (nums[i - 1] + 1):
            consecutive_seq_len += 1

    return consecutive_seq_len
