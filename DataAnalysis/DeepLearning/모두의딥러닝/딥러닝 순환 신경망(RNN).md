# 순환 신경망(RNN)



문장을 학습한다는 것은 지금까지 와는 다르다.

지금까지는 순서와 상관없이 단어의 개수를 세어서 그 글이 긍정적인 글인지 부정적인 글인지와 같은 작업을 진행했다면, 문장은 과거에 들어왔던 데이터와 미래에 들어올 데이터와의 관계를 파악해야만 의미가 전달이 된다.

즉, 데이터 간의 순서를 고려해야만 한다.

즉 딥러닝에 순서에 관계없이 입력되던 것과 달리, 순서를 고려해서 입력되야만 한다.

이를 해결하기 위해서 RNN 이 등장했다.



여러 개의 데이터가 순서대로 입력이 됐을 때, 입력이 됐던 데이터를 잠시 기억해두는 방식이다.

그리고 기억된 데이터가 얼마나 중요한지 가중치를 부여하고 다음 데이터로 넘어간다.

이 가중치가 다음 입력데이터와 관계를 맺고 다음 입력 데이터의 출력에 관여한다.

모든 입력값에 이 작업을 순서대로 진행한다. 따라서 다음층으로 넘어가기 전에 이전 데이터를 다시 확인하므로 같은 층에 멤도는 것처럼 보여서 순환 신경망이라는 이름이 붙여졌다.



**앞서 나온 입력에 대한 결과가 뒤에 나오는 입력값에 영향을 주는 것을 알 수 있다. **



***



예시 문장



"오늘 주가가 어때?"



세 개로 토크나이징 해보면 "오늘", "주가가", "어때" 로 나뉠 수 있다.

즉, 입력 데이터가 오늘, 주가가, 어때 로 세 개가 된다.



"오늘" 입력데이터가 들어가면 그에 맞는 결과1이 나온다. 이를 기억해두었다가, 다음 입력 데이터인 "주가가" 가 입력됐을 때, 결과1과 "주가가" 데이터가 관련되어 결과2가 도출된다.

결국 앞서 나온 입력에 대한 결과가 뒤에 나오는 입력값에 영향을 준다.



이렇게 해야지 비슷한 문장이 들어갔을 때, 그 차이를 구별하여 출력 값에 반영할 수 있다.



예를 들어서 

"어제 주가가 어때?" 와 "오늘 주가가 어때?" 는 입력값이 비슷하지만 그 의미가 다르다.

두 번째 입력값이 "주가" 로 동일하지만 "어제 주가가 어때" 는 그 이전 데이터 "어제" 를 기준으로 계산되어야 하고, "오늘 주가가 어때" 는 "주가가" 이전 데이터인 "오늘" 데이터를 기준으로 계산되어야 한다.



<HR>



하지만 RNN 도 이슈가 발생하는데, 바로 "기울기 소실" 문제다.

LSTM(Long Short Term Memory) 방법이 이를 해결하기 위해 개발됐다.

LSTM 은 기울기 소실 문제를 해결하기 위해서 그 이전 데이터가 반복되기 이전에 다음 층으로 기억된 값을 넘겨야 하는지 넘기지 말아야 하는지 관리하는 단계를 추가한다.



<hr>

## LSTM 이용해서 로이터 뉴스 카테고리 분류



코드를 보면서 해석해가면 자동으로 내용 이해



