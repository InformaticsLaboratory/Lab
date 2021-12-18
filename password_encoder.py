def convert_num(string):
    sum = 0
    avr = 0
    spl = []
    new_x = ''
    new_y = ''

    spl = string.split(',')
    print(spl)
    avr_str = spl[1][0:-1]
    len_str = len(avr_str)

    if len_str > 0:
        for i in range(len_str):
            if avr_str[i] != ',':
                sum += int(avr_str[i])
            else:
                len_str -=1
        avr = int(sum//len_str)
        if avr < 2:
            avr = 2
    else:
        avr = 2

    x = int(spl[0])
    y = int(spl[1][-1:-2:-1])
    print('1')
    while y != 0:
        new_y += str(y%avr)
        y //= avr
    print('2')
    while x != 0:
        new_x += str(x%avr)
        x //= avr


    new_x = new_x[::-1]
    new_y = new_y[::-1]
    new_string = new_x + ',' + spl[1]
    new_string = new_string[0:-1] + '+' + new_y
    print(new_string)
    return new_string
print(convert_num("2489357,34289529345"))