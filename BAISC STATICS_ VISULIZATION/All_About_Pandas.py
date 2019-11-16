import pandas as pd 
import numpy as np

orders = pd.read_table("http://bit.ly/chiporders")
user_cols = ["user_id","age","gender","occupation","zip_code"]
movie_users = pd.read_csv("http://bit.ly/movieusers",header=None,sep="|",names = user_cols)
ufo_reports = pd.read_csv("http://bit.ly/uforeports",sep=",")
ufo_reports.head()
type(ufo_reports)
ufo_reports.City
ufo_reports["City"]
type(ufo_reports.City)
ufo_reports["Colors Reported"]
ufo_reports.shape
ufo_reports.head()
ufo_reports.tail()
"this"+"is"+"awsome"
# to create a new series in data frame 
ufo_reports["Location"] = ufo_reports.City+", "+ufo_reports.State
ufo_reports.head()
# IMDB
movies = pd.read_csv("http://bit.ly/imdbratings")
movies.head()
# Descriptive Characteristics of all numerical columns  
movies.describe()
# shape
movies.shape
# data types of objects 
movies.dtypes
type(movies) # Object type 
# to describe the column of type object 
movies.describe(include=["object"])
# renaming columns 
ufo_reports.columns
ufo_reports.rename(columns = {"Colors Reported":"Colors_Reported","Shape Reported":"Shape_Reported"},inplace = True)
ufo_reports.columns
ufo_cols = ["city","colors reported","shape reported","state","time"]
ufo_reports.head
ufo_reports.describe(include=['object'])
ufo_columns = ufo_reports.columns.str.replace(" ","_")
ufo_reports.head()

# to drop columns
ufo_reports.drop("Location",inplace = True,axis=1)
ufo_reports.drop(["City","State"],axis = 1)

# to drop rows 
ufo_reports.drop([0,1],axis=0,inplace=True)
ufo_reports.head()
ufo_reports.shape

# How do i sort pandas data frame or series
movies.head()
# Sort specific column from data frame 
movies.title.sort_values() # dot notation
movies["title"].sort_values()
type(movies["title"].sort_values()) # pandas.core.series.Series
movies.title.sort_values(ascending=False)

# sort the entire data frame with respect to some column
movies.sort_values('title')
movies.sort_values('duration',ascending = False)
movies.head()

# sort with respect to one column and then sort the
# resultant with respect to other column
movies.sort_values(['content_rating','duration'])
# filter rows of data frame by some column value 
movies.head()
movies.shape
type(True)
booleans = []   
for i in movies.duration:
    if i >= 200:
        booleans.append(True)
    else:
        booleans.append(False)


booleans[1:5]
len(booleans)
is_long = pd.Series(booleans)
is_long.head()
type(is_long)
movies[is_long]

# instead
is_long = movies.duration >=200 # replacement for "for" loop
movies[is_long].head()

# other way
movies[movies.duration >=200]

# pulling out genre which satisfies above condition
movies[movies.duration >=200].genre

# or 
movies[movies.duration >200]['genre']

# how do i apply multiple filter criteria on pandas DF
movies[(movies.duration >=200) & (movies.duration <=300)]
movies[(movies.duration >=200) | (movies.genre == 'Drama') ]

True and False 
movies[(movies.duration >=200) | (movies.duration <=300) | (movies.genre == 'Drama')]

# isin operator 
movies[movies.genre.isin(['Crime','Drama','Action'])]


##### Practice ##### 
import pandas as pd
import numpy as np

movies = pd.read_csv("http://bit.ly/imdbratings")
ufo = pd.read_csv("http://bit.ly/uforeports")
ufo.head()
ufo.columns
ufo.rename(columns={"Colors Reported" : "Colors_Reported","Shape Reported" : "Shape_Reported"},inplace=True)
ufo.columns
ufo_cols = ['City','Colors Reported','Shape Reported','State','Time']
ufo.columns = ufo_cols
ufo.head()
ufo = pd.read_csv("http://bit.ly/uforeports",names = ufo_cols,header=0)
ufo.columns= ufo.columns.str.replace(' ','_')
ufo.columns
ufo.shape
ufo.columns.str.replace("_"," ")
ufo.drop('Colors_Reported',axis=1,inplace = True)
ufo.drop(["City","Time"],axis=1,inplace=True)
ufo.drop([0,1],axis=0,inplace = True)
ufo.head()
ufo.shape
movies
movies.title.sort_values()
movies['title'].sort_values(ascending = True)
movies.sort_values('title')
movies.sort_values('title',ascending=True)
movies.sort_values('duration',ascending = True)
movies.sort_values(['content_rating','duration'],ascending=True)
booleans = []
for i in movies.duration:
    if i > 200:
        booleans.append(True)
    else:
        booleans.append(False)
        

