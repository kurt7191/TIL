# 순환 신경망(RNN)



지금까지 우리가 살펴봤던 신경망은 모두 피드포워드(feed forward) 신경망이다.

피드포워드 신경망은 값의 흐름이 단방향인 신경망을 의미한다.



하지만 피드포워드 신경망은 시계열 데이터의 성질이나 패턴에 대해서 제대로 학습할 수 없다.

따라서 그 대체로 등장한 신경망이 "순환 신경망(RNN)" 이다.



<HR>

## 확률과 언어 모델



### word2vec을 확률 관점에서 바라보다.



말뭉치 W가 있다고 가정해보자. 말뭉치 W는 [w1, w2, w3, wt-1, wt, wt+1, w....] 로 이루어져 있다고 하자.

word2vec 은 타깃단어를 맥락 단어들로 추론하는 방법을 사용한다.

타깃단어를 wt 라고 정하고 맥락 단어들을 wt-1, wt+1 로 정한다. 즉, wt-1, wt+1 이 주어졌을 때, wt를 추론하는 방식이다.

이를 확률적으로 표현하면 사후 확률로 나타낼 수 있고 다음과 같다.



`P(wt | wt+1, wt-1)` 



지금까지 word2vec 의 맥락 단어들을 고려할 때 윈도우가 좌우로 나아감을 전제했다. 그런데, 우리는 윈도우가 한쪽 방향으로만 나아가는 상황을 전제할 수 있다. 한쪽 상황으로 윈도우 크기가 2인 경우의 사후 확률은 아래와 같다.



`P(wt | wt-1, wt-2)`



이 확률 또한 교차 엔트로피 손실함수에 집어 넣을 수 있으며, 이 값이 최저가 되게끔 하는 가중치 매개변수를 찾는 게 CBOW 모델의 목적이다. 손실값이 최저게 되는 가중치 매개변수의 값을 찾고 이 값을 이용해서 각 단어의 분산 표현을 찾을 수 있다.



이렇게 CBOW가 단어의 맥락으로부터 타깃을 추론하는 과정을 이용해서 단어의 분산 표현을 부산물로 얻었는데, CBOW의 본래 목적인 "맥락으로부터 타깃을 추측하는 것" 은 어디에 사용될 수 있을까?

즉, P(wt | wt-2, wt-1) 은 어디에 사용될 수 있을까? 이때 등장하는 게 `언어 모델` 이다.



### 언어 모델



**언어 모델(Language model)** 은 **단어 나열**에 확률을 부여한다.

예를 들어서 you say goodbye 라는 단어 시퀸스에는 높은 확률, 예를 들어서 0.092를 출력하고

you say good die  라는 단어 시퀸스에는 낮은 확률 0.00000032 를 출력하는 게 일종의 언어 모델.

(즉, 단어 나열(시퀸스)에 확률을 부여하는 게 일종의 언어 모델.)



언어 모델은 다양하게 사용될 수 있는데, 기계 번역과 음성 인식이 대표적이다.

그리고 언어 모델은 새로운 문장을 생성하는 용도로도 사용할 수 있다. (단어 순서의 자연스러움을 확률적으로 평가할 수 있으므로, 다음으로 적합하고 자연스러운 단어를 출력할 수 있다.)

(언어 모델을 이용한 문장 생성은 다음 장에서 살펴볼 것)



그러면 다음으로 언어 모델을 수식으로 나타내보자.

만일 문장 m이 단어 w1, .... ,wm 나열로 이루어져 있다고 가정하면, 이 단어 시퀸스가 일어날 확률은

`P(w1, .... ,wm)` 이다. 이 확률은 여러 사건이 동시에 일어나는 확률인 동시 확률이라고 부르기도 한다.



이 동시 확률은 사후 확률을 이용해서 다르게 표현될 수 있다.

(확률의 `곱셉정리` 이용.) => 곱셉 정리 : P(A,B) = P(B|A) X P(A)



P(Wm | W1 .... Wm-1)  X  P(W1 .... Wm-1)  

=> 

P(Wm | W1 ... Wm-1)  X  P(Wm-1 | W1 .... Wm-2) X P(W1 .... Wm-2)

=>

P(Wm | W1...Wm-1) X P(Wm-1 | W1 .... Wm-2) X P(Wm-2 | W1 .... Wm-3) X P(W1 .... Wm-3)

.

.

.

.



. . . . . . . P(W3 | W2, W1)  X P(W2, W1)

=>

P(W3 | W2, W1) X P(W2 | W1) X P(W1)



