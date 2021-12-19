def letters_to_alphabet_num(keyword):
    code = list()
    for symbol in keyword:
        ascii_code = ord(symbol.lower())
        if 97 <= ascii_code <= 122:
            code.append(ascii_code - 96)
        elif ord('а') <= ascii_code <= ord('я'):
            if ascii_code > ord('е'):
                code.append(ascii_code - ord('а') + 2)
            else:
                code.append(ascii_code - ord('а') + 1)
        elif ascii_code == ord('ё'):
            code.append(7)
        else:
            print("You can input only russian or english letters!")
            exit(0)

    return code


def mul_to_incremented_next(code):
    list_size = len(code)
    coded_letters.append(coded_letters[0])
    for index in range(0, list_size):
        coded_letters[index] = coded_letters[index] * (coded_letters[index + 1] + 1)

    return coded_letters[0:list_size]


def to_float(code):
    list_size = len(code)
    float_number = 0
    for index in range(0, list_size):
        code[index] = str(code[index]) + "0" * (list_size - index - 1)
        float_number += int(code[index])

    float_number = list(str(float_number))
    encoded_number_size = len(float_number)
    if not list_size <= 0:
        if encoded_number_size > list_size:
            float_number.insert(encoded_number_size - list_size, ",")
        elif encoded_number_size < list_size:
            for i in range(0, list_size - encoded_number_size):
                float_number.insert(0, "0")
            float_number.insert(0, ",")
            float_number.insert(0, "0")
        else:
            float_number.insert(0, ",")
            float_number.insert(0, "0")

    return float_number


def dec_to_three(n):
    orientated = list()
    is_negative = False
    if n < 0:
        is_negative = True
        n = -n
    if n == 0:
        orientated.append(0)

    remainders = list()

    while n != 0:
        remainders.append(n % 3)
        n //= 3

    overflow = 0
    for i in remainders:
        i = i + overflow
        if i == -1:
            orientated.insert(0, '-')
            overflow = 0
        elif i == 0:
            orientated.insert(0, 0)
            overflow = 0
        elif i == 1:
            orientated.insert(0, '+')
            overflow = 0
        elif i == 2:
            orientated.insert(0, '-')
            overflow = 1
        elif i == 3:
            orientated.insert(0, 0)
            overflow = 1

    if overflow != 0:
        orientated.insert(0, '+')

    if is_negative:
        for i in range(0, len(orientated)):
            if orientated[i] == '-':
                orientated = orientated[0:i] + list('+') + orientated[i + 1:]
            elif orientated[i] == '+':
                orientated = orientated[0:i] + list('-') + orientated[i + 1:]

    return "".join(map(str, orientated))


print("Enter the keyword: ", end='')
user_keyword = input()

coded_letters = letters_to_alphabet_num(user_keyword)
coded_letters = mul_to_incremented_next(coded_letters)
encoded_number = to_float(coded_letters)
