import time
import random
import os
from Score import add_score

list_A= []
list_B= []

def generate_sequence(difficulty):
    for i in range (0,difficulty):
        x=random.randint(1, 101)
        list_A.append(x)
        print(list_A)
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')


def get_list_from_user(difficulty):
    print('After seeing the numbers enter the numbers you saw, each one separated with Enter.')
    for i in range (0,difficulty):
        x=int(input('choose number'))
        list_B.append(x)





def is_list_equal(list_A, list_B):
    if list_A == list_B:
        print('True')
        difficulty=len(list_A)
        print('-----------------------------------------------------------------------')
        add_score(difficulty)

    else:
        print('False')



def play(difficulty):
    generate_sequence(difficulty)
    get_list_from_user(difficulty)
    is_list_equal(list_A, list_B)

