#FOR TESTS ONLY
#adding random digits to Data.txt

import random


file = open('Data.txt', "a")
for i in range(100):
    a = random.randint(1, 1)
    file.write(str(a))
    file.write('\n')

file.close()
