import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from util import *

loans = pd.read_csv('data/train.csv').pipe(reduce_mem_usage)

corr_matrix = loans.corr()

sns.heatmap(corr_matrix, xticklabels=corr_matrix.columns, yticklabels=corr_matrix.columns, annot=True)

plt.show()

# loans = loans.dropna()
#
# loans_plot = pd.DataFrame()
# loans_plot['Salary'] = loans['Annual Income']
# ll = loans[loans['Current Loan Amount'] < 99999999]
#
# print(ll)