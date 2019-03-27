def countBits(num):
    if num < 2:
        return num % 2
    else:
        return num % 2 + countBits(num // 2)

def countBits2(num):
    count = 0
    while num:
        count += (num & 1)
        num >>= 1
    return count

def mod(power, x):
    mask = (2 ** power) - 1
    return (x & mask)

def isPower(x):
    return x == (x & ~(x - 1))

def main():
    testCases = [4, 5, 6, 8, 11, 15, 16]

    out1 = [countBits(x) for x in testCases]
    out2 = [countBits2(x) for x in testCases]

    powers = [1, 2, 3]
    out3 = [[mod(y, x) for x in testCases] for y in powers]

    out4 = [isPower(x) for x in testCases]

    print(out1)
    print(out2)
    print(out3)
    print(out4)

# main()

