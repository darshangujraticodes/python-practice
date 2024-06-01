
"""
There are four collection data types in the Python programming language:

1] List is a collection which is ordered and changeable. Allows duplicate members.

2] Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

3] Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.

4] Dictionary is a collection which is ordered** and changeable. No duplicate members.


Note 
set and disctionary are denoted by {} curly braces but dictionary store data in key:value pair and set store value in direct format
"""


set1 = {'mumbai','bangalor','panaji','jaipur','lucknow'}

print(set1)

print(type(set1))

# will give error set doessn not have index number hence it is unordered
# print(set1[0])

#note set does not allow showcasing duplicate vaue and true and 1 and false and 0 treasted as same duplicate value
set2 = {'mumbai','bangalor','panaji','jaipur','mumbai',True,0,False,1,78,546,5454}
print(set2)

print('\n for loop in set')

for i in set2:
    print(i)

if 'mumbai' in set2:
    print('Mumbai is Present in Set2')
else:
    print('Mumbai is not Present in Set2')


if 'mumbai' not in set2:
    print('mumbai is Not Present in Set2')
else:
    print('mumbai is Present in Set2')

#items operation 

set1.add('ranchi')
print(set1, len(set1))


list_update = ['patna', 'hyderabad']
set1.update(list_update)
print(set1, len(set1))

set1.remove('lucknow')
print(set1, len(set1))


#to empty the set

set1.clear()
print(set1)

#to deleted set from value and memory 

# del set1
# print(set1) 
# will give error of set in not defined as it is deleted from memory

#set operation 

set2 = {1,2,3,4,5,6,7,8,9}
set3 = { 11,12,13,14,15,16,17,18,19,4,5,6,8 }

union_set1 = set2.union(set3)
union_set2 = set2 | set3

print('Union Set 1 = ', union_set1, )
print('Union Set 2 = ', union_set2, )

intersection_set1 = set2.intersection(set3)
intersection_set2 = set2 & set3

print('Intersection Set 1 = ', intersection_set1 )
print('Intersection Set 2 = ', intersection_set2)


difference_set1 = set2.difference(set3)
difference_set2 = set2 - set3
difference_set3 = set2 ^ set3  #symmetric Differnce


print('Difference Set 1 = ', difference_set1 )
print('Difference Set 2 = ', difference_set2)
print('Difference Set 3 = ', difference_set3)