```python
from tensorflow.keras.datasets import reuters
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, LSTM
from tensorflow.keras.preprocessing import sequence
import tensorflow as tf

# tf.keras.utils.to_categorical()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#빈도가 1~1000개 사이인 단어만 선택해서 불러오며, test 데이터는 20%로 설정
#이미 단어들은 모두 숫자로 레이블링 되어 있다.(빈도를 척도로)

(X_train, Y_train), (X_test, Y_test) = reuters.load_data(num_words = 1000,
                                                        test_split = 0.2)

#데이터 확인하기
category = np.max(Y_train) + 1
print(category, '카테고리')
print(len(X_train), '학습용 뉴스 기사')
print(len(X_test), '테스트용 뉴스 기사')
print(X_train[0]) #이미 레이블링된 상태로 제공

#데이터 전처리

#패딩
x_train = sequence.pad_sequences(X_train, maxlen = 100)
x_test = sequence.pad_sequences(X_test, maxlen = 100)

#원-핫 인코딩

y_train = tf.keras.utils.to_categorical(Y_train)
y_test = tf.keras.utils.to_categorical(Y_test)

#모델 설계하기

model = Sequential()
model.add(Embedding(1000, 100)) #원핫 인코딩 공간 손실 줄이기 위해
model.add(LSTM(100, activation = 'tanh')) #기사당 단어 개수.활성화함수
model.add(Dense(46, activation = 'softmax'))# 46개의 주제 중 하나로 도출되기 때문에

#모델의 컴파일

model.compile(loss = 'categorical_crossentropy',
             optimizer = 'adam',
             metrics = ['accuracy'])

history = model.fit(x_train, y_train, epochs = 20, batch_size = 100,
                   validation_data = (x_test, y_test))

print('테스트 데이터 정확도 : ',model.evaluate(x_test, y_test)[1])

#테스트셋의 오차

y_vloss = history.history['val_loss']
y_loss =history.history['loss']

#그래프로 나타내기

x_len = np.arange(len(y_vloss))

plt.plot(x_len,y_vloss, color = 'red',marker = '.', label='Testset loss')
plt.plot(x_len, y_loss, color = 'blue', marker = '.', label = 'Trainset loss')
plt.grid()
plt.legend(loc = 'upper right')
plt.show()

```



## LSTM + CNN 영화 리뷰 분석





CNN의 합성곱 층과 풀링 층을 추가하여 더 높은 성능을 보이는 모델을 만들려고 한다.

앞선 CNN 은 이미지에서의 CNN 인데, 이미지는 2차원을 가지고 있기 때문에 Conv2D 를 사용했다.

반면에 텍스트는 1차원의 벡터이기 때문에 Conv1D를 사용하려고 한다. Maxpooling1D 도 마찬가지.

본래 Conv2D에서는 커널 크기를 인자로 (X,Y)로 줬는데, Conv1D는 1차원 형식으로만 주면 된다.



코드는 다음



```python
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, LSTM
from tensorflow.keras.layers import Conv1D, MaxPooling1D
from tensorflow.keras.layers import Dropout, Activation
from tensorflow.keras.datasets import imdb

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

#빈도를 기준으로 데이터 단어들이 레이블링 되어있고,
#빈도 1 ~ 5000개의 단어만 가져오기

(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words = 5000)

#데이터 전처리
#레이블 데이터는 이진 분류 문제이기 때문에(긍정, 부정) 원-핫 인코딩 불필요

x_train = sequence.pad_sequences(x_train, maxlen = 100)
x_test = sequence.pad_sequences(x_test, maxlen = 100)

#모델 설계하기

model = Sequential()
model.add(Embedding(5000, 100))
#꼭 원핫 인코딩 하지 않아도, 전처리 과정에서
#데이터 크기가 달라졌다면 활용
model.add(Dropout(0.5))
model.add(Conv1D(64, 5, padding = 'valid', activation = 'relu',
                strides = 1))
model.add(MaxPooling1D(pool_size = 4))
model.add(LSTM(100,activation = 'tanh'))
model.add(Dense(1))
model.add(Activation('sigmoid'))
model.summary()

model.compile(loss = 'binary_crossentropy',
             metrics = ['accuracy'],
             optimizer = 'adam')

history = model.fit(x_train, y_train, validation_data = (x_test, y_test), epochs = 5, batch_size = 100)

y_vloss = history.history['val_loss']
y_loss = history.history['loss']

x_len = np.arange(len(y_vloss))
plt.plot(x_len, y_vloss, color = 'red', marker = '.', label = 'Testset_loss')
plt.plot(x_len, y_loss, color = 'blue', marker = '.', label = 'Trainset_loss')
plt.grid()
plt.legend(loc = 'upper right')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()

```



여기서 나는 Embedding 층이 원-핫 인코딩 때문에만 사용할지 알았는데, 그것 뿐만 아니라

데이터 전처리 과정을 통해 입력된 값을 받아 다음 층으로 알아들을 수 있는 형태로 변환하는 역할도 한다.





