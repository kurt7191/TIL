# 게이트가 추가된 RNN





RNN 은 그 구조도 단순하여 구현도 쉬웠지만 단점이 존재한다.

바로 성능이 좋지 않다는 점인데, 그 이유는 멀리 떨어진 장기(long term) 관계를 잘 학습할 수 없기 때문이다.

따라서 이번 장에서는 단순 RNN 성능을 보완한 LSTM 이나 GRU 계층이 쓰인다.



LSTM이나 GRU 는 게이트(gate) 라는 구조가 더해진다.

이 게이트 덕분에 장기 의존 관계를 학습할 수 있다. (멀리 떨어진 단어를 잘 학습할 수 있다.)



<hr>

## RNN 의 문제점



RNN은 장기 의존 관계를 잘 학습할 수 없는데, 그 이유는 기울기 소실 문제가 일어나거나 기울기 폭발 문제가 일어나기 때문이다.

기울기 소실 문제는 오차역전파시 기울기가 소실되는 문제를 의미하고 기울기 폭발 문제는 그 반대로 기울기가 너무 큰 숫자가 되는 것을 의미한다. 두 경우 모두 학습이 제대로 이뤄지지 않는다.



그렇다면 RNN은 왜 이러한 문제가 발생하는걸까?



### RNN 복습



RNN의 구조는



Ht-1 => 그 이전의 히든 스테이트 값

Wh => 그 이전의 출력값을 현재 시각의 출력값으로 바꿔주는 가중치들

Xt => 현재 시각의 입력값

Wt => 현재 시각의 출력값으로 바꿔주는 가중치들

b => 바이어스

tanh => 최종 출력값으로 변환



위와 같은 변수들로 RNN 구조는 형성되어 있는데,

Ht-1 X Wh 를 곱한 값과 Xt X Wt 를 곱한 값을 더하고 바이어스 b를 더해준 값에 tanh 활성화 함수를 넣어줘서 t시각의 Ht값을 얻는다.



### 기울기 소실 또는 기울기 폭발



RNN 구조가 역전파를 할시 어떻게 진행되는지 살펴보자.



`"Tom was watching TV in his room. Mary came into the room. Mary said hi to [ ? ]"`



여기서 이미 순전파를 통해 앞의 단어들이 입력값으로 들어왔다고 가정하고, 정답을 Tom 을 주었다고 해보자. 그리고 역전파를 진행한다고 한다면 기울기가 통과해야될 계산 그래프의 노드는 tanh 과 matmul 함수이다.

matmul 함수는 두 개가 존재하는데 그 중에서 우리는 앞의 시각의 rnn 계층으로 가야하기 때문에, 이전 Ht 값과 Wh 를 곱하는 matmul 을 이용한다.



즉 두 개, tanh 함수일 때의 역전파와 Ht 로서의 matmul 역전파를 고려해야 한다.



### 기울기 소실과 기울기 폭발의 원인



tanh 함수를 미분하면 값이 작아지는데, 역전파시 기울기가 tanh 을 T번 지날 때 마다 T번 기울기가 작아진다.

이러한 이유로 기울기가 너무 작아지게 된다면 학습이 잘 이루어지지 않는다.

이러한 문제를 해결하기 위해서 RNN 구조에 활성화 함수를 tanh 을 사용하지 않고 ReLU 를 사용해서 모델의 성능을 개선한 경우도 있다. ReLU 활성화 함수는 x가 0 이상이면 기울기 값을 그대로 하류로 흘러보내기 때문이다.



다음으로는 matmul 함수이다.

matmul 함수는 똑같은 Wh 가중치 매개 변수 행렬을 RNN 시각의 개수 T만큼 반복한다. 곱셈의 미분은 입력값을 서로 바꾸어 그 이전의 기울기 미분값과 곱해주는데 따라서 dh X Wh^T 로 곱하는 것이다.

근데 T만큼 실제로 곱해보면 기울기가 지수그래프로 급증하는 걸 볼 수 있다. 이게 바로 `기울기 폭발` 이다.

오버플로를 일으켜 nan 값을 일으킨다.

또 Wh 의 초깃값들을 다르게 변경시켜준다면 역으로 기울기가 작아지는 현상이 생긴다. 즉 `기울기 소실` 이 생긴다. 만일 Wh 행렬 특잇값(여러 특잇값 중 최댓값)이 1보다 크면 지수적으로 증가하고, 1보다 작으면 지수적으로 감소할 가능성이 높다.

 

### 기울기 폭발 대책



