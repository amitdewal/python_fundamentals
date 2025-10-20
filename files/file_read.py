with open("exmaple.txt") as file:
    content = file.read()
    # print(content)


# read line
with open("exmaple.txt","r") as file:
    line = file.readline()
    while line:
        print(line, end="")
        line = file.readline()


# readlines
with open("exmaple.txt","r") as file:
    lines = file.readlines()
    for line in lines:
        print(line, end="")



with open("exmaple.txt","r") as file:
    chunk = file.read(5)
    while chunk:
        print(chunk)
        chunk = file.read(5)
