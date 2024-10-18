#zad1
def mean_median(numbers):
    if not numbers:
        return None, None

    mean = sum(numbers) / len(numbers)
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    if n % 2 == 0:
        median = (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    else:
        median = sorted_numbers[n//2]

    return mean, median

#zad2
def sort_tuple(tup):
    return sorted(tup)

#zad3
def count_empty(matrix):
    count = 0
    for row in matrix:
        for element in row:
            if element is None:
                count += 1
    return count
