# basic function
def greet():
    print("hello world")

greet()
greet()
greet()
greet()

# 2 greeting with name
def greet_user(name):
    print("Hello,", name)
greet_user("sachin")
greet_user("dhoni")

names = ["alice","bob","charles"]
for name in names:
    greet_user(name)


# 3
# square function
def square(num):
    return num * num

result = square(5)
print("Square is ", result)
print(square(3))
print(square(4))

# maximum of two number
def maximum(a,b):
    if a > b:
        return a
    else:
        return b
max_value = maximum(5,6)
print("max value:",max_value)



# function with default valuess
def gree_default(name="Guest"):
    print("hello, ",name)
gree_default()
gree_default("sachin")