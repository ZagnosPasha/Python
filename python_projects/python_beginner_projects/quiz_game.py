print("Welcome to my computer quiz")

playing = input("Do you want to play? ")
result = 0

if playing.lower() != "yes":
    quit()

print('okay lets play :)')

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print('Correct')
    result +=1


answerSecond = input('what does i stand for')
if answerSecond == 'me':
    print('correct')
    result += 1

print(result)