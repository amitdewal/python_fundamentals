# symmetric difference in python

# define two sets

set_A = {"red", "green", "blue"}
set_B = {"blue", "yellow", "pink"}

print("Set A", set_A)
print("Set B", set_B)
# "Mujhe wo elements do jo ya to A me hain ya B me,
# lekin dono me ek sath nahi hain."
# method 1: using symmetric_difference()
unique_values = set_A.symmetric_difference(set_B)
print("Unique values", unique_values)

# method 2 using carrot symbol
short_diff = set_A ^ set_B
print("Short difference", short_diff)

# real world example comparing preference
alice_fruits = {"apple", "mango", "kiwi", "banana"}
bob_fruits = {"banana", "mango", "papaya", "guava"}
unique_fruits = alice_fruits.symmetric_difference(bob_fruits)
print("Unique fruits", unique_fruits)
