
#* Day 14 
import random
import art
import game_data
import os

def pick_data():
    value = random.choice(game_data.data)
    return value

def game():
    print(art.logo)
    total_score = 0
    should_continue = True
    valueA = pick_data()
    valueB = pick_data()

    if valueA == valueB:
        valueB = pick_data()

    while should_continue:
        print(f'Compare A: {valueA["name"]}, a {valueA["description"]}, from {valueA["country"]}.')
        print(art.vs)
        print(f'Compare B: {valueB["name"]}, a {valueB["description"]}, from {valueB["country"]}.')
        # print(valueA)
        # print(valueB)
        selection = input('Who has more followers type: "A" or "B" \n').lower()
        if selection == 'a':
            if valueA['follower_count'] > valueB['follower_count']:
                total_score += 1
                print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
                print(f'You are right, current score: {total_score}')
                valueA = pick_data()
                valueB = valueB
                #os.system('clear')
            else:
                print(f'Sorry, that is a wrong answer, Final Score: {total_score}')
                should_continue = False
        elif selection == 'b':
            if valueB['follower_count'] > valueA['follower_count']:
                total_score += 1
                print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
                print(f'You are right, current score: {total_score}')
                valueA = pick_data()
                #os.system('clear')
            else:
                print(f'Sorry, that is a wrong answer, Final Score: {total_score}')
                should_continue = False

    #print(total_score)
game()