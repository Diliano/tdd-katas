def move_zeroes(nums):
    """
    Moves all zeroes to the end of the list

    Approach:
    1) Use a pointer to track the position for the next non-zero
        - Starting at index 0
    2) Iterate through the list
        - If a zero is found, skip it
        - If a non-zero is found, swap it with the element at the pointer's position
    3) Increment the pointer after each swap
    """
    j = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1

    return nums
