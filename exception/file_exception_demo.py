try:
    file = open('example.txt','r')
    content = file.read()

except FileNotFoundError as e:
    print(f'File not found: {e}')

# else block run when no exception occured
else:
    print("File content read successfully")
    print(content)

finally:
    if 'file' in locals():
        file.close()
    print('File handling closed')