def sum_of_digits(num):
    if num < 10:
        return num

    digit_sum = 0

    while num != 0:
        digit_sum += num % 10
        num //= 10

    return digit_sum
