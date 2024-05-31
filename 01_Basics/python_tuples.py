"""

In python tuples are denoted by ()
note key difference between tuples and list

list is mutable and demoted by []
tuples is immutable and denoted by ()

"""

#declaration



india_city = ('mumbai','nasik','matheran','pune','nagpur')

new_city = ('indore' , 'jaganath', 'vadodara', 'surat','surat','surat','surat')

print(india_city)

print(india_city[0])

print(india_city[0:4])

print(india_city[-1])

print(india_city[3:])


print('type identifcation = ', type(india_city))


 # will not give error
print(india_city[:10])    

combo_city = india_city + new_city

print(combo_city)


#important immutable test

#it should give error due to tuple immutable behaviour
# india_city[2] = 'nagpur'  

#methods

print('length =',len(combo_city))

print('surat count() = ',combo_city.count('surat'))


# tuples have special case while fetching database values


country = ('india','france','japan')

# as we unwrap distort data in react here same database value is unwrap using tuple 2 reason why tuple is using due to its unwrap feature and immutable nature which make tuple data intact


# here indian, france and  japan are variable which are storing tuple data in sequence very useful in database value 
(ind, fr, jp) = country 


print(ind, fr, jp)

#loops and condition

print('\n  for loop on tuples')

for k in combo_city:
    print(k)


print('\n value check in tuples')


if 'vadodara' in combo_city:
    print('yes i have !!')


