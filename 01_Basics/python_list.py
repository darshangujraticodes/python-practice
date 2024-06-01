
"""
in python array another term is list which is denoted by []

Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.


"""


# declaration
list1 = ['harry','ron','harmoine']

print(list1[0])

print(list1[0:2])

print(list1[-1])

list1[1] = "hagrid"

list1[2] = ['malfoy', 'ginny', 'lewis']

list1_copy = list1.copy()

print('list1_copy = ',list1_copy)

print('append() =',list1.append('dumbledore'), list1)

print('insert() =',list1.insert(2,'dr snake'), list1)

print('pop() = ',list1.pop(), list1)

print('remove() = ', list1.remove('harry'),list1)



# methods

square_value = [x**2 for x in range(10)]

print(square_value)



# operation

print('\nfor loop')

for i in list1:
    print(i)

print('\nfor loop')

for k in list1:
    print(k , end='-')

print('\ncondition')

list1 = []  #emptyigng all element of list.

if 'hagrid' in list1:
    print('\nIt is present !!')
else:
    print('\nIt is absent !!')


