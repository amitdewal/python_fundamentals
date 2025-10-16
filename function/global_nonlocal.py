global_variable = "I am global"

def my_function():
    # to change the values of global variable u need to use the "global" keyword
    global global_variable
    global_variable ="modified global variable"
my_function()
print(global_variable)



# nonlocal keyword

def outer_function():
    enclosing_variable ="i am enclosing"
    def inner_function():
        nonlocal enclosing_variable
        enclosing_variable ="modified enclosing variable"

    inner_function()
    print(enclosing_variable)
outer_function()