동시 확률은 확률의 곱셉정리를 이용해서 위와 같이 사용될 수 있는데,

**결국 동시 확률은 사후 확률의 총곱으로 나타낼 수 있다.**



여기서 주목할 것은 이 사후 확률은 타깃 단어의 왼쪽에 있는 단어들을 조건으로 사용한다는 점이다.

즉 W1 .... Wt-2, Wt-1,Wt, .... 이 있으면 Wt가 타깃 단어라고 할 때 타깃 단어의 왼쪽에 있는 W1 .... Wt-1 까지를 조건으로 사용한다.

  

지금까지의 이야기를 정리하면 우리의 목표는 단어 시퀸스(나는 간편하게 문장이라고 이해함) 의 확률, 즉 동시 확률을 얻는 것.



### CBOW 모델을 언어 모델로?



맥락의 크기를 특정 값에 한정하여 사용할 수 있다.

타깃 단어 왼쪽의 두 단어를 맥락으로 사용하여 근사적으로 나타낼 수 있다.



> 머신러닝이나 통계학에서는 마르코프 연쇄(Markov chain) ,마르코프 모델(Markov model) 라는 말을 자주 사용한다. 마르코프 연쇄란 미래의 상태가 현재의 상태에만 의존해 결정되는 것을 말한다. 만일 이 사상의 확률이 그 직전 N개에 의존해서 결정될 때, "N층 마르코프 연쇄" 라고 부른다. CBOW 모델은 그 직전 2개의 단어에만 의존해서 그 다음 단어가 결정되기 때문에 "2층 마르코프 연쇄" 라고 부를 수 있다.



CBOW 모델을 언어 모델에 적용할 때, 윈도우 길이를 더 늘릴 수 있다. 하지만 그렇다고 해도 문제가 발생한다.

윈도우 크기를 늘린다고 해도 윈도우 크기 이상의 단어들은 무시된다는 점이다.



예를 들어서

`Tom was watching TV in his room. Mary came into the room. Mary said hi to [ ? ].`



여기서 정답은 Tom 이 적절해 보인다.

이때 우리가 Tom 이라고 대답할 수 있는 이유는 앞의 문장에 Tom 이 있음을 알기 때문이다.

하지만 CBOW 를 억지로 언어 모델에 끼운 다음에 윈도우 크기를 10으로 했다면 18번째나 앞에 나오는 Tom 을 확인할 수 없기 때문에 올바른 추론을 할 수 없게 된다.



그렇다면 윈도우 크기를 크게 늘리면 해결할 수 있어 보이는데, 그렇지 않다.

CBOW 모델은 맥락안의 단어 순서가 무시된다는 단점이 있다.



예를들어서 CBOW 모델은 입력층에 단어 벡터가 여러 개일때, 각각 W_in 가중치와 곱한 다음 그 값들이 은닉층에서 더해진다. 따라서 (you, say) 나 (say, you) 라는 맥락을 똑같이 취급한다.

(밑바닥2 그림 5-5)



정리하자면, CBOW 모델을 이용한 언어 모델은 두 가지 문제점을 가진다.

첫 번째는 윈도우 크기 이상의 단어에 대해서는 학습을 할 수 없다는 점이다.

두 번째는 맥락안의 단어 순서를 고려할 수 없다는 점이다.



이러한 단점들을 보완할 수 있는 모델이 바로 순환신경망(RNN) 이다.

순환 신경망은 맥락이 아무리 길어도 전부 기억할 수 있고, 맥락안의 단어의 순서도 고려할 수 있다. 즉, 맥락의 정보를 기억할 수 있다.



<hr>



## RNN이란



RNN은 Recurrent Neural Network 라고 부른다. 직역하면 순환하는 신경망이라고 부른다.



RNN의 핵심은 "순환" 이며, 주목할점은 RNN은 "순환하는 경로(닫힌 경로)" 가 존재한다.

순환 경로 덕에 데이터는 끊임없이 순환할 수 있게 되고, 순환하는 덕에 과거 데이터의 정보를 기억하는 동시에 새로운 데이터를 갱신할 수 있다.



### 순환 구조 펼치기



RNN 계층은 그 계층으로부터의 입력과 1개 전의 RNN 계층으로부터의 출력을 받는다. 그리고 이 두 정보를 바탕으로 현 시각의 출력을 계산한다. 식으로는 다음과 같다.



`Ht = tanh(Ht-1 * Wh + Xt * Wx + b)`



위의 식에서 보는 것처럼 RNN 계층은 가중치가 두 개 존재한다.

