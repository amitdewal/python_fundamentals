# list in pyhton are mutable we can change it
# list are indexed based
# list are dynamic
my_list=["apple","banana","cherry"]
print(my_list)

numbers=[10,20,30,40]
print(numbers)

#mixed list
mixed = ["hello",99,3.14,True]
print(mixed)

#empty list
empty_list = []
print(empty_list)

#accessing elements from list - indexing
fruits=["apple","banana","cherry","mango"]

# access frist item
first_item = fruits[0]
print("first item: ",first_item)

third_item=fruits[2]
print("third item: ",third_item)

# last item
last_item=fruits[-1]
print("last item: ",last_item)

# print(fruits[100])#IndexError: list index out of range


#updating the list bcuze list are mutable

fruits = ["apple","banana","cherry","mango"]
print(fruits)
fruits[1]="blueberry"
print(fruits)


fruits[-1]="kiwi"
print(fruits)


#adding new  item to the list

# appends method add item to the list at the ends

fruits =[]

fruits.append("apple")
fruits.append("banana")
fruits.append("cherry")
print(fruits)


# insert method -> this method add / insert item to the specific place
fruits.insert(1, "orange")
print(fruits)


# extend method add multiplace item to the list but at the end
fruits.extend(["mango","kiwi"])
print(fruits)


# removing item from list

colors = ["red","blue","green","yellow", "purple"]
print(colors)

# remove
colors.remove("green")
print(colors)

#remove by index use pop ()

colors.pop(3)
print(colors)

colors.pop() # if we don't pass any index last item will get removed
print(colors)

#clean the list item but not the list
colors.clear()
print(colors)




