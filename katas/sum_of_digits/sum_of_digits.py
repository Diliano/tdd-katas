def sum_of_digits(num):
    """
    Calculates the sum of digits in a non-negative integer

    Approach:
    1) If the number has only one digit, return it
    2) Otherwise:
        - repeatedly extract the last digit using `num % 10`
        - add the extracted digit to a running total
        - remove the extracted digit using floor division `num //= 10`
    """
    if num < 10:
        return num

    digit_sum = 0

    while num != 0:
        digit_sum += num % 10
        num //= 10

    return digit_sum
