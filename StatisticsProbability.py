import math
import numpy as np
trials = 1000000
counts = 0
for n in range (trials):
    prizes = np.random.randint(20,100,10)

    same = 10-len(np.unique(prizes))

    if same == 1:
        counts +=1

        print('the probability of 2 receiving the same prize is approx',
              round(counts/trials, 4))
