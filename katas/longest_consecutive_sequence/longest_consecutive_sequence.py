def longest_consecutive_sequence(nums):
    if not nums:
        return 0

    nums = set(nums)

    longest_seq = 1

    for num in nums:
        if num - 1 not in nums:
            current_num = num
            current_seq = 1
            while current_num + 1 in nums:
                current_seq += 1
                current_num += 1
            longest_seq = max(current_seq, longest_seq)

    return longest_seq
