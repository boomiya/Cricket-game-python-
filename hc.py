import random

def checkResult(choice_a , choice_b):
    if choice_a == choice_b:
        return True
    return False

print(' Hello Welcome to my Hand cricket Game')

print("Rules are as follows :")
print("----------------------------------------------")
print("User should choose between bowling and batting")
print("User should choose numbers only from 0 to 6")
print("If batter selects 0 bowler's number will be added to batter's score")
print("Type 'exit' to exit out of the game")
print("----------------------------------------------")

def incrementScore(bat,bowl,curr_score): 
    if bat==0:
        return curr_score + bowl
    else:
        return curr_score + bat


user_choice = input("Choose anyone : 1-Bat / 2-bowl :  ")
if user_choice == '1':
    user_input = input(" You are batting  - Enter any number only from 0-6 :  ")
else:
    user_input = input(" You are Bowling  - Enter any number only from 0-6 :  ")
user_score = 0
comp_score = 0
isFirstHalf = True
user_input = user_input.lower()

while(user_input != "exit"):
    computer_move = random.randint(0,6) # computer selects random move
    user_move = int(user_input)

    print(f"Your move - {user_move} /  Computer move - {computer_move}")

    if user_choice == '1': # when user is currently batting
        if checkResult(user_move,computer_move): # function to check for out condition 
            if isFirstHalf:
                print(f"You are out. Now Computer will bat.. Target is {user_score + 1}")
                print("---------------------------------------------------------")
                isFirstHalf = False 
                user_choice = '2' # user becomes bowler
            else:
                print("Sorry You have lost this game!")
                exit()
        elif isFirstHalf:
            user_score  = incrementScore(user_move,computer_move,user_score)
        else:
            if user_score + user_move > comp_score:
                print("Congratulations!!!! You have Won!!!")
                exit()
            else:
                user_score += incrementScore(user_move,computer_move,user_score)

    else: # if user is bowling
        if checkResult(user_move,computer_move):
            if isFirstHalf:
                print(f"Great Job You took the computer's wicket. Now its Your turn to bat.... target is {comp_score + 1}")
                print("---------------------------------------------------------")
                isFirstHalf = False # first half ends
                user_choice = '1' # user becomes batter
            else:
                print("Congratulations!!!! You have Won!!!")
                exit()
        elif isFirstHalf:
            comp_score  = incrementScore(computer_move,user_move,comp_score)
        else:
            if comp_score+computer_move > user_score:
                print("Sorry You have lost this game!")
                exit()
            else:
                comp_score  = incrementScore(computer_move,user_move,comp_score)
    print(f"Your Score : {user_score}",end="  |  ")
    print(f"Computer Score : {comp_score}")

    print("--------------------------------------------------------")

    if user_choice == '1':
        user_input = input(" You are batting  - Enter any number only from 0-6 :  ")
    else:
        user_input = input(" You are Bowling  - Enter any number only from 0-6 :  ")
    user_input = user_input.lower()