###########################################################
# This file contains forks from the main pipeline that
# were done to help get some insights
###########################################################

import pandas as pd
from util import *

def show_quantified_experience_mean():
    """
    Quantify the experience column and show the mean
    """

    loans = pd.read_csv('./data/3_WithExperienceProvidedColumn.csv')

    quantifiedExperience = loans['Experience'].dropna().apply(experience_str2int)

    print(quantifiedExperience.mean())