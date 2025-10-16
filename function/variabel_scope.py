#local scope, enclosing scope, global scope, built in scope
def my_function():
    local_variable = "i am local"
    # print(local_variable)
my_function()
# print(local_variable) # NameError: name 'local_variable' is not defined


# enclosing scope
def outer_function():
    enclosing_variable = "i am enclosing variable"
    def inner_function():
        print(enclosing_variable)
    inner_function()
outer_function()


# global scope

global_variable = "i am global variable"
def function():
    print(global_variable)
function()
print(global_variable)

# built in scope print len and range

result = len("hello, world!")
print(result)