이전 계층의 출력을 다음 시각의 출력으로 변환하기 위한 Wh 와 입력 X를 출력 H 로 변환시켜주기 위한 가중치 Wx 이다. 

위의 식의 결과, 시각 t의 출력 Ht 가 된다. 이 값 Ht는 다른 계층을 향해 위쪽으로 출력되는 동시에, 다음 시각의 RNN 계층을 향해 오른쪽으로도 도출된다. 즉, Ht는 두 개로 복사되어 하나는 위로 하나는 오른쪽으로 향한다.



결국 현재 출력 Ht는 이전 출력 Ht-1 에 기초해서 계산됨을 알 수 있는데, RNN 은 결국 H라는 상태를 가지고 있음을 알 수 있다. 따라서 RNN 계층을 "상태를 가지고 있는 계층" 혹은 "메모리가 있는 계층" 이라고 한다.



또한 Ht를 `은닉 상태(hidden state)` 혹은 `은닉 상태 벡터(hidden state vector)` 라고도 부른다.

(Ht는 이전 시각의 출력값과 현재 입력값을 받고 도출된 t시점의 출력값. 이걸 은닉 상태라고도 부름)





### BPTT

(시간 방향으로 펼친 신경망의 오차역전파)



RNN 신경망의 경우도 가로로 펼치게 되면 순전파도 진행할 수 있고, 역전파도 진행할 수 있다.

이때 RNN의 역전파를 `BPTT(Backpropagation Through Time)` 라고 부른다. 이는 시간 방향으로 펼친 신경망의 오차역전파라는 뜻이다.



BPTT 도 문제를 가지는데 시계열 데이터의 시간 크기가 커지면 BPTT 가 소비하는 계산 시간도 늘어나게 되고, 시계열 데이터의 크기가 커지면 역전파시 기울기가 불안정해지는 것도 문제다.



즉, BPTT는 시계열 데이터의 크기가 커질시, 계산 시간이 오래걸린다는 점과 오차역전파시 기울기가 불안정해지는 문제를 가진다.



### Truncated BPTT



큰 시계열 데이터를 다룰 때는 신경망 연결을 적당한 길이로 끊는다.

적당한 지점에서 적당한 크기로 잘라내어 작은 신경망 여러 개로 만든다.



주의할 점은 순전파는 온전한 신경망 그대로 이용을 하고, 역전파 시에만 적당한 크기로 여러 개의 신경망으로 분리하는 작업을 거친다.

(계산 시간이 오래 걸린다는 점과 기울기 소실이 일어난다는 점을 해결하기 위해서)



이렇게 되면 오차역전파시 미래의 블록과는 독립적으로 역전파를 진행할 수 있게 된다.



> 지금까지 미니배치 기법을 사용하면서 데이터의 순서에 상관없이 집어넣었는데, 순환신경망은 데이터를 순서대로 집어넣어야 한다.



예를 들어서 신경망 10개 단위로 시계열 데이터를 나누었다고 가정해보자.

처음에 입력데이터 X0 ~ X9 가 사용될 것이다. 이 데이터를 넣으면서 순전파를 진행하고 은닉 상태 H9 을 얻을 것이다.

그리고 순전파를 기초로 하여 역전파를 진행해서 dX0 ~ dX9, dH0 ~ dH9 까지 구할 수 있다.



그리고 다음 신경망 단위로 나아갈 때도 똑같이 순전파를 진행하고 역전파를 진행하는데, **주의할 점은 순전파는 온전한 신경망 그대로 진행되어야 하기 때문에 그 이전의 신경망 단위의 결과물인 은닉 상태 H9 를 사용한다.**

그렇게 되면 순전파는 끊기지 않고 그대로 이어진다.

역전파는 앞에서와 마찬가지로 진행한다.



### Truncated BPTT 의 미니배치 학습



위에서의 예시는 모두 미니배치 크기가 1일 때이다.

만일 미니배치 크기가 2이면 어떻게 될까?

먼저 앞에 예시 그대로를 받아들여보자.



첫 번째 미니배치 샘플에서는 똑같이 처음부터 10개의 입력값을 사용한다.

하지만 두 번째 미니배치 샘플에서는 시작 위치를 옮겨 10개를 사용한다. 만일 시작위치를 500만큼 옮기게 되면

두 번째 미니배치 샘플에서의 입력 데이터는 X500 ~ 509 일 것이다.



순차적으로 데이터가 들어가야 하기 때문에 첫 번째 미니 배치의 다음 샘플의 입력 값은  X10 ~ X19 일 것이고 두 번째 미니배치 샘플에서의 다음 샘플 입력 값은 X510 ~ X519 일 것이다.



