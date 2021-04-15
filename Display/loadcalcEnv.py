import tensorflow
import keras
import numpy as np
import pandas as pd
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle

data = pd.read_csv("new_load_data.csv", delimiter=",")
data = data[["Year", "Month", "Day", "Hour", "Minute", "Load"]]

predict = "Load"

X = np.array(data.drop([predict], 1))
y = np.array(data[predict])

best = 0
for _ in range(30):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.5)

    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)
    print("Accuracy: \n", acc)
    if acc > best:
        best = acc
   # print('Coefficient: \n', linear.coef_)
  #  prediction = linear.predict(x_test)
   # for x in range(len(prediction)):
    #    print(prediction[x],x_test[x],y_test[x])

#Solar test från williams data
'''
data = pd.read_csv("Tester.csv", sep=";")

data = data[["Month", "Day", "Year", "Time", "Vpv1(V)", "Vpv2(V)", "Temperature(C)", "Today Generation(kWh)", "Total Generation(kWh)"]]

# What we are looking for
predict = "Total Generation(kWh)"

# Returns a new frame without total gen
X = np.array(data.drop([predict], 1))
y = np.array(data[predict])
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.5)

best = 0
for _ in range(30):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.5)

    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)
    print("Accuracy: \n",acc)
    if acc > best:
        best = acc


'''