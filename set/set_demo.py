# in simple terms, a set is an unordered collection of unique item.
# that means- it does not keep things in order , and it never allows duplicate
# its similar to a real -life set , like a set of cards, a set of numbers, a set of books, where no item appears twice
# no indexing here


fruits = {"apple", "banana", "orange"}
numbers = set([1, 2, 3, 2, 1])
print("Fruits set: ", fruits)
print("Numbers set: ", numbers)

# empty set
empty_set = set()
print("Empty set: ", empty_set)

user_id = {101, 102, 103, 101, 104}

print("Uniques user ids: ", user_id)