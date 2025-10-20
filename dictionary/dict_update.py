person = {
    "name": "Alice",
    "age": 22,
    "city": "Delhi"

}

person["city"] = "Mumbai"
print(person)

# this create a new entry in the dict
person["email"] = "alice@gmail.com"
print(person)

# update function do the same work as above

# update method can also crate new values
person.update({"phone":"99999999999999999"})
print(person)

# update method can update the existing values
person.update({"age":12})
print(person)















