slayer = int(input('Enter your guess for SLAYER: '))
length = (len(str(slayer)))

if length != 6:
    print('Your guess is incorrect:')
    print('SLAYER must be a 6-digit number.')
else:
    r = slayer % 10
    number = slayer
    value = [0]*5
    for i in range(0,length - 1):
        number = int(number / 10)
        value[i] = number % 10

    layers = 100000 * value[3] + 10000 * value[2] + 1000 * value[1] + 100 * value[0] + 10 * r + 1 * value[4]
    slayer = slayer * 3
    if slayer == layers:
        print('Your guess is correct:')
    else:
        print('Your guess is incorrect:')

    print('SLAYER + SLAYER + SLAYER = ', slayer)
    print('LAYERS = ', layers)

print('Thanks for playing')