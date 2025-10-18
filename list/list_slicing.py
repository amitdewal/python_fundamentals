colors = ["red", "green", "blue", "yellow","orange","purple","pink"]
print(colors)

#first 3 colors
print(colors[0:3]) # ['red', 'green', 'blue']

# from index 2 to 5
print(colors[2:5]) # ['blue', 'yellow', 'orange']

# first start to index 4
print(colors[:4]) # ['red', 'green', 'blue', 'yellow']


# from index 3 to end
print(colors[3:])

# copy full list
print(colors[:]) # ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'pink']

# last 3 items using negative index
print(colors[-3:]) #['orange', 'purple', 'pink']

# every second item
print(colors[::2])
