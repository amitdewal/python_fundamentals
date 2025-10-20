try:
    with open('data.txt', 'w') as file:
        file.write("This is a sample write operation.")

except Exception as e:
    print(f"Error occured: {e}")
finally:
    print("writing operation finished")


try:
    with open('data.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError as e:
    print(f"File not found: {e}")
except Exception as e:
    print(f"Error occured: {e}")
finally:
    print("reading operation finished")