booleans
booleans[0:5]
is_long = pd.Series(booleans)
is_long.head()
movies.genre
movies[is_long]
is_long = movies.duration >= 200
movies[is_long]
movies[movies.duration>=200]['genre']
# .loc allows us to select rows and columns by column labels 
movies.loc[movies.duration >=200,'genre']
#movies[movies.duration >=200].genre
movies.head()
movies.describe(include=['object'])
movies.loc[(movies.duration >=200) | (movies.genre=="Drama"),"genre"]
(movies.duration >200) | (movies.genre=="Drama")

# handling multiple or statements 
movies.genre.isin(['Crime','Drama','Adventure'])
# read only few columns at the time of loading data set 
movies = pd.read_csv("http://bit.ly//imdbratings",usecols = [0,1])
movies.columns
# to select only few rows at the time of loading 
movies = pd.read_csv("http://bit.ly/imdbratings",nrows = 5)

ufo.columns
ufo = pd.read_csv("http://bit.ly/uforeports")
ufo.columns

for index,row in ufo.iterrows():
    print (index,row.State,row.City,row.Time)
    
drinks = pd.read_csv("http://bit.ly/drinksbycountry")
drinks.dtypes
drinks.select_dtypes(include=[np.number]).dtypes
drinks.describe()
drinks.describe(include=['object','float64'])

# axis usage 
drinks.head()
drinks.drop('country',axis=1,inplace=True)
drinks.head()
drinks.drop(2,axis=0,inplace = True)
drinks.head()
drinks.mean()
drinks.mean(axis = 0)
drinks.mean(axis=1).shape
drinks.mean(axis='index')
drinks.mean(axis='columns')

# string methods on pandas data frame 
"upper".upper()
order = pd.read_table("http://bit.ly/chiporders")
order.head()
order.item_name.str.upper()
order.item_name.str.lower()
order.item_name.str.contains('Chicken')
order.choice_description.str.replace('[',' ')
order.choice_description.str.replace('[',' ').str.replace(']',' ')
order.choice_description.str.replace('[\[\]]',' ')

# Changing data type of pandas series 
drinks.dtypes
drinks['beer_servings'] = drinks.beer_servings.astype(float)
drinks.dtypes
drinks = pd.read_csv("http://bit.ly/drinksbycountry",dtype = {'beer_servings':float})
drinks.dtypes
order = pd.read_csv("http://bit.ly/chiporders")
order.head()
order.dtypes
order.item_price.str.replace("$","").mean() # error
order.item_price.str.replace("$","").astype(float).mean()
order.item_name.str.contains("chicken").head()
order.item_name.str.contains("Chicken").astype(float).mean()
order.dtypes
order.item_price.head()
order.item_price.str.replace('$','').astype('float').mean()
order.item_name.str.contains('Chicken').head()
order.item_name.str.contains('Chicken').astype('int').head()

# group by function 
drinks = pd.read_csv("http://bit.ly/drinksbycountry")
drinks.head()
drinks.beer_servings.mean()
drinks.groupby('continent').beer_servings.mean()
drinks.groupby('continent')['beer_servings','spirit_servings'].mean().plot(kind='line')
drinks[drinks.continent=="Africa"].beer_servings.mean()
drinks.groupby('continent').beer_servings.min()
drinks.groupby('continent').beer_servings.agg(['min','max','mean','count'])
drinks.groupby('continent').mean()

# Graphs
import matplotlib.pyplot as plt

drinks.groupby('continent').mean().plot(kind='bar')
drinks.groupby('continent').beer_servings.min().plot(kind='bar')
drinks.head()
drinks.columns
drinks.groupby('continent').mean().plot(kind='line') #not a good plot 
drinks.plot(kind='line') #not a good plot 
##
movies = pd.read_csv("http://bit.ly/imdbratings")
movies.head()

movies.dtypes
movies.describe(include=['object'])
movies.groupby('genre')['star_rating','duration'].mean().plot(kind='bar')
movies.groupby('genre')['star_rating','content_rating'].describe().plot(kind='bar')
movies.genre.value_counts().plot(kind='bar')
movies.genre.value_counts(normalize=True).plot(kind='bar')
movies.genre.value_counts().head()
# to get the unique values 
movies.genre.unique()

