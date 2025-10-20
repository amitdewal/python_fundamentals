person = {
    "name": "Alice",
    "age": 12,
    "city": "Delhi"
}
print(person)

city = person["city"]
print(city)

# country = person["country"]  # this line throw error bcuze country is not key to avoid this use get()

country = person.get("country")
print(country)  # None

age = person.get("age")
print(age)

country = person.get("country", "Not available")
print(country)


student ={
    "id":501,
    "name":"Rahu",
    "grades":[90,85,88]
}

name = student.get("name")
grades = student.get("grades")
print("name is ",name)
print("Grades are",grades)