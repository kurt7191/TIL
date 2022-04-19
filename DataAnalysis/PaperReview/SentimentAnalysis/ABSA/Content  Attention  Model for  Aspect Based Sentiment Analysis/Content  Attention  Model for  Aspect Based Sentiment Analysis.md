# Content  Attention  Model for  Aspect Based Sentiment Analysis



## Abstract



- 논문의 저자들은 기존의 content attention 기반 ABSA 연구에 대해서 문제 의식을 가지고 있다.

- 기존의 연구들은 대부분 문장 내에 주어진 aspects 들에 대한 단어들과의 연관성을 고려하지 않고 sentiment words 과 shift(??) 를 식별하는데 초점을 둔다.

- 따라서 기존의 연구들은 복잡한 문장 구조를 가지는 문장이다 multi aspects를 가지고 있는 문장에 대해서는 충분히 잘 다루지 못한다.

- 논문의 저자들은 이를 타파하기 위해서 aspect 기반 감성 분류 모델에 기반한 새로운 content attiention 모델을 제안한다. 두 개의 attention 메커니즘과 함께한다.
  - sentence-level content attention mechanism
    - 전역적인 관점(global perspective)으로부터 주어진 aspect 에 대한 중요한 정보를 포착하는게 가능하다.
  - context attention mechanism
    - 단어들의 순서와 그들은 상관 관계를 동시에 고려한다.
    - `customized memories` 시리즈에 그것들(단어들?을 의미하는듯)을 임베딩하면서...



<hr>

## Introduction



- ABSA 의 주요 목적은 주어진 개체들에서 aspects 들을 추출하는 것과 각각의 aspect 에 대한 감성 표현을 결정하는 것이다.

- 논문의 저자들은 aspect 기반의 감성 분류 문제에 대해서 집중한다.

  - 주 목적은 특정 측면에 대한 트윗, 코멘트로 전달되어지는 사용자의 의견이 긍정적이냐 부정적이냐 중립적이냐를 결정하는 것이다.
  - semeval 데이터에서 가져온 하나의 예시
    - Looking around, I saw a room full of New Yorkers enjoying a real meal in a real restaurant, not a clubhouse of the fabulous trying to be seen
    - 이 문장의 aspect 들은 `room`, `meal`,`clubhouse` 등등이라고 할 수 있는데, 이 aspect 들에 대해 긍정인지 부정인지 중립인지에 대한 분류 작업을 시행한다.

- context words들이 주어진 aspect 에 대한 감성 극성과 관련 있어 보이지만, 많은 경우에는 contexst words 들의 일부들만이 주어진 aspect 에 대한 감성 극성과 관련이 있다.

  - 위의 리뷰의 예시를 사용하자면, 위의 리뷰에서 aspect 는 room, meal, clubhouse 등등이 있었다. 
  - aspect meal 에 대한 감성 극성을 나타내는 관련있는 단어는 enjoying 이며, 이는 context word 가 분석하려고 하는 aspect 에 대한 감성을 잘 나타내주는 것처럼 보인다.
  - 그러나 context word 중에는 fabulous 가 있는데, 이는 meal aspect 에 대한 감성 분석을 나타내고 있는 것처럼 보이지 않는다.
  - 만일 감성 분류 모델이 aspect words 들을 구분하지 못한다면 특정 사용에 문제가 된다.

- 이러한 문제점을 해결하기 위해서 attention based model 이 많이 나타났는데, 공통적으로 문제점이 있다고 저자는 이야기한다.