<HR>

## RNN 구현



T개의 시계열 데이터를 받는데,

T개의 입력값과 T개의 히든 스테이트(은닉 상태) 를 가질 수 있게 된다.

이렇게 T개 단계를 한꺼번에 처리하는 RNN을 Time RNN 이라고 부른다(이 책에서는)

한 단계의 작업을 수행하는 계층을 RNN 계층이라고 부른다.



먼저 RNN 계층을 구현하고 한꺼번에 구현 가능한 TimeRNN 을 구현할 것



### RNN 계층 구현

RNN 계층 구현 순전파와 역전파 코드는 아래와 같다.



```python
import numpy as np

class RNN:
    def __init__(self, Wx, Wh, b):
        self.params = [Wx, Wh, b]
        self.grads = [np.zeros_like(Wx), np.zeros_like(Wh), np.zeros_like(b)]
        self.cache = None #역전파시 사용할 중간 데이터
        
    def forward(self, x, h_prev):
        Wx, Wh, b = self.params
        t = np.matmul(h_prev, Wh) + np.matmul(Wx, x) + b
        h_next = np.tanh(t)
        
        self.cache = (x, h_prev, h_next)
        
        return h_next
    
    def backward(self, dh_next):
        Wx, Wh, b = self.params
        x, h_prev, h_next = self.cache
        
        dt = dh_next * (1 - h_next ** 2)
        db = np.sum(dt, axis = 0)
        dwh = np.matmul(h_prev.T, dt)
        dh_prev = np.matmul(dt, Wh.T)
        dWx = np.matmul(x.T, dt)
        dx = np.matmul(dt, Wx.T)
        
        self.grads[0][...] = dWx
        self.grads[1][...] = dWh
        self.grads[2][...] = db
        
        return dx,dh_prev
    
    
```



### TimeRNN 계층 구현



TimeRNN 계층은 T개의 RNN계층으로 이루어져 있다.



```python
class TimeRNN:
    def __init__(self, Wx, Wh, b, stateful = False):
        self.params = [Wx, Wh, b]
        self.grads = [np.zeros_like(Wx), np.zeros_like(Wh), np.zeros_like(b)]
        self.layers = None
        
        self.h, self.dh = None, None
        self.stateful = stateful
        
    def set_stateful(self, h):
        self.h = h
        
    def reset_stateful(self):
        self.h = None
        
    def forward(self, xs):
        Wx, Wh, b = self.params
        N, T, D = xs.shape #N : 미니배치 크기, T : T개 분량의 시계열 데이터, D : 입력 벡터의 크기
        #따라서 입력 데이터 xs 의 형상은 (N,T,D) 이다.
        
        D, H = Wx.shape
        
        self.layers = []
        hs = np.empty((N,T,H), dtype = 'f')
        
        if not self.stateful or self.h is None:
            self.h = np.zeros((N,H), dtype = 'f')
            
        for t in ragne(T):
            layer = RNN(*self.params)
            self.h = layers.forward(xs[:,t,:], self.h)
            hs[:,t,:] = self.h
            self.layers.append(layer)
            
        return hs
    
    def backward(self, dhs):
        Wx, Wh, b = self.params
        N, T, H = dhs.shape
        D, H = Wx.shape
        
        dxs = np.empty((N,T,D), dtype = 'f')
        dh = 0
        grads = [0,0,0]
        
        for t in reversed(range(T)):
            layer = self.layers[t]
            dx, dh = layer.backward(dhs[:,t,:] + dh) #합산된 기울기
            dxs[:,t,:] = dx
            
            for i, grad in enumerate(layer.grads):
                grads[i] += grad
                
        for i, grad in enumerate(grads):
            self.grads[i][...] = grad
            
        self.dh = dh
        
        return dxs
    
    
```



<hr>

## 시계열 데이터 처리 계층 구현





RNN을 사용한 언어 모델은 영어로 RNN Language Model 이다.

이를 줄여서 RNNLM 이라고 칭한다.

RNNLM 완성을 목표로 진행한다.

(RNN을 사용한 언어 모델 완성을 목표로)



### RNNLM 의 전체 그림



일반적인 구조는 다음과 같다.



입력 데이터 (Wx) -> Embedding 계층 -> RNN 계층 -> Affine 계층 -> Softmax 계층



이 구조를 기반으로 해서 각 단어마다의 은닉상태 값을 위쪽으로 보내고 오른쪽으로도 보낸다.

