exclusions = []

def phoneNumbers(length):
    possibilities = range(10) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in exclusions:
        possibilities.remove(i)

    if length == 0:
        exit(0)

    for i in range(10):
        if i == 4:
            subNumbers('4', possibilities, length -1)
        else:
            modPossible = possibilities[::1]
            modPossible.remove(4)
            print("4 is not lead: ", modPossible)
            subNumbers(str(i),modPossible, length -1)

def subNumbers(currNumber, poss, length):

    if length == 1:
        for i in poss:
            if len(currNumber) > 0 and int(currNumber[len(currNumber) -1]) == (i):
                continue
            print("{}{}".format(currNumber, i))
    else:
        for i in poss:
            if len(currNumber) > 0 and int(currNumber[len(currNumber) - 1]) == (i):
                continue
            newNumber = currNumber + str(i)
            subNumbers(newNumber, poss, length - 1)

def operate(a, b, operator):
    a = int(a)
    b = int(b)
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    else:
        print("An invalid operator was given.")
        exit(0)

def eval(expr):
    stack = []
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    operators = ['+', '-', '*']

    x = 0
    i = ""

    while x < len(expr):

        i = expr[x]

        if i == " ":
            x += 1
            continue
        elif i in digits:
            while x < len(expr) and expr[x] in digits:
                if (x + 1) < len(expr) and expr[x + 1] == ' ':
                    x += 1
                    continue
                elif (x + 1) < len(expr) and expr[x + 1] in digits:
                    i += expr[x]
                    x += 1
                else:
                    x += 1
                    break

            x += 1
            if len(stack) > 0 and stack[len(stack) - 1] in operators:
                operator = stack.pop()
                prev = stack.pop()
                stack.append(operate(prev, i, operator))
            else:
                stack.append(i)
        else:
            stack.append(i)
            x += 1


    if len(stack) != 1:
        print("An invalid expression was given")
        exit(0)
    else:
        return stack.pop()

def main():
    #phoneNumbers(3)
    print(eval("17 + 8 - 16 * 3"))

main()