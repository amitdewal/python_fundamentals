#lower
original ="Hello World"
lowered = original.lower()
print("lowercase :", lowered)

# upper method
uppered = original.upper()
print("uppercase :", uppered)

# strip() method

messy = " Python "
cleaned = messy.strip()


print("after strip :", cleaned)


#replace method
text =" java is powerful"
print(text)
updated = text.replace("java", "python")
print("after replace :", updated)


# split method
sentense = "python is easy to learn"
words = sentense.split()
print("split result ",words)


# find method ()

text = "Learning Python is fun"
position = text.find("Python")
print("Found at index: ", position)


# title() method

heading = "welcome to python programming"
formatted = heading.title()
print("Title case: ",formatted) #Welcome To Python Programming


# capitalize() method
msg = "hello world"
cleaned = msg.capitalize()
print("capitalize result : ", cleaned) #  Hello world

#startWith()
greeting = "Hello everyone"
print(greeting.startswith("Hello")) #true
print(greeting.endswith("hi")) # false

# endswith()
print(greeting.endswith("everyone")) # True
print(greeting.endswith("hello")) # False

#count
sentense = "Python is easy, Python is powerful, Python is popular."
count = sentense.count("Python")
print("total count :",count)


# isalpha()
name = "python"
print(name.isalpha())

mixed = "Python3"
print(mixed.isalpha())

#isDigit() method
num = "2024"
print(num.isdigit())

bad_input = "year2025"
print(bad_input.isdigit())

#isalnum
code = "abc123"
print(code.isalnum())

code = "abc 123"
print(code.isalnum())


#join()

words = ["python","is","awesome"]
result = " ".join(words)
print(result) #python is awesome