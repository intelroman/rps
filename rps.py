#!/usr/bin/python3
import time, random, sys, signal, os

def receiveSignal(signalNumber, frame):
    pass
signal.signal(signal.SIGINT, receiveSignal)
def game_items(chose):
    if '1' == chose:
        return 'rock'
    if '2' == chose:
        return 'paper'
    if '3' == chose:
        return 'scissors'
comp_chose = random.randint(1,3)

def compare(usr_input,comp_chose):
    if game_items(usr_input) == 'rock' and game_items(str(comp_chose)) == 'rock':
        return 'equality'
    if game_items(usr_input) == 'rock' and game_items(str(comp_chose)) == 'paper':
        return 'lose'
    if game_items(usr_input) == 'rock' and game_items(str(comp_chose)) == 'scissors':
        return 'win'
    if game_items(usr_input) == 'paper' and game_items(str(comp_chose)) == 'rock':
        return 'win'
    if game_items(usr_input) == 'paper' and game_items(str(comp_chose)) == 'paper':
        return 'equality'
    if game_items(usr_input) == 'paper' and game_items(str(comp_chose)) == 'scissors':
        return 'lose'
    if game_items(usr_input) == 'scissors' and game_items(str(comp_chose)) == 'rock':
        return 'lose'
    if game_items(usr_input) == 'scissors' and game_items(str(comp_chose)) == 'paper':
        return 'win'
    if game_items(usr_input) == 'scissors' and game_items(str(comp_chose)) == 'scissors':
        return 'equality'
    else:
        print("WTF")
        pass

def key_input():
    while True:
        key_input = input('Select item 1 = rock , 2 = paper, 3 = scissors: ').lower()
        if "quit" in key_input or key_input == 'q':
            sys.exit("Game quited , Bye Bye")
        if key_input == '1' or key_input == '2' or key_input == '3':
            return key_input
        else:
            print ("Please select a number from 1 to 3\nOr type quit to exit the game")

def main():
    win = 0
    lose = 0
    while True:
        comp_chose = random.randint(1,3)
        usr_input = key_input()
        print ("Computer chose {}".format (game_items(str(comp_chose))))
        print ("You chose {}".format (game_items(usr_input)))
        print ('Outcome is: {}'.format (compare(usr_input,str(comp_chose))))
        if 'win' in compare(usr_input,str(comp_chose)):
            win += 1
        elif 'lose' in compare(usr_input,str(comp_chose)):
            lose += 1
        print ("Win: {}  Lose: {}".format (win, lose))

if __name__ == "__main__":
    main()
