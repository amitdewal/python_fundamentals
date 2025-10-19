fruits = ("apple", "banana", "cherry")
print(fruits)  # ('apple', 'banana', 'cherry')
# fruits[1]="date"  # Tuples don't support item assignment
fruits_list = list(fruits)
print(fruits_list) # ['apple', 'banana', 'cherry']

fruits_list[1]= "blueberry"
print(fruits_list)


# convert list to tuple

numbers = [10,20,30,40]
print(numbers)
numbers_tuple = tuple(numbers)
print(numbers_tuple)