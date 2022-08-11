"""Task2. 10 points
Написать функцию которая будет принимать 2 аргумента (int) и находить максимум из них.
Затем используя функцию1 (вызвать ее) написать функцию2 которая будет принимать 3 аргумента и находить
максимум с помощью функции1.
в итоге будет . псевдокод
функция_нахождения_макс_из_2х(арг1, арг2):
return максимальное значение из 2х аргументов
функция_нахождения_макс_из_3х(арг1, арг2, арг3):
использую тут функция_нахождения_макс_из_2х()
return максимальное значение из 3х аргументов."""
# create a function to find the larger number of the two inputs
def max_value_2(a: int, b: int):
    # use the built-in max function to find the larger value
    return max(a, b)
# create a function to find the larger number of the three inputs
def max_value_3(a: int, b: int, c: int):
    # repeat the procedure using the result of the leading function
    return max(max_value_2(a, b), c)
# output the result of the second function and substitute the values into it
print(max_value_3(1, 10, 4))