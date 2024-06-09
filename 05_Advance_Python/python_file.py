
# file handling operation in python

'''
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)

'''

# Note file handling operation should be clear if is open for reading purpose then it cannot be altered or updated.

# open and close the file of certain requirement eg if it is open to write or append data read() method could be possible first close write() and again open with read method()

import os

try:
    # this operation is done on already existing file
    f = open('d:/python-practice/05_Advance_Python/demofile.txt','r')
    print('\nread() ',f.read())  # read and print whole text content of file 
    # print('\nreadlines',f.readlines())  # read only single line return data in list

    # f.write('Learning and Implementing Devops Technology for Scalable Application')
    # f.close()

    f = open('d:/python-practice/05_Advance_Python/demofile.txt','a')
    f.write('Mastering Frontend, Backend and Deveop\'s ')
    f.close()

    # if this file already exist lead to error otherwise will create new file
    f = open('d:/python-practice/05_Advance_Python/newfile.txt','x')
    f.write('New File is Created and content is added to new file!')
    f.close()

    # read new created file 
    f = open('d:/python-practice/05_Advance_Python/newfile.txt','r')
    print('new file content : ',f.read())
    f.close()

    # testing write methods which replace old with new content
    f = open('d:/python-practice/05_Advance_Python/newfile.txt','w')
    f.write('Updated File with New content in using write Operation method !')
    f.close()

    # read new created file 
    f = open('d:/python-practice/05_Advance_Python/newfile.txt','r')
    print('new file content : ',f.read())
    f.close()

    # now to delete new created required root level os access 
    os.remove('d:/python-practice/05_Advance_Python/newfile.txt')
    print('New File is Deleted !')

except FileNotFoundError:
    print("File is Missing !")

else:
    print("File is Found ")

finally:
    print("File Handling operation is done successfully !")
    


'''
Note
'a' => append data in file without disturbing previous content
'w' => Erase out previous content and Replace it with new content shared content in write() method
'''