import pandas as pd
import numpy as np
value_matrix = pd.read_csv('./value_matrix_4.csv').set_index('username')
print(value_matrix)
matrix = value_matrix.values
print(matrix)
u, s, vh = np.linalg.svd(matrix, full_matrices=False)
print(u)
print(s)
print(vh)

np.save(open('u.npy', 'wb'), u)
np.save(open('s.npy', 'wb'), s)
np.save(open('vh.npy', 'wb'), vh)