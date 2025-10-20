import  os

try:
    os.rename("old_file.txt", "new_file.txt")
except FileNotFoundError:
    print("File not found. - maybe it was already renamed")
except Exception as e:
    print(e)


