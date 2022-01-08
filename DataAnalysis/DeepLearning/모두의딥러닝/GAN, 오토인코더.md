# GAN, 오토인코더



## DCGAN



GAN(Generative Adversarial Network), 줄여서 GAN(간) 이라고 부름

한국말론, "생성적 적대 신경망" 이라고 칭함.



GAN 알고리즘 내부에서는 적대적인 경합이 진행된다.

이를 비유하자면

위조 지폐범과, 이를 가려내기 위해 노력하는 경찰의 관계를 비유로 들 수 있다.

위조 지폐범은 진짜 지폐와 똑같은 지폐를 만들어낼 것이고 경찰은 이를 실제 지폐와 비교하여 가짜와 진짜를 구별할 것이다. 

이 둘의 계속된 경합이 점점 더 위조 지폐범이 진짜와 가까운 위조 지폐를 만들 수 있게 돕는다는 원리이다.

페이스북은 GAN 에서 Deep Covolutional GAN 을 개발했는데 이는 GAN 의 엄청난 발전을 도왔고, 이를 DCGAN 이라고 부른다.



<HR>



## 생성자



생성자(Generator) 는 가상의 이미지를 만들어 내는 공장이다.

맨 처음에는 랜덤한 픽셀 값으로 채워진 이미지를 만들고 그 이후에 판별자의 판별 결과에 따라서 지속적으로 

업데이트 하면서 진짜와 가까운 이미지가 완성된다.



DCGAN 은 합성곱을 사용한다고 했는데, 여기서 사용하는 합성곱은 앞서 설명했던 합성곱과 조금 차이가 있다.

우선 최적화 과정이 존재하지 않고(optimizer), 컴파일 과정이 없다.

일부 매개변수를 삭제하는 풀링 과정도 없으며 대신 패딩 과정이 포함되어있다.



패딩 과정이 있는 이유는, 입력 크기와 출력 크기를 맞추기 위함임.

먼저 합성곱 과정을 거치면 연산이 되면서 데이터의 크기가 줄어듬을 우리는 알고 있다.

**생성자가 가짜 이미지를 만들 때 중요한 점은 둘의 크기가 같아야 하는데, 합성곱을 사용하면 데이터의 크기가 달라진다. 따라서 패딩을 이용하여 이미지의 크기를 동일하게 맞추어준다.**



`padding = same` 을 통해서 입력과 출력의 크기가 다를 경우 자동으로 크기를 확장, 확장된 공간에 0을 집어 넣을 수 있다.



<hr>

##### **배치 정규화(Batch Normalizationn)**



패딩 이외에 DCGAN 에서 알아두어야 할, **배치 정규화(Batch Normalizationn)**.



배치 정규화란 입력 데이터의 평균이 0, 분산이 1이 되도록 재배치하는 것.

이는 데이터를 정규 분포로 재배치.

이는 다음 층으로 입력될 값을 일정하게 재배치하는 역할을 한다.



<hr>
**생정자의 활성화 함수**



생성자의 활성화 함수로는 `ReLU()` 함수를 사용한다.

판별자로 넘겨주기 전에는 `tanh()` 함수를 사용한다.

탄젠트 함수는 출력되는 값을 -1과 1사이로 배정한다.



기존 relu가 아니가 LeakyReLU 를 사용



<HR>

## 판별자



생성자가 만든 이미지가 진짜인지 가짜인지 판별하는 판별자는

기존의 CONV 신경망 구조대로 만들면 된다.

왜냐하면 합성곱 신경망 구조 자체가 무엇인가를 구별하는데 사용하는데 최적화 되어있기 때문에.



주의할 점은 판별자는 진짜인지 가짜인지만 판별하지 본인이 직접 학습하면 안된다.

따라서 판별자를 만들 때는 가중치를 저장하는 학습 기능을 꺼줘야 한다.



<hr>

## 적대적 신경망 실행하기



생성자와 판별자를 연결시키고 학습을 진행, 기타 여러 가지 옵션을 설정하는 순서



생성자에서 나온 출력을 판별자에 넣어서 진위여부를 판별하게 만든다는 뜻.



