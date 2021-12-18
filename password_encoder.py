print("Enter the keyword: ", end='')
key_word = input()
coded_letters = list()

# Part 1
for i in key_word:
    ascii_code = ord(i.lower())
    if 97 <= ascii_code <= 122:
        coded_letters.append(ascii_code - 96)
    elif ord('а') <= ascii_code <= ord('я'):
        coded_letters.append(ascii_code - ord('а') + 1)
    else:
        print("You can input only russian or english letters!")
        exit(0)

# Part 2
list_size = len(coded_letters)
coded_letters.append(coded_letters[0])
for i in range(0, list_size):
    coded_letters[i] = coded_letters[i] * (coded_letters[i+1] + 1)

coded_letters = coded_letters[0:list_size]

# Part 3
encoded_number = 0
for i in range(0, list_size):
    coded_letters[i] = str(coded_letters[i]) + "0" * (list_size - i - 1)
    encoded_number += int(coded_letters[i])

encoded_number = list(str(encoded_number))
encoded_number_size = len(encoded_number)
if not list_size <= 0:
    if encoded_number_size > list_size:
        encoded_number.insert(encoded_number_size - list_size, ",")
    elif encoded_number_size < list_size:
        for i in range(0, list_size - encoded_number_size):
            encoded_number.insert(0, "0")
        encoded_number.insert(0, ",")
        encoded_number.insert(0, "0")
    else:
        encoded_number.insert(0, ",")
        encoded_number.insert(0, "0")
