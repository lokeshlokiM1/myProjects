menu = {
    'samosa' : 20,
    'egg-puff' : 25,
    'chips' : 10,
    'manchuria' : 60,
    'coke' : 35,
    'ice-cream' : 50
}
print('select your orders :\n   1.samosa - ₹20\n   2.egg-puff - ₹25\n   3.chips - ₹10\n   4.manchuria - ₹60\n   5.coke - ₹35\n   6.ice-cream - ₹50')
t = 0
while True:
    a = input('enter the item : ')
    if a not in menu:
        print(f'    {a} unavailable.')
        a = input('enter the item : ')
    n = int(input('enter quantity : '))
    if a in menu:
        t += n * menu[a]
        print('if you are done with this. type yes else no..')
        i = input()
        if i == 'yes':
            break
    else:
        print(f'{a} unavailable..')


print('Total amount :',t)