# no. of unique values
movies.genre.nunique()

# cross tabulation
pd.crosstab(movies.genre,movies.content_rating).plot(kind='bar')
movies.duration.describe()
movies.groupby('genre').duration.mean()
movies.duration.value_counts().plot(kind='bar')
movies.duration.plot(kind='hist')
movies.genre.value_counts().plot(kind='bar') 

# handling missing values 
ufo = pd.read_csv("http://bit.ly/uforeports")
ufo.head()
ufo.tail()
ufo.isnull().head()
ufo.isnull().sum(axis=0)
pd.Series([True,False,True,True,False,True]).sum()
ufo.isnull().head()
sum(ufo["Colors Reported"].isnull())
ufo.isnull().sum()
ufo[ufo.City.isnull()]
ufo.shape
ufo.dropna(how="any").shape # drop a row if any of its value is missing 
ufo.dropna(how="all").shape # drop a row if all of its value is missing 
# drop rows with respect to some columns
ufo.dropna(subset=['City','Shape Reported'],how="any").shape
# only drop a row if City and Shape has missing rows 
ufo.isnull().sum()
ufo['Shape Reported'].value_counts(dropna=False)
ufo['Shape Reported'].value_counts()
ufo['Shape Reported'].fillna(value='VARIOUS',inplace=True)
ufo['Shape Reported'].value_counts(dropna=False)

# All about pandas indexes 
drinks = pd.read_csv("http://bit.ly/drinksbycountry")
drinks.head()
drinks.index
drinks.columns
drinks.shape
pd.read_table("http://bit.ly/movieusers",header=None,sep="|").head()
drinks[drinks.continent=="South America"]

# changing the index to some existing column inside the dataframe 
drinks.index
drinks.set_index('country',inplace=True)
drinks.head()
drinks.loc['Afghanistan','beer_servings']
# in .loc function we should use only names ....unless if the index values
# are integers then we can use integers inplace of names 

# removing the index name from the data frame 
drinks.index.name=None
drinks.head()

# setting the index name for the data frame 
drinks.index.name='country'

# resetting the index values to integers 
drinks.reset_index(inplace = True)
drinks.head()

drinks.describe()
drinks.describe().index
drinks.describe().columns
drinks.describe().loc["25%","beer_servings"]
# .loc[] first parameter is the row index --- it can be number or row name 
# second paramter must be column name 

# .iloc[] => 
drinks.head()
drinks.set_index('country',inplace=True)
drinks.head()
drinks.continent.head()
drinks.continent.value_counts() # counts each category in the columns\
drinks.index.value_counts()
drinks.continent.value_counts().values
drinks.continent.value_counts()["Africa"]
drinks.continent.value_counts().sort_values(ascending=False).values
# creating a pandas series 
people = pd.Series([3223432,234232],index=["Andhra","Telangana"],name="Deaths")
people.index = ['Mauritania','Tajikistan']
people.head()
drinks.beer_servings * people

# Adding a new column based on series index 
pd.concat([drinks,people],axis=1).head()

# loc,iloc,ix selecting data frame columns  
ufo = pd.read_csv("http://bit.ly/uforeports")
ufo.head()
# .loc
ufo.loc[0, : ] # panda series 
ufo.loc[[1,2,3], : ]
ufo.loc[0:2,:] # inclusive on both sides (0,1,2)
ufo.loc[:, 'City']
ufo.loc[:, "City":"State"].head()
ufo.head(3).drop('Time',axis=1)
ufo[ufo.City=="Oakland"]
ufo.loc[ufo.City=="Oakland","State"]
ufo.iloc[:,[0,3]].head(3) # position 
ufo.iloc[:,0:4].head(5)  # exclusive of 2nd number but inclusive of 1st number
ufo.iloc[0:3,:]
ufo[['City','State']]
ufo.loc[:,['City','State']]
ufo[0:2]
ufo.iloc[0:2,:]
# .ix it is going to mix labels and integers 
drinks = pd.read_csv("http://bit.ly/drinksbycountry",index_col="country")
drinks.head()
drinks.ix["Albania",0]
drinks.ix[1,"beer_servings"]
drinks.ix["Albania":"Andorra",0:2]
ufo.head(10)
ufo.ix[0:2,0:2]

