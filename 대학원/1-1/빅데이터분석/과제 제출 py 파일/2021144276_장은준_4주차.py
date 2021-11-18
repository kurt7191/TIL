#!/usr/bin/env python
# coding: utf-8

# # scikit-learn lab 1

# In[16]:


import pandas as pd


# In[89]:


from sklearn.datasets import load_breast_cancer

#1번
breast_cancer = load_breast_cancer()

#2번
print(breast_cancer.target_names)
print(breast_cancer.target)

#3번

cancer_data = breast_cancer.data
cancer_target = breast_cancer.target
breast_df = pd.DataFrame(cancer_data,columns =  breast_cancer.feature_names)
breast_df['target'] = cancer_target
print(breast_df)
breast_df


# In[44]:


data


# In[59]:


#4번

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

target = breast_cancer.target
data = breast_cancer.data

X_train, X_test, y_train, y_test = train_test_split(data, target, test_size = 0.3, random_state = 156)

tree = DecisionTreeClassifier()
tree.fit(X_train,y_train)
pred = tree.predict(X_test)
accuracy = accuracy_score(pred,y_test)
print(accuracy)


# In[62]:


#5번

from sklearn.model_selection import KFold
import numpy as np

n_iter = 0
fold = KFold(n_splits = 5)
metrics_list = []
tree = DecisionTreeClassifier()

for train_index, test_index in fold.split(data):
    X_train, X_test = data[train_index], data[test_index]
    y_train, y_test = target[train_index], target[test_index]
    
    #학습 및 예측 그리고 평가
    
    tree.fit(X_train, y_train)
    pred = tree.predict(X_test)
    n_iter += 1
    
    accuracy = accuracy_score(pred, y_test)
    metrics_list.append(accuracy)
    
    
    
    
print(metrics_list) 
print(np.mean(metrics_list))


# In[76]:


skfold = StratifiedKFold(n_splits=3)
n_iter=0
cv_accuracy=[]

# StratifiedKFold의 split( ) 호출시 반드시 레이블 데이터 셋도 추가 입력 필요  
for train_index, test_index  in skfold.split(breast_cancer.data, breast_cancer.target):
    # split( )으로 반환된 인덱스를 이용하여 학습용, 검증용 테스트 데이터 추출
    X_train, X_test = breast_cancer.data[train_index], breast_cancer.data[test_index]
    y_train, y_test = breast_cancer.target[train_index], breast_cancer.target[test_index]
    #학습 및 예측 
    tree.fit(X_train , y_train)    
    pred = tree.predict(X_test)

    # 반복 시 마다 정확도 측정 
    n_iter += 1
    accuracy = np.round(accuracy_score(y_test,pred), 4)
    train_size = X_train.shape[0]
    test_size = X_test.shape[0]
    print('\n#{0} 교차 검증 정확도 :{1}, 학습 데이터 크기: {2},검증 데이터 크기: {3}' 
          .format(n_iter, accuracy, train_size, test_size))
    print('#{0} 검증 세트 인덱스:{1}'.format(n_iter,test_index))
    cv_accuracy.append(accuracy)
    
# 교차 검증별 정확도 및 평균 정확도 계산 
print('\n## 교차 검증별 정확도:', np.round(cv_accuracy, 4))
print('## 평균 검증 정확도:', np.mean(cv_accuracy))


# In[81]:


#7번

from sklearn.model_selection import cross_val_score

cross = cross_val_score(tree, breast_cancer.data, breast_cancer.target)
cross


# # scikit-learn lab 2

# In[139]:


from sklearn.datasets import load_boston

#1번
boston = load_boston()
#2번
boston_df = pd.DataFrame(data = boston.data, columns = boston.feature_names)

#3번
boston_df['CHAS_STR'] = 0
boston_df['CHAS_STR'] = boston_df['CHAS'].astype(str)


# In[140]:


#4번
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

encoder = LabelEncoder()
a = encoder.fit_transform(boston_df['CHAS_STR'])
boston_df['CHAS_L_ENCODE'] = a

#5번c

one_hot_results = pd.get_dummies(boston_df['CHAS_STR'])
new_boston_df = pd.concat([boston_df,one_hot_results], axis = 1)



# In[144]:


#6번

scaler = StandardScaler()
boston = load_boston()
boston_df = pd.DataFrame(data = boston.data, columns = boston.feature_names)
names = boston.feature_names.tolist()

for i in names:
    boston_df[i] = scaler.fit_transform(boston_df[[i]])
    

boston_s_scaled = boston_df
boston_s_scaled.describe()


# In[152]:


#7번

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
boston_m_scaled = boston_df
for i in names:
    boston_m_scaled[i] = scaler.fit_transform(boston_m_scaled[[i]])
    
boston_m_scaled.describe()


# In[ ]:




