import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

train = pd.read_csv(os.path.join('./', 'cb.csv'))
test = pd.read_csv(os.path.join('./', 'cb.csv'))
# train.info()


# train.head()

X=train.iloc[:,1:]
Y=train['suicide'].ravel()


#Divide the dataset into training and testing data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=0)
print(Y)

#Fit the training data into the Random Forest Classifier
model=RandomForestClassifier().fit(X_train, Y_train)
predict = model.predict(X_test)
print("Efficiency is :")
print(accuracy_score(predict, Y_test)*100) 