기울기 폭발 문제를 해결하는 전통적인 기법 `기울기 클리핑(gradient clipping)`.



먼저 기호를 설명 하자면 g^(^) 는 신경망에서 사용되는 모든 매개변수의 기울기를 하나로 모은 걸 의미한다.

예를 들어서 W1 기울기와 W2 기울기가 있을 때, 이 두 매개변수에 대한 기울기 dW1, dW2 를 결합한 값이 g^(^) 이다.



L2노름을 적용한 값이 ||g^(^)|| 이다.

수식은 아래와 같다.



if ||g^(^)|| > threshold:

​	g^(^) = threshold / ||g^(^)|| X g^(^)



만일 L2적용한 g^(^) 가 임계값을 넘긴다면 g^(^) 는 임계값에 l2노름 g^(^) 한 값을 나눠주고 g^(^) 값을 곱해준 값이 된다.

아래는 기울기 클리핑을 구현한 파이썬 코드.



```python
import numpy as np

dW1 = np.random.rand(3,3) * 10
dW2 = np.random.rand(3,3) * 10
grads = [dW1, dW2]

def clip_grads(grads, max_norm):
    total_norm = 0
    for grad in grads:
        total_norm += np.sum(grad ** 2)
    total_norm = np.sqrt(total_norm)
    
    rate = max_norm / (total_norm + 1e-6)
    if rate < 1:
        for grad in grads:
            grad *= rate
            
```



<hr>



## 기울기 소실과 LSTM



앞에서는 기울기 폭발을 개선하기 위한 기울기 클리핑을 살펴봤다.

RNN 에서는 기울기 폭발 뿐만 아니라 기울기 소실도 큰 문제다.

이  문제를 해결하려면 RNN 아키텍처를 근본부터 뜯어 고쳐야 한다.

이때 게이트가 추가된다.

게이트가 추가된 RNN 아키텍처는 많이 제안됐는데 그 중에서 LSTM과 GRU 가 유명하다.



### LSTM 의 인터페이스



RNN 과 LSTM 의 큰 차이점은 LSTM 은 C경로를 추가로 가진다는 점이다. 이 C경로는 기억 셀(memory cell) 이라고 불리며 다음 계층으로는 그 값을 넘기지 않고 LSTM 계층 내에서만 값을 주고 받는다. 반면에 h 경로는 다음 계층으로도 그 값을 보내고, 자기 자신으로도 값을 보낸다.



### LSTM 계층 조립하기



LSTM 은 RNN과 다르게 Ct 가 있음을 살펴봤다. Ct는 현재 시각 t 까지의 기억이 모두 저장되어 있다고 가정한다.

그리고 이 기억을 바탕으로 히튼스테이트(은닉상태) h를 도출한다. 이때 도출한 h 값은 기억 셀 Ct의 모든 원소에 tanh 함수를 적용한 것과 같다.

(이 사실을 토대로 Ct와 h에 대해서 유추해보자면, Ct의 각 원소에 tanh 함수를 적용한 값이 Ht가 되기 때문에, 둘은 원소 수가 동일하다.)

그리고 다음 값들을 도출하기 위해서 Ct, Ht가 입력값으로 들어가서 어떤 계산을 거치게 되고 Ct+1가 출력이 되고, 그리고 또 다시 Ct+1의 각 원소 값에 tanh 을 적용해서 Ht+1 을 도출한다.



**여기서 등장하는 중요한 개념이 `게이트`** 

게이트란 우리말로 문을 의미한다. 문을 열거나 닫거나 하여 데이터의 흐름을 제어한다.

뿐만 아니라 게이트는 흑백 원리로만 작용하는 게 아니라 데이터를 어느 정도만 흐르게 할지 결정할 수 있다.

즉, 게이트를 조금만 열어두거나, 많이 열어두거나 하여 다음 단계로 흘러갈 데이터의 양을 조절할 수 있다.



게이트의 열림 상태는 0 ~ 1사이의 실수로 나타낸다. 만일 1이면 완전 개방하여 100%의 데이터를 흘러가게 한 것이고 0.2이면 20 %의 데이터만 흘러가게 한다.



### output 게이트



LSTM 의 은닉상태 Ht 는 메모리 셀(기억 셀) Ct 의 각각의 원소에 tanh 함수를 적용한 것과 같다고 했다. 즉 tanh(Ct) 가 Ht 라고 했다.

