import numpy as np

tab = np.zeros((5, 5), dtype=int)

tab[:] = 8
tab[1:4, 1:4] = 0
tab[0,0] = 1
tab = np.where(tab==0, -1, tab)
print(tab)
