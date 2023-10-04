import random

def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess !=random_number:
        guess=int(input(f'Guess the Number between 1 and {x}:'))
        if guess< random_number:
            print('Sorry the number is too low, Guess Again!')
        elif guess>random_number:
            print('Too High! Again Please!')
    print(f'Congrats, You have guessed the number{random_number} correclty')

def computer_guess(x):
    low=1
    high=x
    feedback=""
    while feedback != 'c':
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low
        feedback=input(f'Is {guess}too high(H),too low(l),or correct(C)??').lower()
        if feedback =='h':
            high=guess-1
        elif feedback=='l':
            low=guess+1
    print(f"Yay The computer guess your Number.{guess},correctly!")
computer_guess(1000)