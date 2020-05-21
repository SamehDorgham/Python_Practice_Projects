
print(' welcome in the multiplication app :')
print('enter the first and last number to get multiplication table from :')

first = int(input('enter the first number : '))
last = int(input('enter the last number : '))

for y in range(first,last+1):
    for x in range(first,last+1):
        print(y,'x',x,' = ', y * x)
    print('----------------------------')
