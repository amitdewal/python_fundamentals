users = {
    1:{"name":"Anita","age":12,"country":"China"},
    2:{"name":"Rahul","age":12,"country":"India"},
    3:{"name":"Sara","age":12,"country":"UK"},
}

print(users)


# access values

print(users[1]["name"])
print(users[2]["name"])
print(users[3]["name"])

print("________")
print(users.items())
print("________")

# loop
for user_id ,info in users.items():
    print(user_id, info)
    for key,value in info.items():
        print(key,value)

# add new user
users[4]={"name":"David","age": 40,"country":"Canada"}
print(users)
