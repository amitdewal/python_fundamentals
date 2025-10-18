fruits = ['apple', 'orange', 'strawberry', 'peach']
vegitables = ["carrot","tamato","patato"]

# method 1 using + operator
combined = fruits + vegitables
print("combing using +:",combined)

# method 2 using extend()

all_item = fruits[:]
all_item.extend(vegitables)
print("Combined using extend",all_item)


