def evens(array):
    currLoc = 0
    for i in range(len(array)):
        if array[i] % 2 == 0:
            array[i], array[currLoc] = array[currLoc], array[i]
            currLoc += 1
    print(array)

def evens2(array):
    left = 0
    right = len(array) - 1

    while array[left] % 2 == 0 and \
                left < len(array):
        left += 1

    while right > left:
        if array[right] % 2 == 0:
            array[right], array[left] = array[left], array[right]
            left += 1
        right -= 1
    print(array)

import time

array = [0, 1, 34, 5, 1, 23, 7, 6, 8, 23, 45, 10]

start = time.time()
evens(array)
print(time.time() - start)

start = time.time()
evens2(array)
print(time.time() - start)