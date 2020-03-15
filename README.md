# Predicting Default on Loans
This is an attempt to predict who will default on loans based on existing customer data. 
This is a kaggle challenge. 
You can find it [here](https://www.kaggle.com/c/credit-default-prediction-ai-big-data/)

## Filling in missing values
The first step is do do something about missing values. 
There is missing data in the columns for salary, experience, delinquency, and credit scores.

### Salary and Experience
My first intuition was that there may be a correlation between Salary and Experience. 
If this were true, we could at-least infer values for Salary or Experience where 1 is missing. 
To test this theory, I removed all records where either was missing and 
plotted Salary vs Experience in a box plot.

The following was the result:

![Default](./viz/SalaryVsExperience.PNG)

As can be seen here, it doesn't look like there is any clear enough link between Salary and Experience
for us to perform an inference. So instead, I decided to fill in the missing values with
the mean of their column. But before that, I will create 2 boolean columns to indicate
whether or not the original Salary and Experience column had missing values as this information
might turn out to be a significant indicator of default.  