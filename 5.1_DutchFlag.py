def DFP(a):
    pivotVal = a[len(a) // 2]
    left, right = 0, len(a) - 1
    while left < right:
        if a[left] < pivotVal:
            left += 1
        elif a[right] >= pivotVal:
            right -= 1
        else:
            a[right], a[left] = a[left], a[right]
            left += 1
            right -= 1

    right = len(a) - 1
    while left < right:
        if a[left] == pivotVal:
            left += 1
        elif a[right] > pivotVal:
            right -= 1
        else:
            a[right], a[left] = a[left], a[right]
            left += 1
            right -= 1

    print(pivotVal)
    print(a)

def DFP2(a):
    left, middle, right = 0, 0, len(a) - 1
    pivotVal = a[len(a) // 2]

    while middle < right:
        if a[middle] > pivotVal:
            a[right], a[middle] = a[middle], a[right]
            right -= 1
        elif a[middle] < pivotVal:
            a[left], a[middle] = a[middle], a[left]
            left += 1
        middle += 1
    print(pivotVal)
    print(a)

def Variant2(a):
    numTrue, currLoc = 0, 0
    while currLoc < (len(a) - numTrue):
        if a[currLoc]:
            numTrue += 1
        a[currLoc] = 0
        currLoc += 1
    for i in range(currLoc - numTrue, currLoc):
        a[i] = 1
    print(numTrue, a)

test = [1, 3, 5, 7, 4, 6, 7, 1, 4, 3, 2, 3, 4, 1, 7, 8, 9]
DFP(test)
DFP2(test)

test2 = [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1]
Variant2(test2)