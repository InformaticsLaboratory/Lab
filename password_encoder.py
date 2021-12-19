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
