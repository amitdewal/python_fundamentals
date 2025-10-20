with open("log.txt", "a") as file:
    file.write("Appending first line\n")

with open("log.txt", "a") as file:
    file.write("""Appending second line\nAppending third line\n """)

