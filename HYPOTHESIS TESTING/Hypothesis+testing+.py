#importing the pacakages which are required 
import pandas as pd
import numpy as np
import scipy 
from scipy import stats
import statsmodels.api as sm

#install plotly package 
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.tools import FigureFactory as FF

#Mann-whitney test 
data=pd.read_csv("C:/Users/suri/Desktop/practice programs/Hypothesis testing/with and without additive.csv")

#doing Normality test for Mann whitney
#without additive Normality test
withoutAdditive_data=stats.shapiro(data.Without_additive)
withoutAdditive_pValue=withoutAdditive_data[1]
print("p-value is: "+str(withoutAdditive_pValue))

#Additive normality test
Additive=stats.shapiro(data.With_Additive)
Additive_pValue=Additive[1]
print("p-value is: "+str(Additive_pValue))

#Doing Mann-Whiteny test
from scipy.stats import mannwhitneyu
mannwhitneyu(data.Without_additive, data.With_Additive)

#############################End of Mann-whiteny test#####################################

#2- Sample T-Test
#Creditcard Promotion data set 
promotion=pd.read_csv("C:/Users/suri/Desktop/practice programs/Hypothesis testing/Promotion.csv")
#Ho: Avg of purchases made by FIW < = Avg purchases made by SC =>default/ current/ no action
#Ha: Avg of purchases made by FIW > Avg purchases made by SC =>take action 
#Doing Normality test 
#We consider Ho: Data are normal
#We consider Ha: Data are not normal

Promotion=stats.shapiro(promotion.InterestRateWaiver)
Promotion_pValue=Promotion[1]
print("p-value is: "+str(Promotion_pValue))

SDPromotion=stats.shapiro(promotion.StandardPromotion)
SDPromotion_pValue=Promotion[1]
print("p-value is: "+str(SDPromotion_pValue))
#we can proceed with the model 
#Varience test 
scipy.stats.levene(promotion.InterestRateWaiver, promotion.StandardPromotion)

#2 Sample T test 
scipy.stats.ttest_ind(promotion.InterestRateWaiver,promotion.StandardPromotion)

scipy.stats.ttest_ind(promotion.InterestRateWaiver,promotion.StandardPromotion,equal_var = True)
###########################End of 2-Sample T-Test############################################

#One way Anova
#Importing the data set of contractrenewal 
from statsmodels.formula.api import ols
cof=pd.read_csv("C:/Users/suri/Desktop/practice programs/Hypothesis testing/ContractRenewal_Data(unstacked).csv")
cof.columns="SupplierA","SupplierB","SupplierC"

#Normality test 
SupA=stats.shapiro(cof.SupplierA)    #Shapiro Test
SupA_pValue=SupA[1]
print("p-value is: "+str(SupA_pValue))

SupB=stats.shapiro(cof.SupplierB)
SupB_pValue=SupB[1]
print("p-value is: "+str(SupB_pValue))

SupC=stats.shapiro(cof.SupplierC)
SupC_pValue=SupC[1]
print("p-value is: "+str(SupC_pValue))

#Varience Test 
scipy.stats.levene(cof.SupplierA, cof.SupplierB)
scipy.stats.levene(cof.SupplierB, cof.SupplierC)
scipy.stats.levene(cof.SupplierC, cof.SupplierA)

#One-Way Anova

mod=ols('SupplierA~SupplierB+SupplierC',data=cof).fit()
aov_table=sm.stats.anova_lm(mod,type=2)
print(aov_table)
###########################End of One-Way Anova###################################################

#Chi-Square test 
#Importing the data set of bahaman 
Bahaman=pd.read_csv("C:/Users/suri/Desktop/practice programs/Hypothesis testing/Bahaman.csv")
count=pd.crosstab(Bahaman["Defective"],Bahaman["Country"])
count

Chisquares_results=scipy.stats.chi2_contingency(count)
Chi_pValue=Chisquares_results[1]
print("p-value is: "+str(Chi_pValue))

##########################End of chi-square test################################################

#1 Sample Sign Test 
import statsmodels.stats.descriptivestats as sd
#importing the data set of signtest.csv
data=pd.read_csv("C:/Users/suri/Desktop/practice programs/Hypothesis testing/Signtest.csv")
#normality test 
data_socres=stats.shapiro(data.Scores)
data_pValue=data_socres[1]
print("p-value is: "+str(data_pValue))

#1 Sample Sign Test 
sd.sign_test(data.Scores,mu0=0)
############################End of 1 Sample Sign test###########################################

#2-Proportion Test 
two_prop_test=pd.read_csv("C:/Users/suri/Desktop/practice programs/Hypothesis testing/JohnyTalkers.csv")
#importing packages to do 2 proportion test
from statsmodels.stats.proportion import proportions_ztest
#we do the cross table and see How many adults or children are purchasing
tab = two_prop_test.groupby(['Person', 'Icecream']).size()
count = np.array([58, 152]) #How many adults and childeren are purchasing
nobs = np.array([480, 740]) #Total number of adults and childern are there 

stat, pval = proportions_ztest(count, nobs,alternative='two-sided') 
#Alternative The alternative hypothesis can be either two-sided or one of the one- sided tests
#smaller means that the alternative hypothesis is prop < value
#larger means prop > value.
print('{0:0.3f}'.format(pval))
# two. sided -> means checking for equal proportions of Adults and children under purchased
# p-value = 6.261e-05 < 0.05 accept alternate hypothesis i.e.
# Unequal proportions 

stat, pval = proportions_ztest(count, nobs,alternative='larger')
print('{0:0.3f}'.format(pval))
# Ha -> Proportions of Adults > Proportions of Children
# Ho -> Proportions of Children > Proportions of Adults
# p-value = 0.999 >0.05 accept null hypothesis 
# so proportion of Children > proportion of children 
# Do not launch the ice cream shop

###################################End of Two proportion test####################################