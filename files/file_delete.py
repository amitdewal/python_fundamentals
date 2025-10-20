import os

try:
    os.remove("example.txt")
    print("Deleted file")
except FileNotFoundError as e:
    print(f"File not found: {e}")
except PermissionError as e:
    print(f"Permission error: {e}")
except Exception as e:
    print(f"Unknown error: {e}")
