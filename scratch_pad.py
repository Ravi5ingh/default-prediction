import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'val1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'val2': [2, float('nan'), 4, float('nan'), 6, float('nan'), 8, float('nan'), 10, float('nan')]
})

df = pd.DataFrame([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9],
                   [np.nan, np.nan, np.nan]],
                  columns=['A', 'B', 'C'])

print(df)

plt.show()