import random

while True:
    top_of_range = input('type a number: ')

    if top_of_range.isdigit() and top_of_range.isdigit() >= 0:
        top_of_range = int(top_of_range)
        random_number = random.randint(0, top_of_range)
        break
        

    

        
                

    else:
        print('please type a number next time')
        

#random_number = random.randint(0, top_of_range)
#print(random_number)

guesses = 0

while True:
    guesses += 1
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)

    
    else:
        print('please type a number next time')
        continue

    if user_guess == random_number:
        print('you got it')
        break
    else:
        print('you got it wrong')
    
print(f'you got it in {guesses} guesses')