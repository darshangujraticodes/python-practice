'''
Exception is one of the best practice to deal with errors and prvent app from getting crash 
it generally occurs through coder mistake logic or syntax, or accessing unavailable resource 

eg. 

list = [1,2]
print(list[3]) #showcase Index error due to missing 3rd position value 

All this kind of error are handled through exception

'''



try:
    student_id = int(input("\nEnter Your Roll No = "))
    file = open("python_funcions.py")

# it has limitation it can only handle one type of error i.e value for multiple type exception follow other syntax
# except ValueError as ex:
#     print('Please enter valid Roll Number')
#     print(ex, type(ex))

except (ValueError, ZeroDivisionError):
    print('Please enter valid Roll Number')

else:
    # it get executed if no exception is catch
    print('\nNo Exception is Found !')
    if (student_id == 1):
        print('Roll No 1 is Ron.')

finally:
    # this part will get executed in both case if exception is catch or not very userful in database, api and file operation 
    file.close()


print('\nExecution Continues....\n')

