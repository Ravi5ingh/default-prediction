import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from util import *

loans = pd.read_csv('data/train.csv').pipe(reduce_mem_usage)
loans = loans.dropna()

loans_plot = pd.DataFrame()
loans_plot['Salary'] = loans['Annual Income']
ll = loans[loans['Current Loan Amount'] < 99999999]

print(ll)