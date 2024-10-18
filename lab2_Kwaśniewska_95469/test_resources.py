from resources import mean_median, sort_tuple, count_empty

#1
numbers = [11, 10, 5, 8, 9]
mean, median = mean_median(numbers)
print(f"Średnia: {mean}, Mediana: {median}")

#2
tuple = (7, 2, 9, 3, 5)
print(f"Posortowana lista: {sort_tuple(tuple)}")

#3
matrix = [
    [1, None, 3],
    [4, 5, None],
    [None, 8, None]
]
print(f"Liczba pustych pól: {count_empty(matrix)}")