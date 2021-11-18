#!/usr/bin/env python
# coding: utf-8

# In[142]:


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, recall_score, accuracy_score, precision_score, f1_score
from sklearn.linear_model import LogisticRegression
from keras import models
from keras import layers


# In[174]:


#1
spam_df = pd.read_csv('C:\\study\\workspace_python\\pdsample\\datasets\\mydata\spam7.csv')


#2
spam_df['yesno'].replace({'y':1, 'n':0}, inplace = True)

#3

X = spam_df.iloc[:,:-1]
y = spam_df.iloc[:,-1]

#4
scaler = MinMaxScaler()
X = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 1011)

#5
#0의 값이 1의 값에 약 1.53배 많다.
print(len(y[y==0])/len(y[y==1]))

#6 모델 만들기
model = models.Sequential()
model.add(layers.Dense(10, activation = 'relu', input_dim = X_train.shape[1]))
model.add(layers.Dense(10, activation = 'relu'))
model.add(layers.Dense(1, activation = 'sigmoid'))
print(model.summary())

#7 모델 학습 정의, 모델 학습

model.compile(optimizer = 'rmsprop', loss = 'binary_crossentropy', metrics = ['accuracy'])
history = model.fit(X_train, y_train, epochs = 200, batch_size = 128, validation_split = 0.3, class_weight = {0:1,1:1.53})

#8 학습시의 Loss 함수를 그리기
#9 학습시의 정확도 함수를 그리기

history_dict = history.history
history_dict.keys()

loss = history.history['loss']
acc = history.history['accuracy']
val_loss = history.history['val_loss']
val_accuracy = history.history['val_accuracy']
epochs = range(1, len(acc)+1)

plt.plot(epochs, loss, 'bo', label = 'Training loss')
plt.plot(epochs, val_loss,'b', label = 'Validation loss')
plt.xlabel('Epochs')
plt.legend()
plt.show()

plt.plot(epochs, acc, 'bo', label = 'Training accuracy')
plt.plot(epochs, val_accuracy, 'b', label = 'Validation accuracy')
plt.xlabel('Epochs')
plt.legend()
plt.show()

#10
predict_result = model.predict(X_test)
predict_result.shape
predicted_target = pd.Series([1 if predict_result[i] > 0.5 else 0 for i in range(0, predict_result.shape[0])])


#11
accuracy = accuracy_score(y_test, predicted_target)
precision = precision_score(y_test, predicted_target)
f1 = f1_score(y_test, predicted_target)
recall = recall_score(y_test, predicted_target)
print(classification_report(y_test, predicted_target))
print('정확도 : ', accuracy)
print('재현율 : ', recall)
print('정밀도 : ', precision)
print('f1 score : ', f1)

#12
print(confusion_matrix(y_test, predicted_target))

#13
logistic = LogisticRegression()
logistic.fit(X_train, y_train)
pred = logistic.predict(X_test)

#14
print(classification_report(y_test, pred))
print(confusion_matrix(y_test, pred))

