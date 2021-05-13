# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataframe
df = pd.read_csv(path)
df.shape
#Code starts here

# calculating the probability of fico
p_a = df[df['fico'].astype(float)>700].shape[0]/df.shape[0]
print(p_a)

# caculating the purpose =='debt_consolidation'
p_b = df[df['purpose']=='debt_consolidation'].shape[0]/df.shape[0]
print(p_b)

#checking for conditional probability
df1 = df[df['purpose']=='debt_consolidation']

# checking for p(A|B)
p_a_b = df1[df1['fico'].astype(float)>700].shape[0]/df1.shape[0]
print(p_a_b)
result = (p_a==p_a_b)
print(result)

# calculating prob_lp

prob_lp = df[df['paid.back.loan']=='Yes'].shape[0]/df.shape[0]
print(prob_lp)

# calculationg prob_cs
prob_cs  = df[df['credit.policy']=='Yes'].shape[0]/df.shape[0]
print(prob_cs)

new_df = df[df['paid.back.loan']=='Yes']

prob_pd_cs = new_df[new_df['credit.policy']=='Yes'].shape[0]/new_df.shape[0]
print(prob_pd_cs)

bayes = (prob_pd_cs*prob_lp)/prob_cs
print("Expected value for bayes",bayes)

df.purpose.value_counts(normalize =True).plot(kind='bar')
plt.title("Probability Distribution for purpose")
plt.xlabel("Purpose")
plt.ylabel("Probability")
plt.show()

#calculating the paid.back.loan== No
df1 = df[df['paid.back.loan']=='No']

df1.purpose.value_counts(normalize=True).plot(kind='bar')
plt.title("Probability Distribution for purpose")
plt.xlabel("Purpose")
plt.ylabel("Probability")
plt.show()

df1.shape

#calculating median for installment
inst_median = df['installment'].median()
print(inst_median)
#calculating mean for installment
inst_mean = df['installment'].mean()
print(inst_mean)
# plotting histogram for installment
df['installment'].hist(bins=60)
plt.axvline(x=inst_median,color='b')
plt.axvline(x=inst_mean,color = 'r')
plt.show()

# plotting histogram for log annual imcome
df['log.annual.inc'].hist(bins=70)
plt.show()


