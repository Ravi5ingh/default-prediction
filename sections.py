from util import *

import pandas as pd
import matplotlib.pyplot as plt

def plot_income_vs_experience():
    """
    Removes records where either income or experience is missing and plots the rest
    """

    loans = pd.read_csv('data/train.csv').pipe(reduce_mem_usage)
    loans = loans.dropna()
    row_count = row_count_of(loans)

    loans_plot = pd.DataFrame()

    loans_plot['< 1 year'] = pad(loans[loans['Years in current job'] == '< 1 year']['Annual Income'], row_count)
    loans_plot['1 year'] = pad(loans[loans['Years in current job'] == '1 year']['Annual Income'], row_count)
    loans_plot['2 years'] = pad(loans[loans['Years in current job'] == '2 years']['Annual Income'], row_count)
    loans_plot['3 years'] = pad(loans[loans['Years in current job'] == '3 years']['Annual Income'], row_count)
    loans_plot['4 years'] = pad(loans[loans['Years in current job'] == '4 years']['Annual Income'], row_count)
    loans_plot['5 years'] = pad(loans[loans['Years in current job'] == '5 years']['Annual Income'], row_count)
    loans_plot['6 years'] = pad(loans[loans['Years in current job'] == '6 years']['Annual Income'], row_count)
    loans_plot['7 years'] = pad(loans[loans['Years in current job'] == '7 years']['Annual Income'], row_count)
    loans_plot['8 years'] = pad(loans[loans['Years in current job'] == '8 years']['Annual Income'], row_count)
    loans_plot['9 years'] = pad(loans[loans['Years in current job'] == '9 years']['Annual Income'], row_count)
    loans_plot['10+ years'] = pad(loans[loans['Years in current job'] == '10+ years']['Annual Income'], row_count)

    plot_to_show = loans_plot.plot.box()

    plot_to_show.set_title('Correlation between Salary and Experience')
    plot_to_show.set_xlabel('Experience')
    plot_to_show.set_ylabel('Salary')

    plt.show()