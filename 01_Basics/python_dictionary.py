"""

In python set and dictionary is denoted by { } curly braces

"""

#declaration


india_states = { 
            'maharashtra':{ 'capital':'mumbai', 'city1':'pune', 'city2':'nagpur' } ,
            'gujrat':{ 'capital':'ahmedabad', 'city1':'vadodara', 'city2':'surat' } ,
            'kerala':{ 'capital':'trivandrum', 'city1':'kochi', 'city2':'kollam' } ,
            'rajasthan':{ 'capital':'jaipur', 'city1':'udaipur', 'city2':'jaisalmar' } ,
            'assam':{ 'capital':'dispur', 'city1':'guwahati', 'city2':'jorhat' } ,
        }


india_capital = {'maharashtra':'mumbai', 'kerala':'trivandrum', 'gujrat':'Ahmedabad','andra pradesh':'hyderabad','assam':'dispur','goa':'panaji'}


india_capital['karnataka'] = 'bangalore'

print('\n pop() = ',india_capital.pop('karnataka'), india_capital)


print('\npopitem() = ',india_capital.popitem())

del india_capital['kerala']


india_city_copy = india_capital.copy()

print('\nfinal = ',india_capital)

print('\nfinal india_city_copy = ',india_city_copy)


print(india_capital['maharashtra'])

print(' \nnested dictionary =  ',india_states['assam']['city1'])

india_states['assam']['city2'] = 'dibrugarh'
print(india_states)


#important note

# if name is wrong will give unknown key error
# print(india_capital['keraly'])  


print(india_capital.get('kerala'))




#method



#operation


squarred_num = {x: x**2 for x in range(10)}

print(squarred_num)

print(squarred_num.clear())



#loop in dictionary 

print('\n')

print('\nfor loop in dictionary')

for val in india_states:
    print(val, india_states[val])

print('\n')


for key,value in india_capital.items():
    print(key,' = ', value)


if 'gujrat' in india_capital:
    print('it is present !!')

# different declaration methods

keys = ['united states','united kindom','japan','germany']

default_values = "Best Country for Exploration"

country_dict = dict.fromkeys(keys, default_values)

print("\n")

print(country_dict)





