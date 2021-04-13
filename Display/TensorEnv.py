import tensorflow
import keras
import numpy as np
import pandas as pd
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle

data = pd.read_csv("new_load_data.csv", sep=",")
data = data[["Data","Time","Load"]]

predict = "Load"

X = np.array(data.drop(["Load"],1))
y = np.array(data[predict])

x_train,x_test, y_train, y_test = sklearn.model_selection.train_test_split(X,y, test_size=0.2)

linear = linear_model.LinearRegression()
linear.fit(x_train,y_train)
accuracy = linear.score(x_test,y_test)
print(accuracy)