- ##### 첫 번째 문제

  - 대부분의 이 분야의 attention modeling은 주어진 aspect 에 대한 각각의 context word의 공헌도와 관련성을 고려하지 않고 문장에 있는 context 정보의 일부분만을 고려한다.
  - 심각한 문제가 될 수 있는데,  sentiment words 들과 shifters 들이 초점이 맞춰질 수도 있지만 전부다 주어진 aspect 와 관련이 있는건 아니기 때문. 
  - 즉 context word 들이 주어진 aspect 에 대한 감성을 잘 잡아낼 수도 있지만 모든 context word 들이 잘 잡아내는건 아니기 때문이다.
  - 예시
    - The mini's body hasn't changed since late 2010 - and for a good reason.
    - 주어진 aspect 는 `body` 인데, attention 모델을 통해서 `n't`, `good`, `late` 와 같은 단어들이 `focused words` (aspect의 감성을 설명해주는 단어를 이와 같이 표현하는 거 같다.) 포착될 수 있다.
    - 포착된 focused word 들은 부정(negative) 감정을 담고 있다.
    - 하지만 이에 대해서 이 단어들 중에 `good` 만이 진정 `body` aspect 의 감성 극성과 관련 있다고 이야기 할 수 있고, 올바르게 전달된 감성은 긍정(positive)이 되어야 한다고 말할 수 있다.
    - 본 논문의 연구에서는 `short-sighted behavior`이 분류기의 예측 정확도에 중대한 손실을 일으킨다고 주장한다.

- ##### 두 번째 문제

  - 현존하는 attention 모델들은 문장에 의해서 전달되어진 전반적인 의미를 계산하지 않고 `words-level` level 만을 고려한다.
  - 특정 사용자들에서 보이는 풍자적이거나 아이로닉한 주장들과 같은 복잡한 문장들을 위해서, 전체 문장에 관한 더 정확한 정보가 올바른 results 를 예측하기 위해서 필요하다.
  - 예시
    - Maybe the mac os improvement were not the product they want to offer
    - 이는 명백하게 `mac os` 제품에 대한 부정적인 리뷰를 담고 있는 아이로닉한 문장이지만, 대부분의 attention model 은 `improvement` 에 대해서 높은 가중치를 주게 되고 긍정(positive) 로 예측하는 경향을 보인다.

- ##### 세 번째 문제

  - 문장(sentence) 는 주어진 topic에 대해서 multiple aspect를 포함하고 있을 것이다.

  - 따라서 각 단어(나는 focused word, 또는 context word들로 이해했다.) 는 주어진 aspect에 따라서 다른 중요도를 문장 내에서 가질 수 있다.

  - 이전의 작업들도 물론 이 작업에 대해서 고려했는데 널리 펴져 있는 hidden state 기반, memory 기반의 모델을 이용해서 해결하려고 했다.

    > 1. Attention-based LSTM for aspect-level sentiment classification.

    

- ##### 해결 방안

  - ##### sentence level content attention mechanism

    - 첫 번째 문제와 두 번째 문제를 해결하기 위해서 `sentence level content attention mechanism` 을 사용했다.

    - attention weight를 계산하기 위해서 문장 내에서 aspect 와 각각의 단어들에 의해서 전달된 정보들만 고려하지 않고 full sentence의 전체 의미를 고려할 것이다.

    - > Aspect 와 그 주변 단어의 의미만을 고려하지 않을 것이다. 문장의 의미도 고려할 것이다.

    - 이 모델의 이름을 sentence-level content attention moduls(SAM) 이라고 부른다.

    - SAM 모델은 전역적인 관점으로부터 주어진 aspect 에 대한 중요한 정보를 포착할 수 있다. 그리고 전체 문장을 output embedding vecor 로 임베드 할 수 있다.

    - 이 output embedding vector 는 aspect에 특화된 sentence representation 으로 여겨질 수 있다.

  - ##### context attention mechanism

    - 세 번째 문제점을 해결하기 위해서 context attention mechanism 을 사용했다.
    - 단어 시퀀스의 순서만을 고려하는 게 아니라 단어들과 aspect간의 상관관계를 계산한다.
    - 이를 context attention based memory mudule의 약자인 CAM 으로 표현한다.
    - CAM 은 `customized memory` 를 각각의 aspect에 제공한다. 이는 시퀀셜한 방법에서 업데이트될 수 있다.

- Contribution
  - Content attention based aspect based sentiment classification(cabasc) 를 발전
  - 위에서 설명한 의미론적 mismatch 문제를 해결하기 위해서 두 개의 attention model mechanism 을 사용. 그리고 성능 평가
  - 역시나 SemEval 데이터 셋, twitter 데이터 셋 사용
  - 성능이 높아졌다.



> model frame work



![스크린샷 2022-04-19 오후 8.18.04](/Volumes/GoogleDrive/내 드라이브/타이포라_source/스크린샷 2022-04-19 오후 8.18.04.png)

