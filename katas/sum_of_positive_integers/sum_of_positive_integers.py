def sum_of_positive_integers(nums):
    if not nums:
        return 0

    if all(num < 0 for num in nums):
        return 0

    return sum(nums)
