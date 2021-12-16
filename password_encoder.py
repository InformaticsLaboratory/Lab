print("Enter the keyword: ", end='')
key_word = input()
coded_letters = list()

# Part 1
for i in key_word:
    coded_letters.append(ord(i))
