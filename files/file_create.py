file = open("output.txt",
            "w")  # w means write mode if file exists it clean the file and write, if file does not exists it create the file

file.write("This is the first line of the text.")
file.write("\n")
file.write("This is the second line of the text.\n")
file.close()


# write multiples line in the files
file = open("output.txt", "w")
lines = ["Line1\n", "Line2\n", "Line3\n"]
file.writelines(lines)
file.close()



# safer way to work with the file  here we dont need to write the close() python handle automatically
with open("output.txt", "w") as file:
    file.write("This is the first line of the text.")