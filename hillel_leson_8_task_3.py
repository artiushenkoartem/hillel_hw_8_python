"""Task 3. 10 points Lambda function. с помощью Анонимной функции остортировать список кортежей по цифре.
Пример(Example)
Input: [('bread', 5), ('milk', 2), ('eggs', 30), ('cola', 1)]
Otput: [('cola', 1), ('milk', 2), ('bread', 5), ('eggs', 30)]"""
# create a list of tuples by condition
tuple_list = [('bread', 5), ('milk', 2), ('eggs', 30), ('cola', 1)]
# Sort the list based on the second item of the tuple
sorted_list = sorted(tuple_list, key=lambda i: i[1])
# print the result of the function
print(sorted_list)
