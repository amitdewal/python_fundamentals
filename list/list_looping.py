countries = ["india", "canada", "japan", "Brazil"]
print(countries)

# for loop
for each_country in countries:
    print("i want to visit",each_country)

for i in range(len(countries)):
    print("Country at index "+ str(i)+": "+countries[i])


# while loop
index = 0
while index < len(countries):
     print("Country at index "+ str(index)+": "+countries[index])
     index = index + 1



