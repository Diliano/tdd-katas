def move_zeroes(nums):
    set_nums = set(nums)
    empty = not nums
    no_zeroes = 0 not in set_nums
    only_zeroes = len(set_nums) == 1 and set_nums == {0}

    if empty or no_zeroes or only_zeroes:
        return nums
