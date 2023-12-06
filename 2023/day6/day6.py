import numpy as np
    
t, d = np.loadtxt('6.txt', dtype=int, unpack=False, usecols=(1, 2, 3, 4))
print(np.prod([np.sum((np.arange(1, t[i] + 1) * (t[i] - np.arange(1, t[i] + 1))) > d[i]) for i in range(len(t))]))
print(np.sum(np.arange(52947594) * (52947594 - np.arange(52947594)) > 426137412791216))
