# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)


#Code starts here
categorical_var = bank_data.select_dtypes(include='object')
categorical_var.shape

numerical_var = bank_data.select_dtypes(include='number')
numerical_var.shape

# creating a new variable and drop the Loan_ID
banks=bank_data.drop(columns='Loan_ID')

banks.isnull().sum()

# Calculating mode 
bank_mode=banks.mode().iloc[0]
bank_mode

banks.fillna(bank_mode, inplace=True)
banks.isnull().sum()

banks.shape

# Craete a pivot table
avg_loan_amount = banks.pivot_table(index=['Gender','Married','Self_Employed'],values=['LoanAmount'],aggfunc=np.mean)

avg_loan_amount['LoanAmount'][1]

loan_approved_se = banks.loc[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y'),["Loan_Status"]].count()

loan_approved_nse = banks.loc[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y'),["Loan_Status"]].count()

#Calcualting the percentage
percentage_se=(loan_approved_se*100/614)
percentage_se
round(percentage_se,2)

percentage_nse =(loan_approved_nse*100/614)
round(percentage_nse,2)

loan_term= banks['Loan_Amount_Term'].apply(lambda x :int(x)/12)
big_loan_term = len(loan_term[loan_term>=25])
big_loan_term

loan_groupby = banks.groupby('Loan_Status')

loan_groupby = loan_groupby['ApplicantIncome','Credit_History']

mean_values=loan_groupby.agg([np.mean])
round(mean_values,2)





