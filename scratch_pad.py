import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from util import *

loans = pd.read_csv('data/1_WithSalaryProvidedColumn.csv').pipe(reduce_mem_usage)

print(loans['Salary'])

inferred = map(lambda pair: 2*pair[0] + 1 if is_nan(pair[1]) else pair[1]), zip(loans['Monthly Debt'], loans['Salary'])



# loans = loans.dropna()
#
# loans_plot = pd.DataFrame()
# loans_plot['Salary'] = loans['Annual Income']
# ll = loans[loans['Current Loan Amount'] < 99999999]
#
# print(ll)