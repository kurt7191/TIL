# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 23:19:11 2021
Decision Tree

@author: USER
"""
## iris example

from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
iris_data = iris.data
iris_df = pd.DataFrame(data=iris_data, columns=iris.feature_names)
iris_df['label']=iris.target

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test  = train_test_split(iris_df.iloc[:,:4],iris_df.iloc[:,4],test_size=0.20)


from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(criterion = "entropy", max_depth=3)
model.fit(x_train,y_train)
y_pred = model.predict(x_test)

from sklearn.metrics import accuracy_score

accuracy_score(y_test, y_pred)

# Feature Importance

model.feature_importances_

pd.DataFrame({'feature' : x_train.columns,
              'importance' : model.feature_importances_})

import matplotlib.pyplot as plt
import seaborn as sns

dt_importances_values = model.feature_importances_
dt_importances = pd.Series(dt_importances_values,index=x_train.columns  )
dt_top20 = dt_importances.sort_values(ascending=False)[:20]

plt.figure(figsize=(8,6))
plt.title('Feature importances Top 20')
sns.barplot(x=dt_top20 , y = dt_top20.index)
plt.show()

model.classes_

# Breast Cancer data
import pandas as pd

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

cancer = load_breast_cancer()

data_df = pd.DataFrame(cancer.data, columns=cancer.feature_names)

x_train, x_test, y_train, y_test = train_test_split(cancer.data, cancer.target, 
                                                    test_size=0.2 , random_state= 156)

dt = DecisionTreeClassifier(criterion = "entropy", max_depth=3)
dt.fit(x_train,y_train)
y_pred = dt.predict(x_test)


from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
print (' \n confusion_matrix of decision tree \n ')
cm = confusion_matrix(y_test, y_pred)
print (cm)
print ('\n Here is the classification report:')
print (classification_report(y_test, y_pred))

# Random Forest

from sklearn.ensemble import RandomForestClassifier
clf_RF = RandomForestClassifier(n_estimators=10)
clf_RF.fit(x_train, y_train)
y_pred_RF = clf_RF.predict(x_test)

print (' \n confusion_matrix of random foreset \n ')
cm = confusion_matrix(y_test, y_pred_RF)
print (cm)
print ('\n Here is the classification report:')
print (classification_report(y_test, y_pred_RF))

import matplotlib.pyplot as plt
import seaborn as sns

ftr_importances_values = clf_RF.feature_importances_
ftr_importances = pd.Series(ftr_importances_values,index=cancer.feature_names  )
ftr_top20 = ftr_importances.sort_values(ascending=False)[:20]

plt.figure(figsize=(8,6))
plt.title('Feature importances Top 20')
sns.barplot(x=ftr_top20 , y = ftr_top20.index)
plt.show()

# GBM(Gradient Boosting Machine)
from sklearn.ensemble import GradientBoostingClassifier
clf_GBM = GradientBoostingClassifier(random_state=0)
clf_GBM.fit(x_train , y_train)
y_pred_GBM = clf_GBM.predict(x_test)

print (' \n confusion_matrix of GBM \n ')
cm = confusion_matrix(y_test, y_pred_GBM)
print (cm)
print ('\n Here is the classification report:')
print (classification_report(y_test, y_pred_GBM))

import matplotlib.pyplot as plt
import seaborn as sns

ftr_importances_values = clf_GBM.feature_importances_
ftr_importances = pd.Series(ftr_importances_values,index=cancer.feature_names  )
ftr_top20 = ftr_importances.sort_values(ascending=False)[:20]

plt.figure(figsize=(8,6))
plt.title('Feature importances Top 20')
sns.barplot(x=ftr_top20 , y = ftr_top20.index)
plt.show()
