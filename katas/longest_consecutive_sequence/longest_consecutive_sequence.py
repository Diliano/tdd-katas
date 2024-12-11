def longest_consecutive_sequence(nums):
    """
    Finds the length of the longest consecutive sequence in a list of integers

    Approach:
    1) Remove duplicates by converting the list to a set
    2) Iterate through the set, identifying the start of each sequence
        - A number is the start of a sequence if `num - 1` is not in the set
    3) For each sequence, count its length by checking for consecutive numbers
    4) Track the longest sequence length and update it as required
    """
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
