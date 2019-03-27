def getAdditive(lower, upper):
    lower = str(lower)
    upper = str(upper)

    a = int(lower[0])

    for a in range(lower[0], upper[0]):
        for b in range(lower[1], min(9 - a, upper[1])):
            if a != upper[0] or b!= upper[1] or (a + b) != upper[2]:
                c = a + b
                for d in range(10):
                    for e in range(9 - d):
                        f = d + e
                        print("{}{}{}{}{}{}".format(a, b, c, d, e, f))
            elif (a + b) == upper[2]:
                for d in range(lower[3], upper[3]):
                    for e in range(lower[4], upper[4]):
                        if (d + e) <= upper[5]:
                            f = d + e
