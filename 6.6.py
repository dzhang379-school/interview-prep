def numToString(num):
    dict = {
        9: 'nine',
        8: 'eight',
        7: 'seven',
        6: 'six',
        5: 'five',
        4: 'four',
        3: 'three',
        2: 'two',
        1: 'one',
        0: ''
    }

    tensDict = {
        9: 'nine',
        8: 'eigh',
        7: 'seven',
        6: 'six',
        5: 'fif',
        4: 'for',
        3: 'thir',
        2: 'twen',
    }

    str = ''
    hundreds = num // 100
    tens = (num // 10) % 10
    ones = num % 10

    if hundreds:
        str += dict[hundreds] + ' hundred'
    if tens > 1:
        str += ' ' + tensDict[tens] + 'ty'
        str += ' ' + dict[ones]
    elif tens == 1:
        if ones > 2:
            str += ' ' + tensDict[ones] + 'teen'
        elif ones == 2:
            str += ' twelve'
        elif ones == 1:
            str += ' eleven'
        elif ones == 0:
            str += ' ten'
    else:
        if ones != 0:
            str += ' ' + dict[ones]

    return str

test = [112, 334, 500, 667, 652, 608, 611, 957, 572, 515, 613, 614, 618, 100]
output = [numToString(x) for x in test]
print(output)
