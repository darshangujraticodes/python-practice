
# python internal loop working model 

'''
python loop consist of three components

1] iteration_tool
(while and for loop)

2] iterable Objects
(list, array, file, tuples, strings)

3] __next__  => (next())


 (while, for loop)
  iteration tool ------------------>  iterabel Objects (list, tuples) ----------
       ^                                                                       | 
       |                                                                       | 
       --------------------------  __next__  <----------------------------------     
          next() next() next()

'''

import time

print('Testing File operation using iterator function')

print(' Darshan is practicing python coding skills')

username = 'Darshan'
email = 'darshaninfo@gmail.com'

print(username, email)


