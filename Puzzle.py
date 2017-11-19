def validity(input_str):
    if input_str.isdigit():
        if int(input_str) >= 0:
            return True
    return False


flag = True
while flag:
    num_str = input('Input a large whole number: ')
    if validity(num_str):
            break
    else:
        print('Input must be a whole number. Try again.')

while flag:
    split = input('Input the split (whole number): ')
    if validity(split):
        if len(num_str) % int(split) == 0:
            break
        else:
            print('{0} must be evenly divisible by {1}'.format(num_str, split))
    else:
        print('Input must be a whole number. Try again.')

initial = 0
previous = 0
flag = False
count = 0
for i in range(1,len(num_str) + 1):
    if i % int(split) == 0:
        print(num_str[initial:i], end='')
        result = num_str[initial:i]
        if int(result) < previous:
            print('sequence is not increasing')
            flag = True
        previous = int(result)
        initial = i
        if count < (int(len(num_str) / int(split))) - 1:
            print(", ",end='')
            count += 1

if not flag:
    print('\nsequence is increasing')

print('approach 2')

initial = 0
for i in range(0, int(len(num_str) / int(split))):
    #print(initial)
    print(num_str[initial:int(split) + initial])
    initial = initial + int(split)
