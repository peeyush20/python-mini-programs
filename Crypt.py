with open('cypher1.txt', 'r') as myFile:
    data = myFile.read().split(" ")

count = [0] * 26
for i in data:
    for j in i:
        count[ord(j) - ord('a')] += 1

dict = {}
for i in range(0, 26):
    dict[chr(ord('a') + i)] = count[i]

# index having maximum frequency
max_index = count.index(max(count))
# print(max_index)

# encrypted character repeated maximum times.
max_letter = chr(ord('a') + max_index)
print('encrypted character repeated maximum times: ', max_letter)

# Shift by
shift = (ord(max_letter) - ord('e')) % 26
print("Shift is by: ", shift)
print("To Confirm: Next Most occurrence should be of letter t")

for j in range(0, len(data)):
    if data[j] == '':
        continue
    for i in range(0, len(data[j])):
        print(chr(((ord(data[j][i]) - ord('a') - shift) % 26) + ord('a')), end="")
    print(" ", end="")

for i in count[:]:  # the slice creates a copy
    if i == max(count):
        count.remove(i)

second_max_index = count.index(max(count))
second_max_letter = chr(ord('a') + second_max_index)

print("\nEncrypted second most occurrence: ", second_max_letter)

print((ord(second_max_letter) - shift))
print(((ord(second_max_letter) - shift) % 26))
letter = chr(((ord(second_max_letter) - shift) % 26) + ord('a'))
print(letter)