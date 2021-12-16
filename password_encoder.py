print("Enter the keyword: ", end='')
key_word = input()
coded_letters = list()

# Part 1
for i in key_word:
    coded_letters.append(ord(i))

# Part 2
coded_letters.append(coded_letters[0])
list_size = len(coded_letters)
for i in range(0, list_size - 1):
    coded_letters[i] = coded_letters[i] * (coded_letters[i+1] + 1)

coded_letters = coded_letters[0:list_size-1]