그럼 tanh(Ct) 에 게이트를 적용하는 걸 생각해보자. 즉 tanh(Ct) 의 각 원소에 대해서 그 원소가 다음 은닉 상태 Ht에 얼마나 중요한가를 조정한다.

이 게이트는 다음 은닉 상태 Ht의 출력을 담당하는 게이트므로 output 게이트라고 부른다.



게이트 식은 다음과 같다.



`o = Sigmoid(Xt * Wx(o) + Ht-1 * Wh(o) + b(o))`



여기서 o는 Output 게이트를 의미하는 차원에서의 o이다. 식을 해석하면 t시각의 입력층에 가중치 매개변수 행렬을 곱해주고 그 이전의 은닉상태 값에 가중치 매개변수 행렬 값을 곱해준 값들을 더한 후 바이어스를 더하고 그 값에 시그모이드 함수를 적용한 값이 게이트 값이다.

이렇게 구한 게이트 행렬 값 o를 tanh(Ct) 행렬과 곱해주어 Ht 값을 구한다.



본래 게이트를 넣지 않으면 Ct-1 , Ht-1 과 어떤 계산이 이루어진 이후 Ct가 출현하고, 그 Ct의 각각의 원소에 tanh 함수를 적용해서 Ht 를 구했는데, 어떤 정보가 다음 Ht를 구하는데 중요한지 구별하기 위해서 tanh(Ct) 의 행렬에 o(게이트 값 행렬)를 곱해준다.

이때 게이트 값과의 곱이란 `아다마르 곱(Hadamard product)` 라고도 한다. 이 곱은 행렬의 각 원소별 곱을 의미한다.



> tanh 함수의 출력값은 -1.0 ~ 1.0 사이다. 이 값은 그 안에 인코딩된 정보의 강약 정도를 나타낸다. 그럼 본래 tanh(Ct) 를 하게 되면 각각의 t 시각의 정보의 강약 정도가 나타난다.
>
> 한편 sigmoid 함수는 값은 0.0 ~ 1.0 을 지니며 데이터를 얼마만큼 통과시킬지를 정하는 비율을 뜻한다. 따라서 주로 게이트에는 시그모이드 함수가, 실질적인 정보를 지니는 데이터는 tanh 함수가 활성화 함수로 적용된다.
>
> 실질적인 정보 지닌 데이터 : tanh, 게이트 : sigmoid



### forget 게이트



우리가 다음에 해야 할 일은 기억 셀에 "무엇을 잊을까" 를 명확하게 지시하는 것.

이러한 작업도 게이트를 이용한다.

망각을 담당하는 게이트를 "forget 게이트" 라고 부른다.



forget 게이트 계산 식은 다음과 같다.



`f = Sigmoid(Xt * Wx(f) + Ht-1 * Wh(f) + b(f))`



f값을 구하게 되면 그 이전의 기억 셀 Ct-1과 f를 아다마르 곱, 원소별 곱을 진행하여 Ct 값을 구한다.



### 새로운 기억 셀



forget 게이트를 이용해서 잊어야 할 값들을 모두 잊게 됐다. 이 게이트 가지고는 기억 셀에서 잊는 것밖에 하지 못한다. 새로 기억해야 할 정보를 기억 셀에 추가해야한다. 이러한 작업은 tanh 노드를 추가해서 진행한다.



이 tanh 노드는 게이트가 아니다. 새로운 정보를 기억 셀에 추가하는 것이 목표다. 따라서 simoid 함수가 아니라 tanh 함수가 사용된다. (simoid 함수는 데이터를 얼마만큼 통과시킬지에 관한 비율 수치)

tanh 노드에서 수행하는 계산식은 다음과 같다.



`g = tanh(Xt * Wx(g) + Ht-1 * Wh(g) + b(g))`



tanh 노드에서는 t시각의 입력값과 그 이전의 은닉 상태를 받아서 매개변수값과 바이어스를 고려해 계산을 수행한다. 이 결과값인 g는 f게이트를 거친 Ct-1 과 "더하기" 과정을 거쳐서 새로운 기억을 추가한다.



### input 게이트



마지막으로 g경로에 게이트 하나를 추가할 예정. 여기에 새롭게 추가하는 게이트를 input게이트라고 한다.

input 게이트는 g의 각 원소가 새로추가되는 정보로써의 가치가 얼마나 큰지를 판단한다.

즉, 새로 추가되는 정보를 무비판적으로 받아들이는 게 아니라 적절히 취사선택하는 것이 이 게이트의 역할이다.

input 게이트의 계산식은 다음과 같다.



