# word2vec



컴퓨터가 이해할 수 있게 단어를 표현하는 방식에 대해서 저번에 다루었다.

***시소러스 방식, 통계 기반 방식(동시발생행렬, ppmi)***



이 이외에 다른 방식으로 `추론 기반 방식` 이 있다는 걸 언급했었는데, 이번 장에서는 추론 기반 방식 중 하나인 `word2vec` 에 대해서 살펴볼 것.



<hr>

## 추론 기반 기법과 신경망



`분포 가설` 은 통계 기반 기법의 원리이지만 "추론 기반 기법" 에도 분포 가설은 원리로 작동한다.



### 통계 기반 기법의 문제점



현업에서는 데이터가 너무 크기 때문에 동시발생행렬 혹은 ppmi 를 만들 때 너무 거대한 행렬을 만들게 된다. 이를 svd한다고 한다는 게 실행하기 어렵다.



통계 기반 기법은 모든 데이터를 한꺼번에 사용한다는 점이 있는데, 미니배치 기법은 모든 학습데이터를 사용하지 않고 일부 데이터를 먼저 끄집어내어 학습한다. 즉, 미니배치 학습을 한다.



### 추론 기반 기법 개요



추론 기반 기법에서의 추론 : 



주변 단어(맥락)가 주어졌을 때, 변수 x에 어떤 값이 들어갈지 예측하는 작업



`"you "X" goodbye and I say hello"`



이러한 추론 문제를 반복해서 풀면서 단어의 출현 패턴을 학습하고 문제가 들어오면 정답을 알아맞추는 기법.



우리는 신경망을 사용해서 추론기반 기법을 사용한다.

모델은 맥락 정보를 입력받아 각 단어의 출현 확률을 출력한다.



### 신경망에서의 단어 처리



신경망엥서는 단어를 "you", "say" 있는 그대로 입력값으로 받을 수 없으니 **"고정 길이의 벡터"** 로 변환해야 한다.

대표적인 방식이 `원-핫 인코딩` 방식. 원-핫 인코딩이란 단어를 벡터화 시키는데 벡터의 원소 하나만 1이고 나머지는 0인 인코딩 방식을 의미한다.



예)You say goodbye and I say hello.

단어가 "you","say","goodbye","and","I","say","hello" 로 7개 등장.

그럼 you 단어를 원핫 인코딩 해보면 [1,0,0,0,0,0,0]

또 say 단어를 원핫 인코딩 해보면 [0,1,0,0,0,0,0]



이 작업을 위해서는 단어에 모두 ID 를 부여하고 단어 개수 만큼의 원소를 가진 벡터를 만든 후, 

그 벡터에 그 단어 ID에 해당하는 인덱스만 1을 가지게 하고 나머진 0을 가지게 한다.



원-핫 인코딩 덕에 벡터의 길이는 고정될 수 있게 되었고 그 덕분에 신경망의 입력층은 뉴런 수를 고정할 수 있게 됐다.



"You say goodbye and I say hello." 는 7개의 어휘로 이루어져 있기 때문에 각 어휘를 의미하는 입력층이 하나씩 존재한다. 따라서 7개의 입력층 존재한다.

(즉, 입력값의 속성의 개수가 입력층의 노드 개수)



단어가 벡터로 표현됐으니 신경망을 구축하고 그 값을 넣어볼 수 있다.



```python
import numpy as np

c = np.array([1,0,0,0,0,0,0]) #입력
W = np.random.randn(7,3) #가중치
h = np.matmul(c,W) #중간 노드
print(h)
```



결과가 단순히 W행렬의 1번째 행을 꺼내는 것과 같다.

비효율적이라고 생각되지만 다음 장에서 개선할 사항



## 단순한 word2vec



word2vec 의 모델 중 하나인 CBOW(continuois bag of words) 모델을 살펴볼 예정



### CBOW 모델의 추론 처리



CBOW 모델은 맥락(타겟 주변 단어) 으로부터 타겟 단어를 추론하는 신경망.



CBOW 신경망 모델의 입력은 "맥락"

근데 단어 그 자체로는 신경망은 입력값을 받아들일 수 없다.

