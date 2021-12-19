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


def convert_edges(string):
    average = 0
    spl_str = []
    new_x = ''
    new_y = ''

    if not(',' in string):
        string += ',0'

    spl_str = string.split(',')

    average = calculate_average(spl_str)

    x = int(spl_str[0])
    y = int(spl_str[1][-1:-2:-1])

    while x != 0:
        new_x += str(x % average)
        x //= average

    while y != 0:
        new_y += str(y % average)
        y //= average

    if len(new_x) == 0:
        new_x = '0'
    if len(new_y) == 0:
        new_y = '0'

    new_x = new_x[::-1]
    new_y = new_y[::-1]
    new_string = new_x + ',' + spl_str[1]
    new_string = new_string[0:-1] + '+' + new_y

    return new_string


def calculate_average(spl_str):
    amount = 0
    average_str = spl_str[1][0:-1]
    len_str = len(average_str)

    if len_str > 0:
        for i in range(len_str):
            if average_str[i] != ',':
                amount += int(average_str[i])
            else:
                len_str -= 1
        average = int(amount // len_str)
        if average < 2:
            return 2
    else:
        return 2

    return average


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


def move_right_part(code_word):
    code_word = str(code_word)
    right_part = ""
    while code_word[-1] != "+":
        right_part += code_word[-1]
        code_word = code_word[:-1]
    right_part = right_part[::-1]

    right_part = convert_to_binary(right_part)

    left_part = convert_to_binary(code_word[:code_word.find(',')]) + (code_word[code_word.find(','):])

    return right_part + '-' + left_part


def convert_to_binary(number):
    number = int(number)
    binary = ""
    while number // 2 != 0:
        binary += str(number % 2)
        number //= 2
    binary += str(number % 2)

    binary = binary[::-1]

    if binary[0] == '0':
        binary = binary[1:]
    if binary == '':
        binary = "0"
    return binary


print("Enter the keyword: ", end='')
user_keyword = input()

coded_letters = letters_to_alphabet_num(user_keyword)
coded_letters = mul_to_incremented_next(coded_letters)
encoded_number = to_float(coded_letters)
