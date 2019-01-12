from sklearn import tree
from cleaningWineData import *
import pandas as pd
import json

#In progress

#create empty data frame
wine_df = pd.DataFrame()

#add liked variable
wine_df['Liked'] = liked
print liked
print price
#add price variable
wine_df['Price'] = price

#add points variable
wine_df['Points'] = points

#add variety variable
wine_df['Variety'] = variety

#add winery variable
wine_df['Winery'] = winery

#add province variable
wine_df['Province'] = province

#add country variable
wine_df['Country'] = country

# print(wine_df)

# string_data = pd.get_dummies(wine_df[['Variety', 'Winery', 'Province', 'Country']])  # get_dummies
# string_data

# join the continuous data with string data using pandas .join()
# wine_data = wine_df[['Price', 'Points']].join(string_data)
# wine_data

# clf = tree.DecisionTreeClassifier()

#fit my decision tree with me new encoded data, and then the target data which was our play column
# clf_train = clf.fit(wine_data, wine_df['Liked'])

# print (tree.export_graphviz(clf_train, None))

# digraph Tree {
# node [shape=box] ;
# 0 [label="X[0] <= 84.5\ngini = 0.459\nsamples = 14\nvalue = [5, 9]"] ;
# 1 [label="X[0] <= 55.0\ngini = 0.375\nsamples = 12\nvalue = [3, 9]"] ;
# 0 -> 1 [labeldistance=2.5, labelangle=45, headlabel="True"] ;
# 2 [label="gini = 0.0\nsamples = 1\nvalue = [1, 0]"] ;
# 1 -> 2 ;
# 3 [label="X[1] <= 37.3\ngini = 0.298\nsamples = 11\nvalue = [2, 9]"] ;
# 1 -> 3 ;
# 4 [label="gini = 0.0\nsamples = 6\nvalue = [0, 6]"] ;
# 3 -> 4 ;
# 5 [label="X[0] <= 70.5\ngini = 0.48\nsamples = 5\nvalue = [2, 3]"] ;
# 3 -> 5 ;
# 6 [label="gini = 0.0\nsamples = 3\nvalue = [0, 3]"] ;
# 5 -> 6 ;
# 7 [label="gini = 0.0\nsamples = 2\nvalue = [2, 0]"] ;
# 5 -> 7 ;
# 8 [label="gini = 0.0\nsamples = 2\nvalue = [2, 0]"] ;
# 0 -> 8 [labeldistance=2.5, labelangle=-45, headlabel="False"] ;
# }

# Running our prediction
# prediction = clf_train.predict([[72, 15.3, 0, 0, 1, 0, 1]])

# print prediction

# array(['yes'], dtype=object)