생성자를 G()

판별자를 D()

실제 데이터를 X

입력값을 input



입력값을 받아들인 생성자의 출력 : G(input)

이를 받아들인 판별자 : D(G(input))



판별자는 실제 데이터를 넣은 D(X) 만을 참으로 여긴다.

하지만 G(input) 이 점점 X 와 닮아지면서 판별자가 더는 구별을 잘 못하게 되고

정확도가 0.5로 가까워질질 때 학습을 멈춘다.



이를 코드로 구현하면 밑에와 같다.

코드 주석에 설명을 덧붙였다.



```python
from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Input, Dense, Reshape, Flatten, Dropout
from tensorflow.keras.layers import BatchNormalization, Activation, LeakyReLU, UpSampling2D, Conv2D
from tensorflow.keras.models import Sequential, Model

import numpy as np
import matplotlib.pyplot as plt

#이미지의 크기는 28 * 28

#생성자

generator = Sequential()
generator.add(Dense(128*7*7, input_dim = 100, activation = LeakyReLU(0.2))) #128은 임의로 정한 노드 숫자. 100은 100차원 랜덤 벡터 의미.
#7*7의 이미지의 최초의 크기, 이미지의 크기를 점점 늘린다음에 conv를 지나치게 하는 게 DCGAN 의 특징
generator.add(BatchNormalization()) #데이터를 정규 분포로 만들어준다. (평균 0, 분산 1)
generator.add(Reshape((7,7,128))) #CONV 의 INPUT_SHAPE 에 들어가게끔 설정(행,열, 흑백인지 색상인지)
generator.add(UpSampling2D())
generator.add(Conv2D(64, kernel_size = 5, padding = 'same'))
generator.add(BatchNormalization())
generator.add(Activation(LeakyReLU(0.2))) 
#본래 RELU 는 0보자 작으면 0, 그러나 기울기 소실 문제가 발생, 0보다 작을 때, (0.2) 면 0.2를 곱하라는 의미
generator.add(UpSampling2D())
generator.add(Conv2D(1, kernel_size = 5, padding = 'same',
                    activation = 'tanh'))

#판별자

discriminator = Sequential()
discriminator.add(Conv2D(64, kernel_size = 5, strides = 2, input_shape  = (28,28,1), padding = 'same'))
#strides 를 2를 주면 1보다 더 데이터의 크기가 적어지기 때문에 풀링을 할 필요가 없다.
#생성자와 달리 이미지를 28로 맞출 필요가 없기 때문에 적극적으로 축소 기법을 사용가능.

discriminator.add(Activation(LeakyReLU(0.2)))
discriminator.add(Dropout(0.2))
discriminator.add(Conv2D(128, kernel_size = 5, strides = 2, padding = 'same'))
discriminator.add(Activation(LeakyReLU(0.2)))
discriminator.add(Dropout(0.3))
discriminator.add(Flatten())
discriminator.add(Dense(1, activation = 'sigmoid'))

discriminator.compile(loss = 'binary_crossentropy', optimizer = 'adam')
discriminator.trainable = False #판별이 끝나고 나면 판별자 자신은 학습이 되지 않게 off

#생성자와 판별자 연결 모델

ginput = Input(shape = (100,)) #생성자에 집어넣을 랜덤한 100개의 벡터
dis_output = discriminator(generator(ginput)) #D(G(input)), 생성자가 만든 걸 참과 거짓 판별한 결과
gan = Model(ginput, dis_output) #생성자와 판별자를 연결하는 모델 생성 완성
gan.compile(loss = 'binary_crossentropy', optimizer = 'adam')
gan.summary()

def gan_train(epoch, batch_size, saving_interval):
    
    (X_train,_),(_,_) = mnist.load_data()
    X_train = X_train.reshape(X_train.shape[0], 28, 28,1).astype('float32')
    
    X_train = (X_train -  127.5) / 127.5
    true = np.ones((batch_size,1))
    fake = np.zeros((batch_size,1))
    
    for i in range(epoch):
        #실제 데이터를 판별자에 입력
        
        idx = np.random.randint(0,X_train.shape[0], batch_size)
        imgs  = X_train[idx]
        d_loss_real = discriminator.train_on_batch(imgs, true)
        
        #가상 이미지를 판별자에 입력
        
        noise = np.random.normal(0,1, (batch_size,100))
        gen_imgs = generator.predict(noise)
        d_loss_fake = discriminator.train_on_batch(gen_imgs, fake)
        
        #d_loss_real과 d_loss_fake 가 번갈아 가면서 진위를 판단하기 시작.
        #실제 이미지 넣은 판별자와 가짜 이미지 넣은 판별자의 오차 평균이 판별자의 오차
        
        #판별자와 생성자의 오차 계산
        
        d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)
        g_loss = gan.train_on_batch(noise, true)
        print('epoch:%d' %i, 'd_loss:%.4f' % d_loss, 'g_loss:%.4f'  % g_loss)
    

```