`i = Sigmoid(Xt * Wx(i) + Ht-1 * Wh(i) + b(i))`



그런다음 새로 생성 g와 i의 원소별 곱을 수행하고 그 결과를 Ct-1 기억 셀에 덧셈해서 추가한다.



### LSTM의 기울기 흐름



지금까지는 LSTM 의 구조를 살펴봤는데, 이 구조가 왜 기울기 손실을 일으키지 않는지 알아봐야 한다.

기억 셀(Memory cell) 에만 집중하여 역전파를 살펴보면 계산 그래프에 나타나는 계산은 "+" 와 "X" 다.

"+" 는 tanh 노드의 값과 input 게이트 값의 곱과의 덧셈을 의미한다. "+" 는 역전파시 하류로 기울기를 그대로 흘려 보낸다. 그러면 남은 계산은 "x"인데, 이 곱하기는 fotget 게이트와 이전 기억 셀 Ct-1 과의 곱을 의미한다.

이때 기울기와 f값과 곱을 진행하는데, 그 이전의 모델 rnn은 Wh^T를 하면서 기울기 소실이 일어난 반면, f값은 계속 t시각마다 달라지기 때문에 기울기 소실이 일어나지 않는다. 이처럼 매번 새로운 게이트 값을 이용하므로 곱셈의 효과가 누적되지 않아 기울기 소실이 일어나기 어려워진다.

결국 forget 게이트가 잊어서는 안된다고 판단한 원소에 대해서는 그 기울기가 약화되지 않은채로 하류로 기울기가 전달된다.



이처럼 LSTM 모델은 장기 의존 관계를 유지하기에 유리하다.



<HR>

## LSTM 구현





앞서 LSTM 의 구조를 설명하면서 살펴본 식들은 공통점이 있는데 바로 "아핀 변환(Affine transformation)" 이다.

아핀 변환이란 행렬 변환과 평행 이동(편향) 을 결합한 형태의 식 xWx + hWh + b 를 의미한다.

네 수식이 이러한 아핀 변환식을 가지고 있는데 이를 한꺼번에 처리할 수 있게 하나의 식으로 만들 수 있다.



즉 네 식에서 사용된 가중치 매개변수 행렬들을 모아서 한 번의 아핀 변환으로 계산하는 것.



`Xt [ Wx(f)  Wx(g) Wx(i) Wx(o)] + Ht-1 [ Wh(f) Wh(g) Wh(i) Wh(o)] + [b(f) b(g) b(i) b(o)]`



즉, Xt * Wx + Ht-1 * Wh + b 인데, Wx, Wh, b 에 위의 리스트 값들이 들어가 있는 것.

이러면 4번을 수행하던 아핀 변환을 단 1번에 끝낼 수 있다.





##### slice 역전파



slice 역전파는 새로운 개념.

slice 노드를 통해 행렬이 4개로 slice 되어서 출력됐는데, 각각의 경로의 기울기들의 합을 해주면 slice역전파 값이 도출된다.

즉 df + di + dg  + do 를 더해주면 dA가 만들어진다.



### Time LSTM 구현

Time LSTM 은 T개분의 시계열 데이터를 한꺼번에 처리하는 계층이다.

이 또한 마찬가지로 역전파를 할 때, Truncated BPTT 를 적용한다. 여러 개의 set별로 끊고 set별로 순전파 역전파를 진행하는데, RNN Truncated BPTT 와 마찬가지로 순전파는 전체 신경망 진행을 그대로 따른다. 역전파만 SET별로 진행한다.  따라서 순전파는 그대로 유지하기 위해, 임의의 인스턴스 변수를 설정하는데 LSTM 같은 경우에는 다음 층에 전달되는 값이 기억 셀과 은닉 상태 두 개가 존재하므로 두 개의 인스턴스 변수를 설정해서 그 안에 순전파 값을 담아둔다.



밑은 Time LSTM 파이썬 구현 코드다.



