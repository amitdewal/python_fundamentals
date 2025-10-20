import os

folder_path = "my_files"
entries = os.listdir(folder_path)
print(entries)


for entry in entries:
    full_path = os.path.join(folder_path, entry)
    if os.path.isfile(full_path):
        if entry.endswith(".txt"):
            print(entry)