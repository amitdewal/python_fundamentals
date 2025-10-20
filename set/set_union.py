from time import process_time_ns

fruits_a = {"apple","banana","cherry"}
fruits_b ={"cherry","mango","orange"}

print("Set A:", fruits_a)
print("Set B:", fruits_b)

# using union()
all_fruits = fruits_a.union(fruits_b) # remove duplicate keep only unique
print("CombinedSet:", all_fruits)


# union using pipe operator
result_pipe = fruits_a | fruits_b
print("Union with pipe:", result_pipe)


# adding third set
fruits_c = {"kiwi","mango","banana"}
total_fruits = fruits_a.union(fruits_b).union(fruits_c)
print("CombinedSet:", total_fruits)