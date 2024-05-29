

"""
curiosity question

find the difference between this strings

repr('chai')

str('chai')

print('chai')   

"""


string_val = 'lemon tea'

print(string_val)

print(string_val[2])

print(string_val[0:5])

string_val2 = '0123456789'

print(string_val2[2:])

print(string_val2[:6])

print(string_val2[1:8:2])

print(string_val2[-1])

#string methods

string_val3 = "         Darshan is combination of Frontend Developer and Backend Developer          "

print(string_val3.lower())

print(string_val3.upper())

# note python string is case sensitive 
print('count() = ',string_val3.count('Developer')) # output will be 4

print(string_val3.count('developer')) # ouput will be zero 

print('replace() = ',string_val3.replace('Darshan','Rohit'))

# will help to remove unknowing space of start and end of string specificaly we fetch data from customer input form

print('strip() = ',string_val3.strip())

chai = "Ginger Lemon Masala Mint Green"

print('split() = ',chai.split()) #default split built in funcation

print(chai.split(', ')) #defa

print('len() = ',len(chai)) #length 

print('find()',chai.find('Mint')) #fetch the letter postion where data is found in string

prog_lang = ['java','python','javascript','c++']

print("-".join(prog_lang))

temp1 = 45

temp2 = 'Hello World !'

temp3 = False

print(type(temp1), type(temp2), type(temp3))


# new  order formating


order = 'I ordered {} cups of  {} chai'

order_figure = 6

type_chai = 'Masala'


print(order.format(order_figure, type_chai))



# string loops

print('string loops')


str_val2 = 'darshan full stack developer'

for k in str_val2:
    print(k)


#advance string concepts

str_val4 = 'He said, \"Darshan is Full Stack Developer " '

print(str_val4)


web_url = "c:\darshan\python-practice"
print(web_url)

print('darshan' in str_val2)