위쪽으로간 히든 스테이트는 Affine 과 softmax 를 거쳐서 다음으로 나올 단어의 확률을 내보내고, 

오른쪽으로 간 히든 스테이트는 다음 값이 결정되는 것에 영향을 끼치게 된다.



### Time 계층 구현



시계열 데이터를 한꺼번에 처리하는 계층을 만든다.

TimeRNN 을 만든 것처럼 TimeEmbedding, TimeAffine 계층을 만든다.

(각 시각마다 개별적으로 데이터를 처리한다.)



다음으로는 시계열 버전의 Softmax 함수를 살펴봐야한다.

Softmax 함수를 구현할 때는 역시 손실 함수도 고려해야 하는데, 다중 분류 문제기 때문에 교차 엔트로피 오차를 사용한다. 따라서 cross entropy loss 계층도 구현한다. 이 둘을 합친 계층을 softmax with loss 계층이라고 부르고 한꺼번에 처리하기 위해서 Time softmax with loss 계층을 만든다.



데이터 각각의 손실함수 값을 모두 더하고 데이터의 개수 T로 나누어주면 전체 Loss 값이 도출된다.



<hr>

## RNNLM 학습과 평가



RNNLM 을 직접 구현하고 학습 시켜본 후 평가를 해보겠다.



### RNNLM 구현



```python
class SimpleRnnlm:
    def __init__(self, vocab_size, wordvec_size, hidden_size):
        V, D, H = vocab_size, wordvec_size, hidden_size
        rn = np.random.randn

        # 가중치 초기화
        embed_W = (rn(V, D) / 100).astype('f')
        rnn_Wx = (rn(D, H) / np.sqrt(D)).astype('f')
        rnn_Wh = (rn(H, H) / np.sqrt(H)).astype('f')
        rnn_b = np.zeros(H).astype('f')
        affine_W = (rn(H, V) / np.sqrt(H)).astype('f')
        affine_b = np.zeros(V).astype('f')

        # 계층 생성
        self.layers = [
            TimeEmbedding(embed_W),
            TimeRNN(rnn_Wx, rnn_Wh, rnn_b, stateful=True),
            TimeAffine(affine_W, affine_b)
        ]
        self.loss_layer = TimeSoftmaxWithLoss()
        self.rnn_layer = self.layers[1]

        # 모든 가중치와 기울기를 리스트에 모은다.
        self.params, self.grads = [], []
        for layer in self.layers:
            self.params += layer.params
            self.grads += layer.grads

    def forward(self, xs, ts):
        for layer in self.layers:
            xs = layer.forward(xs)
        loss = self.loss_layer.forward(xs, ts)
        return loss

    def backward(self, dout=1):
        dout = self.loss_layer.backward(dout)
        for layer in reversed(self.layers):
            dout = layer.backward(dout)
        return dout

    def reset_state(self):
        self.rnn_layer.reset_state()
```



이 코드에서 가중치 매개변수의 초깃값의 랜덤 숫자들의 표준편차를 Xavier 초깃값을 사용했다.

Xavier 초깃값은 이전 노드의 개수 n을 이용해서 표준편차를 1 / 제곱근 n 을 사용한다.



### 언어 모델의 평가(RNNLM 의 평가)



언어 모델을 평가할 때 주로 사용하는 척도는 `퍼플렉서티(perplexity)` , 혼란도를 사용한다.

퍼플렉서티는 간단하게 `확률의 역수` 라고 설명할 수 있다.

you say goodbye and I say hello 를 입력데이터로 가정해보자.

처음 you 단어가 들어왔을 때, 출력값의 확률 분포 값을 그려보자.

say가 확률 0.8을 도출했다면 잘 도출한 모델이라고 할 수 있다.

반면에 say가 확률 0.2를 도출했다면 잘못된 도출한 모델이라고 할 수 있다.



퍼플렉시티는 이 확률의 역수값을 가지게 되는데 즉 1 / 0.8,   1 / 0.2 를 가진다.

이렇게 되면 1 / 0.8 = 1.25, 1 / 0.2 = 5 를 가지게 된다.

이 수치는`분기 수 ` 를 의미하는데, 분기 수란 다음에 취할 수 있는 선택사항의 수를 의미한다.

즉, 1.25는 다음에 선택할 수 있는 단어의 수가 대략 1개임을 의미하며 5는 다음에 선택할 단어의 수가 5가지나 더 남았음을 의미한다.

결국 퍼플렉시티의 값이 작을수록 좋은 모델임을 뜻하고 퍼플렉시티의 값이 클수록 좋지 않은 모델임을 뜻한다.