따라서 가장 먼저 이 맥락 단어들을 원핫 표현으로 인코딩해서 CBOW 모델이 입력값을 받을 수 있도록 한다.

**"맥락 단어들을 원핫으로 변환"**



그리고 파이썬을 이용해서 완전연결계층으로 CBOW 모델 구축



```python
class MatMul:
    def __init__(self, W):
        self.params = [W]
        self.grads = [np.zeros_like(W)]
        self.x = None
        
    def forward(self,x):
        W, = self.params
        out = np.matmul(x,W)
        self.x = x
        return out
    
    def backward(self,dout):
        W, = self.params
        dx = np.matmul(dout, W.T)
        dW = np.matmul(self.x.T, dout)
        self.grads[0][...] = dw
        return dw
    
    
    
    
#맥락 데이터

c0 = np.array([1,0,0,0,0,0,0])
c1 = np.array([0,1,0,0,0,0,0])

#가중치 초기 설정

W_in = np.random.randn(7,3)
W_out = np.random.randn(3, 7)

#계층 생성

in_layer0 = MatMul(W_in)
in_layer1 = MatMul(W_in)
out_layer = MatMul(W_out)

#순전파

h0 = in_layer0.forward(c0)
h1 = in_layer1.forward(c1)
h = 0.5 * (h0 + h1)
s = out_layer.forward(h)

print(s)

```



각 입력값의 가중합 값 h_k 를 모두 더하고 k로 나눠줘서 h를 얻는다.

그 값을 입력층으로 넣어서 7개의 출력을 얻고, 가장 큰 값이 결과 값.



### CBOW 모델의 학습



CBOW 모델은 출력층에서 각 단어의 점수를 출력했다. SOFTMAX 함수를 사용하면 각 단어가 정답일 확률이 도출된다. 이 확률은 맥락이 있을 때 그 단어가 정답일 확률을 의미한다.



"You say goodbye and I say hello"

앞에서 맥락 단어 입력값은  You 와 goodbye 였다. 정답은 say인데, 신경망이 올바르게 설정되었다면, say 노드 출력층의 점수가 높아야 한다.



이렇게 올바른 점수를 내기 위해서 출력값 점수 집계에 지대한 영향을 끼치는 weight 들을 CBOW 는 학습을 통해서 조정한다.



이러한 맥락 데이터를 통해서 출현 단어를 예측하는 작업은 신경망 분류 작업 중 "다중 클래스 분류" 작업이라고 할 수 있다.

다중 클래스 분류에서 출력 노드에 있는 활성화 함수를 SOFTMAX로 설정하고,  결과값의 손실 함수를 교차 엔트로피 오차를 사용한다. 그리고 이 손실값을 사용해서 학습을 진행한다.



### word2vec 의 가중치와 분산표현



word2vec 을 표현하는 완전연결게층 신경망은 두 유형의 가중치 set를 가진다.

입력 때의 가중치 W_in, 출력 때의 가중치 W_out 이다.

W_in 의 행은 단어의 분산 표현에 해당된다.

W_out 도 단어의 분산 표현을 인코딩학 있는데, 이때는 행렬의 열 방향이 단어의 분산 표현을 나타낸다.



W_in에도 W_out 에도 단어의 분산 표현이 저장되어 있는데 어느 걸 선택하는 게 좋을까?

(선택지는 3가지)



> A 입력층의 가중치만 이용한다.
>
> B 출력층의 가중치만 이용한다.
>
> C 양쪽 가중치를 모두 이용한다.



선택지는 3개인데 C안을 살펴봐야한다.

C안을 구현하는 방법 중 하나는 단순히  W_in 가중치와 W_out 가중치를 더하는 것이다.



word2vec에서 가장 많이 사용하는 안은 A안이다.

우리도 입력층 가중치만 분산 표현으로 이용한다.



<hr>



## 학습 데이터 준비



"You say goodbye and I say hello" 를 사용



### 맥락과 타깃



word2vec CBOW 모델이 사용하는 입력 데이터는 맥락 단어들.

정답 단어는 맥락 단어들 사이에 감싸져 있는 중간에 있는 데이터 '타깃' 단어.

맥락 단어들을 입력했을 때, 타깃 단어가 나올 확률을 높이는 것.



