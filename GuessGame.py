import random
secret_number = []


def generate_number(difficulty):
    x=random.randint(1, difficulty)
    secret_number.append(x)



def get_guess_from_user(difficulty):
    difficulty=str(difficulty)
    difficulty=int(input('guess a number between 1 to '+ difficulty +''))
    return difficulty

def compare_results(difficulty, secret_number):
    if  secret_number == difficulty:
        print(True)
        from Score import add_score
        print('-----------------------------------------------------------------------')
        add_score(difficulty)
    else:
        print(False)


def play(difficulty):
    generate_number(difficulty)
    get_guess_from_user(difficulty)
    compare_results(difficulty, secret_number[0])

