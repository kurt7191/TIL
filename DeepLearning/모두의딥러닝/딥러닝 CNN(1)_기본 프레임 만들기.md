# 딥러닝 CNN(1)_기본 프레임 만들기



먼저 이미지에 대한 딥러닝 기본 프레임을 mnist 데이터 셋을 이용해서 만들어 보겠다.



데이터 전처리 과정



```python
from tensorflow.keras.datasets import mnist

#이미지 데이터를 X로 이미지에 0~9까지 이름 붙인 걸 Y_class 로 지정.
#그리고 학습 데이터와 테스트 데이터 나눔.

(X_train, Y_class_train),(X_test, Y_class_test) = mnist.load_data

#학습 데이터와 테스트 데이터 개수를 파악

print('학습 데이터 개수 : {}'.format(X_train.shape[0]))
print('테스트 데이터 개수 : {}'.format(X_test.shape[0]))

#이미지 데이터 보기

import matplotlib.pyplot as plt

plt.imshow(X_train[0], cmap = 'Greys') #Greys 는 흑백을 의미
plt.show()

import sys
#이미지는 28 * 28로 이루어져 있음, 이미지의 밝기에 따라서 각 픽셀은 0 ~ 255 사이의 숫자를 부여받음, 즉, 숫자로 이루어진 28 * 28 행렬임

#이를 시각화

for x in X_train[0]:
    for i in x:
        sys.stdout.write('%d\t' % i)
    sys.stdout.write('\n')
    

#데이터가 (x,y,z) 로 이루어져 있음. 이미지가 2차원이라서 삼차원 데이터 구조를 가지는 것.
#딥러닝에 집어 넣기 위해서 이미지를 1차원으로 바꿈, 즉, 784개의 속성을 가진 구조로 바꿈

X_train = X_train.reshape(X_train.shape[0], 784)

#데이터 정규화
#최댓값 255 라서 255로 나누어 0 ~ 1사이의 숫자로 변환
X_train = X_train.astype('float64')
X_train = X_train/255

X_test = X_test.reshape(X_test.shape[0], 784)
X_test = X_test.astype('float64')
X_test = X_test/255

#label 데이터 전처리
#9개의 label 가지고 있는데 0, 1의 데이터를 가지게 원-핫 인코딩

import tensorflow as tf

Y_train = tf.keras.utils.to_categorical(Y_class_train)
Y_test = tf.keras.utils.to_categorical(Y_class_test)

```



이미지 데이터셋은 (x,y,z) 의 구조를 가지고 있다.

이미지 하나는 2차원 구조로 28 *28 형식이다. 또한 각 픽셀은 밝기에 따라서 0 ~ 255 사이의 숫자를 부여받는다.

딥러닝에 데이터를 집어넣고 레이블을 예측하기 위해서는 데이터셋 구조를 2차원 구조로 바꿔줘야 한다. (x,y) => 즉 x개의 행과 y개의 속성을 가진 구조로.

따라서 (x, 784) 로 reshape 한다.



딥러닝은 데이터 셋이 0 ~ 1 사이의 숫자로 되어 있어야 좋은 성능을 발휘한다.

따라서 최댓값인 255로 X_train 데이터와 X_test 데이터를 나누어 준다.



레이블 또한 0,1 둘 중하나로 되어 있으면 좋다. 따라서 원-핫 인코딩 해준다.



다음으로는 모델 생성과 파라미터 설정



```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential()
model.add(Dense(512, input_dim =  784, activation = 'relu'))
model.add(Dense(10, activation = 'softmax'))

model.compile(loss = 'categorical_crossentropy',
             optimizer = 'adam',
             metrics = ['accuracy'])

import os
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

MODEL_DIR ='./Model/'
if not os.path.exists(MODEL_DIR):
    os.mkdir(MODEL_DIR)
    
modelpath = "./model/{epoch:02d}-{val_loss:4f}.hdf5"
checkpointer = ModelCheckpoint(filepath = modelpath, monitor = 'val_loss',
                              verbose = 1, save_best_only = True)
early_stopping_callback = EarlyStopping(monitor = 'val_loss',patience = 10)

history = model.fit(X_train, Y_train, validation_data = (X_test, Y_test), epochs = 30, batch_size = 200, verbose = 0,
                   callbacks = [early_stopping_callback, checkpointer])

print("\n Test Accuracy: %4f" % (model.evaluate(X_test, Y_test)[1]))
```



512개의 노드를 가진 은닉층 생성

앞서 데이터셋의 구조가 속성은 784개 가진 데이터 셋이였음, 따라서 입력층의 정보를 input_dim 에 넣어줌.

활성화 함수는 back propagation을 할 때 기울기 소실 방지를 위해 relu 함수를 사용.



출력층은 0~9까지의 숫자를 예측해야 하기 때문에 softmax 활성화 함수를 사용하고 10개의 노드를 사용.



최적의 모델을 찾기 위해서 keras callback 모듈을 사용.

ModelCheckpoint 사용시, val_loss 를 기준으로 최고의 모델을 찾는다.

EarlyStopping을 사용시 val_loss를 기준으로 10번이상 오차가 줄어들지 않으면 학습을 중지한다.

(과적합 방지를 위해서)



다음으로는 학습 데이터에서의 오차와 테스트 데이터에서의 오차를 그래프로 표현



```python
import matplotlib.pyplot as plt
import numpy as np

#테스트 데이터 오차
y_vloss = history.history['val_loss']

#학습셋의 오차

y_loss = history.history['loss']

#그래프로 표현

x_len = np.arange(len(y_loss))
plt.plot(x_len, y_vloss, marker = '.', c = 'red', label = 'Testset_loss')
plt.plot(x_len, y_loss, marker = '.', c = 'blue', label = 'Trainset_loss')

#그래프에 그리드를 주고 레이블을 표시

plt.legend(loc = 'upper right')
plt.grid()
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()
```





![loss vs val_loss](C:/Users/user/Desktop/TIL/DeepLearning/%EB%AA%A8%EB%91%90%EC%9D%98%EB%94%A5%EB%9F%AC%EB%8B%9D/image/loss%20vs%20val_loss.png)



7번째 epoch 부터 val_loss 가 변화가 없음.

따라서 7번째까지 학습한 모델이 최적의 모델이라고 할 수 있음.

ModelCheckpoint 객체를 통해서 저장했기 때문에 그 모델을 지정된 dir 에서 확인하고 불러올 수 있음.

최종 Test set 에 대한 Accuracy : 0.9787



이는 은닉층 하나를 사용한 단순 딥러닝 구조.

더 깊게 은닉층을 설정해서 성능을 높일 수 있다.

바로 이미지 딥러닝에서 강력한 CNN을 다음 장에서 볼 것.



