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
