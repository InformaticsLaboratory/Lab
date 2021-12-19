def convert_to_binary(number):
    number = int(number)
    print(number)
    binary = ""
    while number // 2 != 0:
        print(number)
        binary += str(number % 2)
        number //= 2
    binary += str(number % 2)

    binary = binary[::-1]

    if binary[0] == '0':
        binary = binary[1:]
    if binary == '':
        binary = "0"
    return binary


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
