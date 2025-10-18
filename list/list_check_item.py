fruits = ["apple","banana","mango","cherry"]
print(fruits)


if "banana" in fruits:
    print("banana is in fruits")

if "grape" in fruits:
    print("grape is in fruits")
else:
    print("grape is not in fruits")


exists = "mango" in fruits
print("Does mango exists? ", exists)


# item = input("Enter a fruit name: ")
# if item in fruits:
#     print(item, " is in list")
# else:
#     print(item, " is not in list")



# list methods demo - len(), index(), and count()

fruits = ["apple","banana","mango","cherry","apple"]

length = len(fruits)
print("length of the list",length)


# index
position = fruits.index("cherry")
print("index of  cherry",position)


# print(fruits.index("kiwi"))

# count method
count = fruits.count("apple")
print("Apple appears:", count,"times")