<hr>

## 오토인코더



GAN 이 세상에 존재하지 않은 완전한 가상의 것을 만들어낸 반면에,

오토인코더는 입력 데이터의 특징을 효율적으로 담아낸 이미지를 만들어 낸다.



장점 :



학습 데이터는 본래 현실 세계에 특징을 반영하고 있어야 한다. 그렇지 않고 가상의 특징들이 담겨 있으면, 이 학습 데이터를 통해서 학습한 모델은 예상치 못한 결과를 도출할 것이다.

하지만 오토인코더는 다르다. 오토인코더는 데이터의 특징을 잘 잡아내기 때문에, 그 덕에 부족한 현실 데이터들이 효과적으로 느는 걸 기대할 수 있다.



구조 :



먼저 입력한 이미지와 똑같은 크기로 출력층을 만든다.

입력층보다 적은 수의 노드를 가진 은닉층을 만든다.

이때 소실된 데이터를 복원하기 위해 학습을 시작하고 이 과정을 통해 입력 데이터의 특징을 효율적으로 응축한 새로운 출력이 나온다.





```python
(X_train, _), (X_test, _) = mnist.load_data()
X_train = X_train.reshape(X_train.shape[0], 28, 28,1).astype('float32') / 255
X_test = X_test.reshape(X_test.shape[0],28,28,1).astype('float32')  / 255

#생성자 생성
#인코딩 부분
#차원을 축소하는 인코딩 부분

autoencoder = Sequential()
autoencoder.add(Conv2D(16, kernel_size = 3, padding = 'same', input_shape = (28,28,1), activation = 'relu'))
autoenncoder.add(MaxPooling2D(pool_size =2, padding = 'same'))
autoencoder.add(Conv2D(8, kernel_size = 3, activation = 'relu',
                      padding = 'same'))
autoencoder.add(MaxPooling2D(pool_size = 2, padding = 'same'))
autoencoder.add(Conv2D(8, kernel_size=3, strides = 2, padding = 'same', activation = 'relu'))

#디코딩 부분
#차원을 점차 늘려 입력 값과 똑같은 크기의 출력 값을 내보냄

autoencoder.add(Conv2D(8, kerenl_size = 3, padding = 'same', activation = 'relu'))
autoencoder.add(UpSampling2D())
autoencoder.add(Conv2D(8, kernel_size = 3, padding = 'same', activation = 'relu'))
autoencoder.add(UpSampling2D())
autoencoder.add(Conv2D(16, kernel_size = 3, activation = 'relu'))
autoencoder.add(UpSampling2D()) #3번하면 본래 크기 초과인데 위의 합성곱에서 PADDING = SAME 을 안줬다. 그래서 크기 같음
autoencoder.add(Conv2D(1, kernel_size = 3, padding = 'same', activation = 'sigmoid'))


#컴파일 및 학습

autoencoder.compile(optimizer= 'adam', loss = 'binary_crossentropy')
autoencoder.fit(X_train, X_train, epochs = 50, batch_size = 128,
               validation_data = (X_test, X_test))

random_test = np.random.randint(X_test.shape[0], size=5)
ae_imgs = autoencoder.predict(X_test)


plt.figure(figsize = (7,2))

이하 생략



```



