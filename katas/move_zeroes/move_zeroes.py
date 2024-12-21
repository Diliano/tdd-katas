def move_zeroes(nums):
    if not nums:
        return []

    set_nums = set(nums)

    if 0 not in set_nums:
        return nums
