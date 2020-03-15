###########################################################
# This file contains all the sections of the pipeline
###########################################################

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

def add_column_for_salary_provided():
    """
    Adds a new column to indicate whether salary data is provided
    """

    loans = pd.read_csv('data/train.csv').pipe(reduce_mem_usage)
    loans = loans.rename(columns={'Annual Income': 'Salary'})
    loans['IsSalaryProvided'] = loans['Salary'].apply(lambda x: int(is_nan(x) == True))

    loans.to_csv('data/1_WithSalaryProvidedColumn.csv', index=False)

def fill_salary_na_with_mean():
    """
    Fill na values in salary with mean
    """

    loans = pd.read_csv('data/1_WithSalaryProvidedColumn.csv').pipe(reduce_mem_usage)

    providedSalaryMean = loans['Salary'].dropna().mean()

    loans['Salary'] = loans['Salary'].fillna(providedSalaryMean)

    loans.to_csv('data/2_WithSalaryNaFilled.csv', index=False)

def add_column_for_experience_provided():
    """
    Adds a new column to indicate whether experience data is provided
    """

    loans = pd.read_csv('data/2_WithSalaryNaFilled.csv').pipe(reduce_mem_usage)

    loans = loans.rename(columns={'Years in current job': 'Experience'})
    loans['IsExperienceProvided'] = loans['Experience'].apply(lambda x: int(is_nan(x) == True))

    loans.to_csv('data/3_WithExperienceProvidedColumn.csv', index=False)

def quantify_experience_and_fill_na_values():
    """
    Quantifies the experience and replaces NaN values with the mean
    """

    loans = pd.read_csv('data/3_WithExperienceProvidedColumn.csv').pipe(reduce_mem_usage)

    loans['Experience'] = loans['Experience'].apply(experience_str2int)
    experienceMean = loans['Experience'].dropna().mean()
    loans['Experience'] = loans['Experience'].fillna(experienceMean)

    loans.to_csv('./data/4_WithExperienceNaFilled.csv', index=False)

# def fill_experience_na_with_mean():
#     """
#     Fill na values in experience with the mean
#     """
#
#     loans = pd.read_csv('data/3_WithExperienceProvidedColumn.csv').pipe(reduce_mem_usage)
#
#     providedExperience =