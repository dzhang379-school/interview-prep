def buy_sell(a):
    min, max, newMin = a[0], a[0], a[0]
    for i in range(len(a)):
        if a[i] > max:
            max = a[i]
        elif a[i] < min:
            newMin = a[i]
        if a[i] > newMin + max - min:
            min = newMin
            max = a[i]
    print(max, min, max - min)

buy_sell([1, 4, 45, 6, 67, 300, 12, 35, 350, 1, 0, 9, 98, 666])

