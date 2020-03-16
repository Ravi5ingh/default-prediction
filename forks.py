###########################################################
# This file contains forks from the main pipeline that
# were done to help get some insights
###########################################################

import pandas as pd
from util import *
import matplotlib.pyplot as plt

def plot_salary_vs_monthly_debt():

    loans = pd.read_csv('data/train.csv').pipe(reduce_mem_usage)
    loans = loans.dropna()

    plt.rc('axes', labelsize=15) # Axis Font
    plt.rc('axes', titlesize=22) # Title Font

    loans_plot = pd.DataFrame()
    loans_plot['Salary'] = loans['Annual Income']
    loans_plot['Monthly Debt'] = loans['Monthly Debt']

    plot = loans_plot.plot.scatter(x = 'Monthly Debt', y='Salary')
    plot.set_xlabel('Monthly Debt')
    plot.set_ylabel('Salary')
    plot.set_title('Salary vs Monthly Debt')

    plt.show()


def plot_salary_vs_loan():

    loans = pd.read_csv('data/train.csv').pipe(reduce_mem_usage)
    loans = loans.dropna()
    loans = loans[loans['Current Loan Amount'] < 99999999]

    plt.rc('axes', labelsize=15) # Axis Font
    plt.rc('axes', titlesize=22) # Title Font

    loans_plot = pd.DataFrame()
    loans_plot['Salary'] = loans['Annual Income']
    loans_plot['Loan'] = loans['Current Loan Amount']

    plot = loans_plot.plot.scatter(x = 'Loan', y='Salary')
    plot.set_xlabel('Loan Amount')
    plot.set_ylabel('Salary')
    plot.set_title('Salary vs Loan Amount')

    plt.show()


def plot_salary_vs_credit_balance():

    loans = pd.read_csv('data/train.csv').pipe(reduce_mem_usage)
    loans = loans.dropna()

    loans_plot = pd.DataFrame()
    loans_plot['Salary'] = loans['Annual Income']
    loans_plot['Credit Balance'] = loans['Current Credit Balance']

    plt.rc('axes', labelsize=15) # Axis Font
    plt.rc('axes', titlesize=22) # Title Font

    plot = loans_plot.plot.scatter(x = 'Credit Balance', y='Salary')
    plot.set_xlabel('Credit Balance')
    plot.set_ylabel('Salary')
    plot.set_title('Salary vs Credit Balance')

    # plt.rcParams.update({'font.size': 50})
    plt.show()

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

def show_quantified_experience_mean():
    """
    Quantify the experience column and show the mean
    """

    loans = pd.read_csv('./data/3_WithExperienceProvidedColumn.csv')

    quantifiedExperience = loans['Experience'].dropna().apply(experience_str2int)

    print(quantifiedExperience.mean())


plot_salary_vs_monthly_debt()