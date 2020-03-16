###########################################################
# This file contains all the sections of the pipeline
###########################################################

from util import *

import pandas as pd

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
    experienceMean = round(loans['Experience'].dropna().mean())
    loans['Experience'] = loans['Experience'].fillna(experienceMean)

    loans.to_csv('./data/4_WithExperienceNaFilled.csv', index=False)

def remove_delinquency():
    """
    Removes the delinquency column
    """

    loans = pd.read_csv('data/4_WithExperienceNaFilled.csv').pipe(reduce_mem_usage)

    loans = loans.drop('Months since last delinquent', axis=1)

    loans.to_csv('./data/5_WithoutDelinquency.csv', index=False)



# def fill_experience_na_with_mean():
#     """
#     Fill na values in experience with the mean
#     """
#
#     loans = pd.read_csv('data/3_WithExperienceProvidedColumn.csv').pipe(reduce_mem_usage)
#
#     providedExperience =