
# file handling operation in python

'''
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)

'''


try:
    f = open('d:/python-practice/05_Advance_Python/demofile.txt')
    print(f.read())

except FileNotFoundError:
    print("File is Missing !")

else:
    print("File is Found ")

finally:
    print("File Handling operation is done successfully !")
    # f.close()


