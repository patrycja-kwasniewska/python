from super_functions import count_words, reverse_words, remove_whitespaces
from super_functions import sum_of_digits, factorial

text = "Hello world! This is a test."
print(f"Liczba wyrazów: {count_words(text)}")
print(f"Odwrócona kolejność wyrazów: {reverse_words(text)}")
print(f"Napis bez białych znaków: {remove_whitespaces(text)}")

number = 12345
print(f"Suma cyfr: {sum_of_digits(number)}")
print(f"Silnia 5: {factorial(5)}")
