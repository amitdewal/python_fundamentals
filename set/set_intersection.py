set_a = {"apple", "banana", "cherry", "mango"}
set_b = {"banana", "kiwi", "mango", "papaya"}

print("Set A",set_a)
print("Set B",set_b)


# insection
common_items = set_a.intersection(set_b)
print("Common items:", common_items)

# intersection using & symbol
result = set_a & set_b
print("intersection with symbol :", result)


# add a third set
set_c = {"mango","banana","guava","peach"}
total_common = set_a.intersection(set_b).intersection(set_c)
print("Common items in all three sets:", total_common)