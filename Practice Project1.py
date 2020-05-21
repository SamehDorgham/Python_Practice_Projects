
print('this is even odd game')
print('enter a nuber and i will tell you if it`s even or odd')

while True:
    a = input('enter a number : ')

    if a == 'x':
        print(' you press exit ... closing the game ...')
        break
    
    try:
        a = int(a)

        if a % 2 == 0:
            print('this is >>> even number ')
        else:
            print('thi is >>> odd number')
    except ValueError:
        print('please enter a valid number !!')
    


