import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sn
data=pd.read_csv('googleplaystore.csv')
print(data)
print(data.columns)
print(data.Category.unique())
print(data.Category.value_counts())
print(data.describe())
print(data.dtypes)
print(data['Content Rating'].value_counts())
print(data.Genres.value_counts())
print(data.Rating)
ratings=data.Rating.isna().sum()
print(ratings)
'''data.Rating=data.Rating.fillna(data.Rating.mean())
sn.barplot(data.Rating)
plt.show()'''
from sklearn.preprocessing import LabelEncoder
lab=LabelEncoder()
data['App']=lab.fit_transform(data['App'])
data['Category']=lab.fit_transform(data['Category'])
data['Size']=lab.fit_transform(data['Size'])
from sklearn.neighbors import KNeighborsClassifier
while True:
    print('press-"1" for 4.5''\n'
          'press-"2" for 4.6''\n'
          'press-"3" for 4.7''\n'
          'press-"4" for 4.8''\n'
          'press-"5" for 4.9 and 5.0''\n'
          'type-"okay-one for okay one"''\n'
          'type-"not likely viewed"''\n')
    inp=input('enter the quality number:-> ')
    if inp=="1":
        o4_5=data[(data['Rating'] ==4.5)]
        colms=o4_5.columns.values
        for i in range(len(o4_5)):
            data=o4_5.iloc[i].values
            print(colms, " : ",data)
    elif inp=="2":
        o5_5=data[(data['Rating'] ==4.6)]
        colms = o5_5.columns.values
        for i in range(len(o5_5)):
            data11 = o5_5.iloc[i].values
            print(colms, " : ")
            print(data11)
    elif inp=="3":
        o6_6=data[(data['Rating']==4.7)]
        colms = o6_6.columns.values
        for i in range(len(o6_6)):
            data44 = o6_6.iloc[i].values
            print(colms, " : ", data44)
    elif inp=="4":
        o7_7=data[(data['Rating'] > 4.8)]
        colms = o7_7.columns.values
        for i in range(len(o7_7)):
            data21 = o7_7.iloc[i].values
            print(colms, " : ")
            print(data21)
    elif inp=="5":
        o8_8=data[(data['Rating'] == 5.0)]
        colms = o8_8.columns.values
        for i in range(len(o8_8)):
            data66 = o8_8.iloc[i].values
            print(colms, " : ", data66)
    elif inp=="okay-one for okay one":
        o1=data[(data['Rating'] > 3.0) &(data['Rating'] <4.0)]
        colms = o1.columns.values
        print(o1)
        for i in range(len(o1)):
            data = o1.iloc[i].values
            print(colms, " : ", data)
    elif inp=="not likely viewed":
        o2=data[(data['Rating'] < 2.5)]
        colms = o2.columns.values
        for i in range(len(o2)):
            data1 = o2.iloc[i].values
            print(colms)
            print("'\n':'")
            print(data1)