name = input('type your name: ')
print(f'welcome {name} to your adventure')

answer = input('you are ona dirt road, it has come to an end you can go left and right. which way would you like to go? ').lower()

if answer == 'left': 
    answer = input('you have come to a river. you can walk around it or swim acroos. type walk to walk or swim to swim: ').lower()

    if answer == 'walk':
        print('you walked ran out of water and lost the game')

    elif answer == 'swim':
        print('you were eaten by an alligator')


    else:
        print('not a valid option. you lose')

elif answer == 'right':

    answer = input('you came to a bridge looks wobbly do you want to cross or hrad back?: ')

    if answer == 'back':
        print('you  lost the game')

    elif answer == 'cross':
        answer = input('you met a stranger, speak or ignore: ').lower()

        if answer == 'speak':
            print('you speak and they help you, u won')

        elif answer == 'ignore':
            print('you were beaten by the stranger')


        else:
            print('not a valid option. you lose')


    else:
        print('not a valid option. you lose')

else:
    print('not a valid option. you lose')
