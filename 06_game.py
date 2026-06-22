import random

print("\t\tWelcome to my Game")
print("\t\tRock Paper Scissors")

user = 0
bot = 0



while True:
    user_score = 0
    bot_score = 0

    for i in range(3):
        print(f"================== Round {i+1} ==============================")
        while True:
            user = input("\t [r] - Rock\n\t [p] - Paper\n\t [s] - Scissors\n\tChoose : ")
            user = user.lower()
            if user == 'r' or user == 'p' or user == 's':
                break
            else:
                print("Error choise")

        bot = random.choice('rps')

        print('\tBot \t\t User')
        print(f'\t[{bot}] \t\t [{user}]')

        if (user == 'r' and bot =='s') or (user=='p' and bot =='r') or user=='s'and bot=='p':
            user_score+=1
        elif bot == 'r' and user =='s' or bot=='p' and user =='r' or bot=='s'and user=='p':
            bot_score+=1

    if user_score> bot_score :
        print("User WIN!!!")
    elif bot_score > user_score:
        print("Bot WIN!!!")
    else:
        print("Draw")

    while True:
        user = input("Play again ? Yes  -[y]. No - [n]")
        user = user.lower()
        if user == 'y' or user == 'n':
            break
        else:
            print("Error letter...")

    if user == 'n':
        print("GAme over")
        break










    