```python
class TimeLSTM:
    def __init__(self, Wx, Wh, b, stateful = False):
        self.params = [Wx, Wh, b]
        self.grads = [np.zeros_like(Wx), np.zeros_like(Wh), np.zeros_like(b)]
        self.layers = None
        
        self.h, self.c = None, None
        self.dh = None
        self.stateful = stateful
        
    def forward(self,xs):
        Wx, Wh, b = self.params
        N, T, D = xs.shape
        H = ws.shape[0]
        
        self.layers = []
        hs = np.empty((N,T,H),dtype = 'f')
        
        if not self.stateful or self.h is None:
            self.h = np.zeros((N,H), dtype = 'f')
        if not self.stateful or self.c is None:
            self.c = np.zeros((N,H), dtype = 'f')
            
        for t in range(T):
            layers = LSTM(*self.params)
            self.h, self.c = layers.forward(xs[:,t,:], self.h, self.c)
            hs[:,t,:] = self.h
            
        return hs
    
    def backward(self, dhs):
        Wx, Wh, b = self.params
        N, T, H = dhs.shape
        D = Wx.shape[0]
        
        dxs = np.empty((N,T,D), dtype = 'f')
        dh, dc = 0, 0
        
        grads = [0,0,0]
        for t in reversed(range(T)):
            layer = self.layers[t]
            dx, dh, dc = layer.backward(dhs[:,t,:] + dh, dc)
            dxs[:,t,:] = dx
            
            for i, grad in enumerate(layer.grads):
                grads[i] += grad
                
            for i, grad in enumerate(grads):
                self.grads[i][...] = grad
                
                self.dh = dh
                
                return dxs
            
    def set_state(self, h, c = None):
                self.h, self.c = h, c
                
    def reset_state(self):
        self.h, self.c = None, None
        
    
```





## LSTM을 사용한 언어모델 



## RNNLM 추가 개선



### LSTM 계층 다층화



RNNLM 으로 정확한 모델을 만들자고 하면 LSTM 계층을 깊게 쌓아 효과를 볼 수 있다.

1번째 LSTM H 값이 다음 계층으로 이동하는 방식으로 몇 층이든 LSTM 계층을 쌓아올릴 수 있다.



성능이 많이 개선이 되는데 이슈가 남아있다. 바로 과적합 문제다.



### 드롭아웃에 의한 과적합 억제



RNN은 일반 피드포워드 신경망보다 더 쉽게 과적합이 일어난다.

전통적인 과적합 방지 법은 "훈련 데이터의 양을 늘리거나 모델의 복잡도를 줄이는 것"

그 이외에는 모델의 복잡도에 패널티를 주는 정규화도 효과적. 예를 들어서 L2정규화는 가중치가 너무 커지면 패널티를 부여한다.



드롭아웃은 훈련시 몇 개의 뉴런을 무작위로 무시하고 학습하는데 이 또한 하나의 정규화라고 할 수 있다.

보통 활성화 함수 뒤에 드롭아웃 계층을 두어서 과적합을 방지했다.

그럼 RNN모델에서는 드롭아웃 계층을 어디에 두어야 하나?



LSTM 시간방향에 드롭아웃을 두는 것은 정보가 소실되는 문제가 발생하면서 노이즈가 발생한다. 시각에 따라서 계속 노이즈가 축척되기 때문에 시간 방향에 따른 드롭아웃 계층 삽입은 좋지 않다.

따라서 상하 방향으로 드롭아웃을 삽입해야 한다.



하지만 최근 연구에는 상하 방향에 드롭아웃을 삽입하는 것 뿐만 아니라 시계열 방향에도 드롭아웃을 넣을 수 있는 "변형 드롭아웃" 을 제안했고 모델의 성능을 더 높일 수 있었다.



일반적인 원리는, 같은 시계열 계층에 있는 드롭아웃의 필터는 고정시키는 것이다. 각 시각 층이 변해갈수록 본래 지수함수만큼의 정보가 손실이 됐는데, 똑같은 필터만 적용되어 있으니, 지수적으로 손실되는 사태를 피할 수 있다.



### 가중치 공유



예를 들어서 Embedding 계층과 Affine 계층이 가중치를 공유하게 되면, 학습하는 매개변수 수가 크게 줄어드는 동시에 정확도도 향상이 된다.



만일 LSTM 의 은닉 차원의 수를 H 라고 한다면 Embedding 가중치 매개변수 행렬은 V X H 이고 Affine 계열 가중치 형상은 H X V 다. 가중치를 공유할 때 Embedding 가중치 형상을 전치하여 공유하면 된다.



가중치를 공유함으로써 학습할 매개변수를 줄인다고 함은 과적합을 억제할 수 있다는 것과 같다.

결국 가중치 공유를 통해서 일석이조의 효과를 낼 수 있다.



### 개선된 RNNLM 구현



LSTM 계층 다층화, 드롭아웃, 가중치 공유 와 같은 RNN언어모델을 향상시킬 수 있는 방법들을 살펴봤다.

이걸 적용하면 더 나은 점수를 획득할 수 있다.

코드 생략















