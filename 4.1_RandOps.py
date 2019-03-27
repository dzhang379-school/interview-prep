import random
import math
import bisect

rrange = [random.randrange(28) for x in range(10)]
rint = [random.randint(8, 16) for x in range(10)]

a = [1, 2, 3, 3, 3, 7, 7, 7, 7, 7]
a.insert(9, 10)
a.remove(7)
aSquare = [a for x in range(10)]

print(a)


rchoice = [random.choice(a) for x in range(10)]
random.shuffle(a)

print(bisect.bisect(a, 5))

print(a)
print(rint, rrange, rchoice)

def roots(a, b, c):
    det = (math.pow(b, 2) - 4*a*c)
    if det < 0:
        print( 'No Real Roots.')
    elif det == 0:
        print( 'There is one real root: ', (-b + det)/ (2*a) )
    else:
        print( 'The two roots are: {} and {}'.format((-b + det)/ (2*a), (-b - det) / (2*a)))

roots(1, 5, 6)