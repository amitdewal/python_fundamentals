fruits = {"apple","banana","orange","pineapple","kiwi"}

print("original fruits: ", fruits)

#remove method
fruits.remove("banana")
print("After remove:", fruits)

# if fruit is not present this remove() throw error
# fruits.remove("date")


# using discard()
fruits.discard("orange")
print("After discard:", fruits)
fruits.discard("watermelon") # no watermelon is there still no error
print("After discard:", fruits)


#pop method
remove_item = fruits.pop() # this method remove?delete random item from the set
print("removed item :", remove_item)
print(fruits)
