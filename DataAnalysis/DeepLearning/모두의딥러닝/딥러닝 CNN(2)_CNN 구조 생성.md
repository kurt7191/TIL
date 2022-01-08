# 딥러닝 CNN(2)_CNN 구조 생성



## 컨볼루션 신경망(CNN)

컨볼루션 신경망은 입력된 이미지에서 `다시 한번 ` 특징을 추출하기 위해서 `커널` 을 사용하는 기법.

다시 한번 특징을 추출.



#### 합성곱



예를 들어서 어떤 이미지 데이터가 4 * 4 의 구조를 가지고 있다고 가정하자.

커널은 하나 생성하는데 그 크기가 2*2 라고 해보자.

커널 각각의 칸 안에는 가중치가 들어가 있다.

2*2커널은 이미지 데이터의 처음부터 한칸씩 좌우, 위아래로 움직이며 원래 있던 값들에서 가중치들을 곱해준다.

그러면 3 * 3 의 행렬이 도출된다.

이렇게 해서 새롭게 만들어진 층을 컨볼루션(합성곱) 이라고 한다.

만일 이러한 커널을 여러 개 생성을 하면 여러 개의 합성곱이 탄생한다.



합성곱 층을 처음에 만들 때도 다중 퍼셉트론을 만들 때처럼 똑같이 input_dim 을 다뤄줘야 한다.

mnist 데이터의 이미지는 28 * 28 흑백의 구조를 가지고 있다. 따라서 input_dim 인자에 (28 ,28,1) 을 넣어준다. 여기서 1의 의미는 흑백인지 색상인지 유무이다. 만일 1이면 흑백이고, 3이면 색상이다.



<HR>

## 맥스 풀링



정해진 풀링 크기 내에서 최댓값을 뽑아내거나 평균 값을 뽑아 내는 것.

주로 맥스 풀링이 많이 사용된다.



합성곱의 크기가 여전히 크면 풀링으로 축소해줘야 한다.



##### 드랍아웃과 플래튼



역시 CNN 에서도 과적합에 대해서 고민해봐야 한다.

과적합에 사용하기 위해서 개발한 방법이 `드랍아웃` 방법이다.

드랍아웃은 은닉층에 배치된 노드들을 임의로 랜덤으로 지정된 %로 꺼주는 역할을 한다.



합성곱과 풀링은 입력 데이터를 2차원으로 다룬다. 본래의 딥러닝 구조에서 절차를 진행하기 위해서는 데이터를 1차원으로 다뤄야 한다. 합성곱과 풀링을 거친 데이터를 1차원으로 펴줘야 하는데 이때 사용하는데

`Flatten()`



밑은 mnist 를 이용한 합성곱 실제 코드



```python
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import sys
import tensorflow as tf


(X_train, Y_train), (X_test, Y_test) = mnist.load_data()
#데이터 전처리
X_train = X_train.reshape(X_train.shape[0],28,28,1) #합성곱과 풀링을 하기 위해서 데이터 reshape 하는 듯
X_train = X_train.astype('float64')
X_train = X_train / 255 #딥러닝은 0 ~ 1 사이의 데이터가 좋음

X_test = X_test.reshape(X_test.shape[0], 28,28,1)
X_test = X_test.astype('float64')
X_test = X_test / 255

#label 전처리
Y_train = tf.keras.utils.to_categorical(Y_train)
Y_test = tf.keras.utils.to_categorical(Y_test)

#신경망 생성

model = Sequential()
model.add(Conv2D(32, kernel_size = (3,3), input_shape = (28,28,1),
                activation = 'relu'))
model.add(Conv2D(64, kernel_size = (3,3), activation = 'relu'))
model.add(MaxPooling2D(pool_size = 2))
model.add(Dropout(0.25)) #25%로 랜덤으로 은닉층을 꺼줌
model.add(Flatten())
model.add(Dense(128, activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation = 'softmax')) #출력층

model.compile(loss = 'categorical_crossentropy',
             optimizer = 'adam',
             metrics = ['accuracy'])

#최적화 모델 생성

MODEL_DIL = './Modle/'
if not os.path.exists(MODEL_DIL):
    os.mkdir(MODEL_DIL)
    
modelpath = './Model/{epoch:02d}-{val_loss:.4f}.hdf5'
checkpointer = ModelCheckpoint(filepath = modelpath, monitor = 'val_loss',
                              verbose = 1, save_best_only = True)
early_stopping_callback = EarlyStopping(monitor = 'val_loss',
                                       patience = 10)

#모델 실행

history = model.fit(X_train, Y_train, validation_data = (X_test, Y_test),
         epochs = 30, batch_size = 200, verbose = 0,
          callbacks = [checkpointer,early_stopping_callback])

print('\n Test Accuracy : %.4f' % (model.evaluate(X_test, Y_test)[1]))

#테스트셋의 오차

y_vloss =history.history['val_loss']
y_loss = history.history['loss']

#그래프 표현

x_len = np.arange(len(y_vloss))
plt.plot(x_len, y_vloss, marker = '.', color = 'red', label = 'Testset_loss')
plt.plot(x_len, y_loss, marker = '.', color = 'blue',label = 'Trainset_loss')
plt.grid()
plt.legend(loc = 'upper right')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.savefig('val_loss vs loss2')
plt.show()

```





