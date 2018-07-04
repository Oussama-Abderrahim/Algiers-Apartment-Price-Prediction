#!/usr/bin/env python 

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LassoLarsCV

data = pd.read_csv("dataset1.csv",header=0)

X = data.loc[:,["Commune","Etage","Superficie","Piece"]].values
Y = data.loc[:,"Prix"].values

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2)

regressor = LassoLarsCV(cv=15)
regressor.fit(X_train,Y_train)
score = regressor.score(X_test,Y_test)
print(score)