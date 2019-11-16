# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # mostly used for visualization purposes 

# importing data set using pandas
mba = pd.read_csv("E:\\Bokey\\Excelr Data\\Python Codes\\all_py\\Basic Statistics _ Visualizations\\mba.csv")


# Finding 3rd and 4rth Business Moments
mba.skew()
mba.kurt()
mba['gmat'].skew()
mba['gmat'].kurt()

# Graphical Representation of data
import matplotlib.pylab as plt
# Histogram
plt.hist(mba['gmat']) # left skew 

#Boxplot
plt.boxplot(mba['gmat'])# for vertical
plt.boxplot(mba['gmat'],1,'rs',0)# For Horizontal
help(plt.boxplot)

# Barplot
# bar plot we need height i.e value of each data
# left - for starting point of each bar plot of data on X-axis(Horizontal axis). Here data is mba['gmat']
index = np.arange(773) # np.arange(a)  = > creates consecutive numbers from 
# 0 to 772 

mba.shape # dimensions of data frame 
plt.bar(height = mba["gmat"], left = np.arange(1,774,1)) # initializing the parameter 
# left with index values 

import pandas as pd
import matplotlib.pyplot as plt
mtcars = pd.read_csv("E:\\Bokey\\Excelr Data\\Python Codes\\all_py\\Basic Statistics _ Visualizations\\mtcars.csv")


# table 
pd.crosstab(mtcars.gear,mtcars.cyl)

# bar plot between 2 different categories 
pd.crosstab(mtcars.gear,mtcars.cyl).plot(kind="bar")

import seaborn as sns 
# getting boxplot of mpg with respect to each category of gears 
sns.boxplot(x="gear",y="mpg",data=mtcars)

sns.pairplot(mtcars.iloc[:,0:2]) # histogram of each column and 
# scatter plot of each variable with respect to other columns 

import numpy as np
plt.plot(np.arange(32),mtcars.mpg) # scatter plot of single variable

plt.plot(np.arange(32),mtcars.mpg,"ro-")

help(plt.plot) # explore different visualizations among the scatter plot

# Scatter plot between different inputs

plt.plot(mtcars.mpg,mtcars["hp"],"ro");plt.xlabel("mpg");plt.ylabel("hp")

mtcars.hp.corr(mtcars.mpg)
mtcars.corr()
# ro  indicates r - red , o - points 
# 
# group by function 
mtcars.mpg.groupby(mtcars.gear).median() # summing up all mpg with respect to gear

mtcars.cyl.value_counts()
# pie chart
mtcars.gear.value_counts().plot(kind="pie")

mtcars.mpg.groupby(mtcars.gear).plot(kind="line")
mtcars.gear.plot(kind="pie")
# bar plot for count of each category for gear 
mtcars.gear.value_counts().plot(kind="bar")


# histogram of mpg for each category of gears 
mtcars.mpg.groupby(mtcars.gear).plot(kind="hist") 
mtcars.mpg.groupby(mtcars.gear).count()

# line plot for mpg column
mtcars.mpg.plot(kind='line') 
plt.plot(np.arange(32),mtcars.mpg,"ro-")


mtcars.mpg = mtcars.mpg.astype(str)
mtcars.gear = mtcars.gear.astype(str)
mtcars.groupby(mtcars.gear).count()

mtcars.groupby("gear")["mpg"].apply(lambda x: x.mean())

mtcars.gear.value_counts().plot(kind="pie")
mtcars.gear.value_counts().plot(kind="bar")

mtcars.head()

pd.crosstab(mtcars.gear,mtcars.cyl).plot(kind="bar",stacked=False,grid=True)
plt.scatter(mtcars.mpg,mtcars.wt)
mtcars.plot(kind="scatter",x="mpg",y="wt")
mtcars.mpg.plot(kind="hist")

import seaborn as sns
sns.pairplot(mpg,hue="gear",size=3,diag_kind = "kde")

sns.FacetGrid(mtcars,hue="cyl").map(plt.scatter,"mpg","wt").add_legend()
sns.boxplot(x="cyl",y="mpg",data=mtcars)
sns.FacetGrid(mtcars,hue="cyl").map(sns.kdeplot,"mpg").add_legend()

sns.pairplot(mtcars,hue="gear",size=3)
