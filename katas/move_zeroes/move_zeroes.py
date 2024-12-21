def move_zeroes(nums):
    if not nums:
        return []

    set_nums = set(nums)

    if 0 not in set_nums:
        return nums

    if len(set_nums) == 1 and set_nums == {0}:
        return nums
