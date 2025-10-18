fruits = ["apple", "banana", "orange", "cherry"]

# print(fruits)

# wrong way to copy list- same reference
# copied_list = fruits
# print(copied_list)
#
# # print both list
# copied_list[0]="mango"
# print("Copied list ",copied_list)
# print("Fruits after bad copy: ",fruits)


# method 1 - slicing

original_list = fruits[:]
original_list[0]= "orange"
print("sliced copy:", original_list)
print("Fruits after slicing: ",fruits)

# method 2 - copy()

copy_using_method = fruits.copy()
copy_using_method[0] = "kiwi"
print("sliced copy:", copy_using_method)
print("Fruits after slicing: ",fruits)


# mathod 3  list()

constrcuted_copy = list(fruits)
constrcuted_copy[0] = "papaya"
print("copy using list():", constrcuted_copy)
print("Fruits after list(): ",fruits)



