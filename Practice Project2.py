
print('game no2 enter any number and i will sum and get average of them')

count = int(input('enter how many number do you want to sum : '))

current_count = 0
summ = 0

while current_count < count:
    number = float(input('enter the numer to sum : '))
    summ += number
    current_count +=1

print('sum of all numbers = ', summ)
print('average of all numbers = ', summ/count)
