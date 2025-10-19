"""a tuple is an ordered collection of items, just like a list
but the key difference is _ tuples are immutable. that means -- once you create a tuple, you cannot change it
the data stays fixes -- and that's the main reason to use tuple
allowed duplicate
faster and use less memory than list
"""


my_tuple = (1,2,3,4,5)
print(my_tuple)


# tuple without ()
another_tuple = (1,2,3,4,5)
print(another_tuple)

#mixed data type
info_tuple = (1,"hello",True,3.14)
print(info_tuple)

empty_tuple = ()
print(empty_tuple)

# single element in the tuple treat as a int
single_tuple = (1)
print(type(single_tuple)) #<class 'int'>

# tuple
# after the elements put the , then this become the tuple
tuple = (10,)
print(type(tuple))  # <class 'tuple'>


