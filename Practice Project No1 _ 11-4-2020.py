
class AllInOne_project1:

    def __init__(self):
        print('Welcome to My Game  ^__^ ')
        print('choose your Game from the list : ')
        print(' [1] Even-Odd Game ')
        print(' [2] Sum-Average Game ')
        print(' [3] Multiplication Game ')

        self.User_Choice()


    def User_Choice(self):

        while True :
                
            try:
                choice = int(input('Please enter your choice No : '))

                if choice == 1:
                    self.odd_even_game()
                elif choice == 2:
                    self.Sum_Average_game()
                elif choice == 3:
                    self.Multiplication_game()
                else:
                    print('please enter a number between 1,2,3 : ')
            except ValueError:
                print('Please enter a valid number between 1,2 or 3 : ')    

    def odd_even_game(self):
        
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
            


    def Sum_Average_game(self):
        
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



    def Multiplication_game(self):
        print(' welcome in the multiplication app :')
        print('enter the first and last number to get multiplication table from :')

        first = int(input('enter the first number : '))
        last = int(input('enter the last number : '))

        for y in range(first,last+1):
            for x in range(1,11):
                print(y,'x',x,' = ', y * x)
            print('----------------------------')


c = AllInOne_project1()