**그러면 맥락 단어 집합과 타깃단어를 뽑는 과정이 필요.**



```python
def create_contexts_target(corpus, window_size = 1):
    target = corpus[window_size:-window_size]
    contexts = []
    
    for idx in range(window_size, len(corpus) - window_size):
        cs = []
        for t in range(-window_size, window_size + 1):
            if t == 0:
                continue
            cs.append(corpus[idx+t])
        contexts.append(cs)
        
        
    return np.array(contexts), np.array(target)


def convert_one_hot(corpus, vocab_size):
    '''원핫 표현으로 변환
    :param corpus: 단어 ID 목록(1차원 또는 2차원 넘파이 배열)
    :param vocab_size: 어휘 수
    :return: 원핫 표현(2차원 또는 3차원 넘파이 배열)
    '''
    N = corpus.shape[0]

    if corpus.ndim == 1:
        one_hot = np.zeros((N, vocab_size), dtype=np.int32)
        for idx, word_id in enumerate(corpus):
            one_hot[idx, word_id] = 1

    elif corpus.ndim == 2:
        C = corpus.shape[1]
        one_hot = np.zeros((N, C, vocab_size), dtype=np.int32)
        for idx_0, word_ids in enumerate(corpus):
            for idx_1, word_id in enumerate(word_ids):
                one_hot[idx_0, idx_1, word_id] = 1

    return one_hot


text = 'You say goodbye and I say hello.'
corpus, word_to_id, id_to_word = preprocessing(text)

contexts, target = create_contexts_target(corpus, window_size = 1)
vocab_size = len(id_to_word)
target = convert_one_hot(target, vocab_size)
contexts = convert_one_hot(contexts, vocab_size)

```



뽑은 맥락 데이토와 타깃 데이터를 원핫 인코딩 해야한다.



```python
def convert_one_hot(corpus, vocab_size):
    '''원핫 표현으로 변환
    :param corpus: 단어 ID 목록(1차원 또는 2차원 넘파이 배열)
    :param vocab_size: 어휘 수
    :return: 원핫 표현(2차원 또는 3차원 넘파이 배열)
    '''
    N = corpus.shape[0]

    if corpus.ndim == 1:
        one_hot = np.zeros((N, vocab_size), dtype=np.int32)
        for idx, word_id in enumerate(corpus):
            one_hot[idx, word_id] = 1

    elif corpus.ndim == 2:
        C = corpus.shape[1]
        one_hot = np.zeros((N, C, vocab_size), dtype=np.int32)
        for idx_0, word_ids in enumerate(corpus):
            for idx_1, word_id in enumerate(word_ids):
                one_hot[idx_0, idx_1, word_id] = 1

    return one_hot


text = 'You say goodbye and I say hello.'
corpus, word_to_id, id_to_word = preprocessing(text)

contexts, target = create_contexts_target(corpus, window_size = 1)
vocab_size = len(id_to_word)
target = convert_one_hot(target, vocab_size)
contexts = convert_one_hot(contexts, vocab_size)

```



다음으로는 간단한 CBOW모델을 구현하고 학습해보는 코드다.



```python
class SimpleCBOW:
    def __init__(self, vocab_size, hidden_size):
        V, H = vocab_size, hidden_size

        # 가중치 초기화
        W_in = 0.01 * np.random.randn(V, H).astype('f')
        W_out = 0.01 * np.random.randn(H, V).astype('f')

        # 계층 생성
        self.in_layer0 = MatMul(W_in)
        self.in_layer1 = MatMul(W_in)
        self.out_layer = MatMul(W_out)
        self.loss_layer = SoftmaxWithLoss()

        # 모든 가중치와 기울기를 리스트에 모은다.
        layers = [self.in_layer0, self.in_layer1, self.out_layer]
        self.params, self.grads = [], []
        for layer in layers:
            self.params += layer.params
            self.grads += layer.grads

        # 인스턴스 변수에 단어의 분산 표현을 저장한다.
        self.word_vecs = W_in

    def forward(self, contexts, target):
        h0 = self.in_layer0.forward(contexts[:, 0])
        h1 = self.in_layer1.forward(contexts[:, 1])
        h = (h0 + h1) * 0.5
        score = self.out_layer.forward(h)
        loss = self.loss_layer.forward(score, target)
        return loss

    def backward(self, dout=1):
        ds = self.loss_layer.backward(dout)
        da = self.out_layer.backward(ds)
        da *= 0.5
        self.in_layer1.backward(da)
        self.in_layer0.backward(da)
        return None
```



