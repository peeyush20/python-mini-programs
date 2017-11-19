import random
word_list= ['time', 'love', 'inspire', 'hello', 'sound', 'air']
r = random.seed()
# print(r)
num = random.randrange(0, 6, 1)
#print(num)
#print(word_list[num])
word_length = word_list[num].__len__()
guess_word = ['_ ']*word_length

print("Guess the word. Hint: It is {} letter word".format(word_length))
for i in range(0,word_length):
    print("_ ",end="")

print("\nYou have 5 attempts. Right guess will not reduce your count!")
total_attempts = 5
current_attempt=0
flag = 0
correct_answer = False
while(current_attempt < total_attempts or correct_answer):
    ip_user = input("Your guess: ")
    present = word_list[num].count(ip_user)
    if present == 0:
        print("Oops! Letter does not exists!")
        current_attempt += 1
    else:
        print("\nYou guessed correctly")

        current_index = 0
        #Traverse through entire word.
        for i in range(0,word_length):
            #search user input in our word, if present get its index
            current_index = word_list[num].find(ip_user,i)
            if i == current_index:
                guess_word[i] = ip_user

    result = ''.join(guess_word)
    print(result)
    if -1 == result.find("_"):
        print("Wow! You guessed the word completely correct!!")
        flag = 1
        break
    print('\nAttempts left= ',total_attempts - current_attempt)

if flag == 0:
    print('Oops! Sorry you could not guess the word in given number of attempts!')

