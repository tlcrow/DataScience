# A prodictive model create at Thinkful's Intro to Data Science seminar

from sklearn import tree
import pandas as pd

#create empty data frame
golf_df = pd.DataFrame()

#add outlook
golf_df['Outlook'] = ['sunny', 'sunny', 'overcast', 'rainy', 'rainy', 'rainy',
                     'overcast', 'sunny', 'sunny', 'rainy', 'sunny', 'overcast',
                     'overcast', 'rainy']

#add temperature
golf_df['Temperature'] = [92, 86, 83, 70, 60, 53, 62,
                         75, 57, 72, 78, 69, 81, 71]

#add humidity
golf_df['Humidity'] = [40.3, 63.1, 35.3, 86.3, 72.4, 22.7, 27.0,
                      80.7, 15.4, 25.1, 18.6, 58.3, 27.2, 39.3]

#add windy
golf_df['Windy'] = ['false', 'true', 'false', 'false', 'false', 'true', 'true',
                   'false', 'false', 'false', 'true', 'true', 'false', 'true']

#finally add play
golf_df['Play'] = ['no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'yes',
                  'yes', 'yes', 'no']

# golf_df

print(golf_df)

one_hot_data = pd.get_dummies(golf_df[['Outlook', 'Windy']])  # get_dummies
one_hot_data

# join the continuous data with one hot data using pandas .join()
golf_one_hot = golf_df[['Temperature', 'Humidity']].join(one_hot_data)
golf_one_hot

clf = tree.DecisionTreeClassifier()

#fit my decision tree with me new encoded data, and then the target data which was our play column
clf_train = clf.fit(golf_one_hot, golf_df['Play'])

print (tree.export_graphviz(clf_train, None))

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
prediction = clf_train.predict([[72, 15.3, 0, 0, 1, 0, 1]])

print prediction

# array(['yes'], dtype=object)
