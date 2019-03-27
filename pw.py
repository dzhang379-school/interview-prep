dict = {}

def getPasswords(currDigit, digitsRemaining):

    num = 0

    key = str(currDigit) + "-" + str(digitsRemaining)
    #print(key)

    if digitsRemaining == 1:
        return currDigit + 1
    elif key in dict:
        return dict[key]
    else:
        for i in range(currDigit + 1):
            num += getPasswords(i, digitsRemaining - 1)

    dict[key] = num
    return num

def getNumPass(digits):
    sum = 0

    if digits == 1:
        return 10

    for i in range(10):
        sum += getPasswords(i, digits - 1)

    return sum

def main():

    print(getNumPass(1))
    print(getNumPass(2))
    print(getNumPass(3))
main()