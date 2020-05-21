
'-----------------------------------------------------------------------------------------'

'''
# جدول الضرب
x = 1
while x < 11:
    print('-------------------------------------------')
    y = 1
    while y < 11:
        print( ' x = ', x, ' y = ', y, ' | ', 'Result = x*y = ', x*y)
        y += 1
    # print(x)
    x += 1
print('-------------------------------------------')
'''

'-----------------------------------------------------------------------------------------'

a = "    i love python    "
print (a.strip())
print (a.rstrip())
print (a.lstrip())

a = "####i love python####"
print (a.strip("#"))
print (a.rstrip("#"))
print (a.lstrip("#"))

a = "I Love Python and 2d Graphics and 4g"
print (a.title())
print (a.capitalize())

x, y, z = "1", "11", "111"
print(x)
print(y)
print(z)

print(x.zfill(3))
print(y.zfill(3))
print(z.zfill(3))

n = "Sameh"
print(n.upper())
print(n.lower())

'-----------------------------------------------------------------------------------------'

Name, Age, Language = "Sameh",43,"Python"

print("My Name Is {} My Age Is {} My Programming Language Is {}".format(Name,Age,Language))

print("My Name Is %s My Age Is %d My Programming Language Is %s" % (Name,Age,Language))

a = 100
b = 20

print("Number1 is : %d Number2 is %.2f" % (a,b))

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a%b)
print(a//b)


'-----------------------------------------------------------------------------------------'


for i in range(1,11) :
    print(i)


start = int(input('enter the start number'))
end = int(input('enter the end number'))

for i in range(start,end+1) :
    print(i)
    

rows = int(input('how many rows'))
cols = int(input('how many columns'))

for r in range(rows) :
    for c in range(cols) :
        print ('*', end='')
    print()

size = 8

for r in range(8) :
    for c in range(r+1) :
        print('*', end='')
    print()


sum1 = lambda x,y : x + y
sum1(3,5)
#print(sum1)
