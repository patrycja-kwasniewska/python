def sum_of_digits(number):
    return sum(int(digit) for digit in str(abs(number)))


def factorial(number):
    if number < 0:
        raise ValueError("Silnia nie jest zdefiniowana dla liczb ujemnych.")
    result = 1
    for i in range(2, number + 1):
        result *= i
    return result