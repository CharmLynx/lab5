def check(n):
    if n % 2 == 0:
        return "loh"
    else:
        return "neloh"

import random
number = random.randrange(0, 100, 2)

check(number)