모델 생성



```python
import time
import numpy as np
window_size = 1
hidden_size = 5
batch_size = 3
max_epoch = 1000

#텍스트 ID
text = "You say goodbye and I say hello."
corpus, word_to_id, id_to_word = preprocessing(text)

#맥락 데이터, TARGET 데이터 나누기
vocab_size = len(id_to_word)
contexts, target = create_contexts_target(corpus, window_size)

#각 단어 원핫인코딩
target = convert_one_hot(target, vocab_size)
contexts = convert_one_hot(contexts, vocab_size)

model = SimpleCBOW(vocab_size, hidden_size)
optimizer = Adam()
trainer = Trainer(model, optimizer)

trainer.fit(contexts, target, max_epoch, batch_size)
trainer.plot()



```



모델 학습



이제 모델 학습이 모두 끝나고 그래프를 확인해보니 손실값이 학습이 진행됨에 따라서 점점 줄어들고 있음을 확인할 수 있다.

그러면 학습이 끝난 후의 단어의 분산표현을 확인하기 위해서 가중치를 확인가능하다.

앞서 w_in 과 w_out 중에 w_in 가중치의 행을 사용하는 게 일반적임을 살펴봤다.

따라서 w_in 을 확인해보면 각 단어별로 분산표현이 되어 벡터로 표현된다.





## word2vec 보충



### CBOW 모델과 확률



A 현상이 일어날 확률 : P(A)

A,B 현상이 동시에 일어날 확률 : P(A,B)

사후 확률은 P(A|B),



말뭉치 [ W1, W2, W3 .... W_k]  가 있다고 했을 때,

Wt가 타겟이고 WINDOW_SIZE = 1로 했을 때, 맥락 데이터는 Wt-1, Wt+1 이다.

그럼 Wt-1과 Wt+1 이 맥락 데이터일 때, Wt 가 타겟일 확률은 사후확률로 표현하면

`P(Wt | Wt-1,Wt+1)` 

신경망의 문제가 다중 클래스 분류 문제기 때문에 손실함수는 교차 엔트로피 오차 식을 사용한다.

교차 엔트로피 오차 식에 위의 확률 식을 넣으면 도출되는 식은

저 식에 log를 취하고 음수를 취한 값이다.



이걸 말뭉치 전체에 하면 시그마하면서 말뭉치 개수대로 나눈다. 손실값 도출!



CBOW 모델이 하는 일은 이 손실값이 가장 적을 때를 찾는 것.

그리고 가장 적을 때의 입력 가중값을 도출해서 단어의 분산 표현 벡터를 얻는 것.



### skip-gram 모델



word2vec 은 2개의 모델을 제안하고 있다.



1. CBOW
2. skip-gram



skip-gram 은 CBOW 와 반대의 모델.

skip-gram 은 중앙의 단어로부터 주변의 단어를 추측한다.

이 모델의 출력층은 맥락 단어 개수이다.

각 맥락별 손실 값을 구하고 더하면 최종 손실값이다.



그래서 확률변수 측면에서 다시 이를 확률식으로 풀어내면 다음과 같다.



`P(Wt-1, Wt+1 | Wt)` 



이 값을 손실 함수에 집어넣고 그 타겟 데이터일 때의 손실 값을 구한다.

그리고 모든 말뭉치에 관해서 손실 함수 값을 구한다.

가장 손실 값이 적을 때를 찾아서 그 때의 분산표현을 찾는다.



주로 skip-gram 모델을 사용한다.



<hr>

## 통계 기반 vs 추론 기반





단어의 유사성 측면에서는 누가 더 우세하다고 꼭 집어서 이야기 불가.

단어가 갱신됐을 때, 처리 과정은 추론 기반은 가중치 초깃값을 지금껏 해왔던 값으로 사용하면 되는데 통계 기반은 다시 동시행렬을 만들고 그 짓거리 해야 해서 수정 부분에서는 추론 기반이 더 우세.















 





 