import random

n = random.randint(1,15)  # 4
print('Guess the number(1-15) in 3 choices :')
c = 3
while c != 0:  # 3
    a = int(input('enter num value : '))  # 2
    if a == n:
        print('Your guess is correct.\nYou Won..👌')
        print('if you want to play again, type yes else no..')
        t = input()
        if t=='no':
            break
        else:
            n = random.randint(1, 15)
            print(n)
            c=3
    else:
        c -= 1  # 2
        print(f'guess is wrong.Now you have {c} choices')
        if c == 0:
            print('You lost..😢')
            print('if you want to play again, type yes else no..')
            t = input()
            if t == 'no':
                break
            else:
                n = random.randint(1, 15)
                print(n)
                c = 3










