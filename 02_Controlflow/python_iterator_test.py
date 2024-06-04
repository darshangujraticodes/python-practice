

print('fetch line data using for loop')

f = open('python_internal_loop_opr.py')

print(f.readline())

for line in open('python_internal_loop_opr.py'):
    print(line)

print('\nfetch line data using while loop')

while True:
    line = f.readline()
    if not line: break
    print(line, end='')


    