# 규제 선형 모델, 릿지, 라쏘, 엘라스틱넷

> 규제 선형 모델의 개요
>
> 릿지 회귀
>
> 라쏘 회귀
>
> 엘라스틱넷 회귀
>
> 선형 회귀 모델을 위한 데이터 변환



### 규제 선형 모델의 개요



 앞서 종속 변수와 독립 변수의 관계가 곡선의 관계를 가지고 있을 때, 일차 방정식의 관계로 파악한다면 과소적합하게 모델을 만든 것이라고 할 수 있고, 더 큰 다항식의 관계로 파악하게 되면 모델이 복잡해지고 변동성이 커져서 오히려 예측력이 떨어진다는 것을 살펴봤다.

 

 지금까지의 선형 회귀 모델 같은 경우에는 RSS, 비용 함수를 줄이는 것에 초점을 맞춰서 식을 만들었다. 하지만 RSS를 최소화 하는 것에만 초점을 두어 모델을 만드는 경우, 학습 데이터를 과적합하게 학습하여 모델이 필요 이상의 다항식으로 나아가게 되고 회귀 계수가 커지면서 과적합하게 되는 문제를 가진다. 따라서 새로운 기준이 필요하다. 새로운 기준은 RSS를 최소화 하면서 과적합을 방지하기 위해서 회귀 계수 값이 커지지 않도록 하는 방법이다. 그렇다면 비용함수의 목표는 다음과 같이 표현될 수 있다. MIN(RSS(W) + alpha * |W|)

 

 여기서 alpha에 주목해야만 한다. alpha는 회귀 계수 값의 크기 제어를 수행하는 튜닝 파라미터이다. 만일 alpha 값이 0이라면 기존의 RSS를 최소화하는 방향과 똑같다. 그리고 alpha 값이 크다면 회귀 계수 값이 굉장히 커질 것이기 때문에 과적합될 위험이 있다. 따라서 w값을 작게 수정해야 한다. 비용함수는 이를 참조하여 alpha값이 크다면 w크기를 작게 조정한다. 그리고 alpha 값이 작다면 회귀 계수 값이 어느 정도 커져도 과적합 될 위험이 적어진다.

 

 따라서 RSS값을 최소화하면서 과적합되지 않는 alpha의 지점을 찾아야만 한다. alpha를 0에서부터 지속적으로 증가시키면서 회귀 계수(w)의 크기를 감소시킬 수 있다. 이렇게 alpha를 패널티로 부여해서 회귀 계수의 크기를 줄이는 것을 규제(Regularization) 라고 부른다. 규제는 크게 L2방식과 L1 방식으로 나뉜다. L2 규제를 적용한 회귀 모형을 릿지 (RIDGE) 회귀 라고 부른다. L2규제는 W의 제곱에 대해서 alpha로 패널티를 부여한 방식을 말한다. 그리고 L1규제를 적용한 회귀 모형을 라쏘(Lasso) 회귀 라고 부르며 이는, W의 절댓값에 대해서 alpha로 패널티를 부여한 방식이다. L2규제는 위의 설명과 같이 높은 회귀 계수를 보여서 과적합된 회귀 모형에 대하여 회귀 계수의 크기를 줄이는 방식을 취한다. L1규제 같은 경우에는 영향력이 적은 회귀 계수 값을 0으로 변경한다.



### 릿지 회귀

 사이킷런은 Ridge 클래스를 통해 릿지 회귀를 구현한다. 앞서 릿지 회귀는 L2규제를 사용함을 살펴봤다. L2규제는 alpha의 값을 설정하고 과적합하게 커진 회귀 계수를 줄이는 줄이는 규제를 말한다. 다음 릿지 회귀를 이용한 코딩이다.



```python
boston = load_boston()

bostonDF = pd.DataFrame(boston.data, columns = boston.feature_names)
bostonDF

bostonDF['PRICE'] = boston.target
bostonDF

y_target = bostonDF['PRICE']
X_data = bostonDF.iloc[:,:-1]
```

 

먼저 파이썬 내장 데이터 셋인 보스턴 주택 가격 데이터를 불러온다.



```python
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score

ridge = Ridge(alpha  = 10)
neg_mse_scores = cross_val_score(ridge, X_data, y_target,scoring = "neg_mean_squared_error", cv = 5)
rmse_scores = np.sqrt(-1 * neg_mse_scores)
rmse_scores
avg_rmse = np.mean(rmse_scores)


print('5 fold의 개별 Negative mse score : ',np.round(neg_mse_scores,3))
print('5 fold의 개별 rmse score : ', np.round(rmse_scores,3))
print('5 fold의 rmse score의 평균 : {:.3f}'.format(avg_rmse))
```



 릿지 회귀 모형 객체를 생성하고 alpha를 10으로 설정한다. (alpha는 튜닝 파라미터 값). 교차 분석을 통해서 각 fold의 rmse score를 한다. scoring 파라미터가 mean_squared_error가 아니고 neg_mean_squared_error인 이유는 교차 분석 같은 경우에는 점수가 크게 나오면 좋은 것으로 판단하는데, 회귀 모형 같은 경우에는 mse값이 작아야만 한다. 따라서 rmse값을 구할 때 -1 을 곱해주어야 한다. 여기까지 하게 되면 cv=5의 5개의 fold 데이터 셋의 rmse값이 나오게 된다.

 

 그렇다면 다음으로는 alpha값을 조금씩 조정해보면서 rmse값이 어떻게 변화하는지 살펴보도록 하자.



```python
alphas = [0,0.1,1,10,100]

#alpha 리스트 값을 반복하면서 alpha에 따른 rmse 평균 값을 구하기(위의 식 반복)

for alpha in alphas:
    ridge = Ridge(alpha = alpha)
    
    #cross_val_score를 이용해 5개 폴드의 평균 rmse 계산하기
    
    neg_mse_scores = cross_val_score(ridge, X_data, y_target, scoring = "neg_mean_squared_error", cv = 5)
    avg_rmse = np.mean(np.sqrt(-1*neg_mse_scores))
    
    print('alpha가 {} 일 때 5 fold의 평균 rmse는 {:.3f}'.format(alpha, avg_rmse))
```



 순차적으로 집어넣을 alpha값을 리스트로 만들어 놓는다. 그리고 반복문을 사용하여 각 alpha별 rmse값을 구하도록 한다. (각 alpha별 교차 분류 평균 구하기) 결과는 다음과 같다.

 

*alpha가 0 일 때 5 fold의 평균 rmse는 5.829*

*alpha가 0.1 일 때 5 fold의 평균 rmse는 5.788*

*alpha가 1 일 때 5 fold의 평균 rmse는 5.653*

*alpha가 10 일 때 5 fold의 평균 rmse는 5.518*

*alpha가 100 일 때 5 fold의 평균 rmse는 5.330*



```python
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

fig, axs = plt.subplots(figsize  = (18,6), nrows = 1, ncols = 5)

coeff_df = pd.DataFrame()

for pos, alpha in enumerate(alphas):
    ridge = Ridge(alpha = alpha)
    ridge.fit(X_data, y_target)
    
    coeff = pd.Series(data = ridge.coef_, index = X_data.columns)
    colnames = 'alhpa : ' + str(alpha)
    coeff_df[colnames] = coeff
    
    coeff = coeff.sort_values(ascending=False)
    axs[pos].set_title(colnames)
    axs[pos].set_xlim(-3,6)
    sns.barplot(x=coeff.values, y=coeff.index, ax=axs[pos])
    plt.savefig('image.png')
#alpha값이 계속 커질수록 회귀 계수 값이 계속 작아지고 있음을 확인할 수 있다.
```



 각 alpha별 회귀 계수의 정보를 담을 데이터 프레임을 만들고, 반복문을 이용하여 데이터 프레임에 정보를 집어 넣는다. (회귀 계수 정보를 시리즈로 만들고) 그리고 시각화를 하면 다음과 같은 그림이 나타난다.



사진 실종..



 각 변수별 회귀 계수의 크기가 alpha 값이 커질수록 줄어들고 있는 것을 볼 수 있다. 왜냐하면 alpha값이 커질수록 alpha * w의 총 크기가 커지기 때문에 w를 줄여야만 하기 때문이다.



### 라쏘 회귀

라쏘 회귀는 alpha * |w|, 즉 회귀 계수의 절댓값을 규제하는 회귀식을 말한다. 릿지 회귀 같은 경우에는 RSS에만 초점을 맞추어 과적합된 모델의 회귀 계수의 크기를 줄이는 규제를 가하는 반면에 라쏘 회귀 같은 경우에는 계수의 크기가 미미한 값을 0으로 만들어 제외시키는 역할을 한다. 따라서 L1규제는 적절한 피처만 회귀에 포함시키는 피처 선택의 특성을 가지고 있다.



```python
from sklearn.linear_model import Lasso, ElasticNet

#alpha값에 따른 회귀 모델의 폴드 평균 RMSE를 출력하고 회귀 계수값들을 DataFrame으로 반환

def  get_linear_reg_eval(model_name, params=None, X_data_n = None, y_target_n = None, verbose=True):
    coeff_df = pd.DataFrame()
    if verbose : print('#######', model_name, '#######')
    for param in params:
        if model_name == 'Ridge' : model = Ridge(alpha=param)
        elif model_name == 'Lasso' : model =  Lasso(alpha=param)
        elif model_name == 'ElasticNet' : model = ElasticNet(alpha=param, l1_ratio=0.7)
        neg_mse_scores == cross_val_score(model, X_data_n, y_target_n, scoring = 'neg_mean_squared_error', cv = 5)
        avg_rmse =  np.mean(np.sqrt(-1 * neg_mse_scores))
        
        print('alpha가 {}일 때의 rmse 평균은 {:.3f}'.format(param, avg_rmse))
        
        model.fit(X_data_n, y_target_n)
        coeff = pd.Series(data = model.coef_, index = X_data_n.columns)
        colnames  = 'alpha: ' + str(param)
        coeff_df[colnames] = coeff
    return coeff_df
```



릿지 회귀 모형을 만들고 평가하는 방식과 라쏘 모형을 만들고 평가하는 방식은 크게 다르지 않다. 후에 엘라스틱넷 모델도 만들어야 하기 때문에 함수를 만들어서 일괄적으로 처리한다. 



```python
lasso_alphas = [0.07,0.1,0.5,1,3]
coeff_lasso_df = get_linear_reg_eval('Lasso', params = lasso_alphas, X_data_n = X_data, y_target_n = y_target)
```



### 엘라스틱넷 회귀



  엘라스틱넷 회귀는 릿지 회귀와 라쏘 회귀의 규제 방식을 둘 다 사용한다. 라쏘 회귀 같은 경우에는 상관 관계가 없는 피처를 제외시키는 역할을 하는데, 그렇게 되면 회귀 계수가 급격하게 변화하는 현상을 보이게 된다. 따라서 릿지 회귀의 규제인 L2규제를 추가시킨 것이다.



   주의해야할 점은 엘라스틱넷 회귀의 alpha값은 릿지 회귀와 라쏘 회귀의 alpha 값과는 다르다는 것이다. 엘라스틱넷의 규제식은 a * L1 + b * L2 라고 할 수 있다. 여기서 a는 L1 규제의 alpha값을 의미하고 b는 L2규제의 alpha값을 의미한다. 따라서 엘라스틱넷 alpha 값은 a+b라고 할 수 있다. 또한 라쏘 회귀와 릿지 회귀와는 다르게 규제의 비율을 정할 수 있는 파라미터 값도 설정해야만 한다. 바로 l1_ratio 이다. l1_ratio의 식은 a / (a+b) 라고 할 수 있다. 만일 l1_ratio 값이 0이라면 a= 0임을 의미한다. 또한 1이라고 한다면 b= 0 이라고 할 수 있다. 따라서 l1_ratio가 0이라면 a = 0이기 때문에 L2규제와 다를 바 없어지고, l1_ratio 가 1이라면 b=0이기 때문에 L1규제와 다를 바 없다.



```python
elastic_alphas = [0.07,0.1,0.5,1,3]
coeff_ElasticNet_df = get_linear_reg_eval('ElasticNet', params = elastic_alphas, X_data_n = X_data, y_target_n = y_target)
```



### 선형 회귀 모델을 위한 데이터 변환



선형 회귀 모델 같은 경우에는 피처값과 타겟값의 분포가 정규분포의 형태를 가지고 있음을 전제한다. 만일 종속변수의 분포와 독립변수의 분포가 정규분포의 모양을 가지지 않고 왜곡된 모양을 가지고 있다면 예측 성능이 많이 떨어질 수 있다. 따라서 선형 회귀 모형을 만들기 전에 데이터를 스케일링 하는 과정이 필요하다. 하지만 데이터를 스케일링 하였다고 하여 성능이 눈에 보이게 좋아지는 것은 아니다.

 

 일반적으로 피처 데이터와 타켓 데이터를 정규화 시키는 방법을 각각 다르다. 먼저 사이킷런을 이용하여 피처 데이터를 정규화 하는 방법은 다음과 같다.

 

1. StandardScaler 클래스를 이용하여 평균이 0, 분산이 1인 표준 정규 분포를 가진 데이터 세트로 변환하거나 MinMaxScaler 클래스를 이용하여 최솟값이 0이고 최댓값이 1인 값으로 정규화를 수행 
2. 스케일링/정규화를 수행한 데이터 세트에 다시 다항 특성을 적용하여 변환하는 방법. 1번 방법이 효과가 미미할시 2번을 추가로 시행하는 것
3. 원래 값에 log함수를 적용하면 보다 더 정규분포에 가까워진다. (로그변환) 실제로 3번의 방법이 1번 2번 보다 더 많이 사용된다. 왜냐하면 1번의 경우에는 성능 향상이 미미하고 2번 같은 경우에는 다항 특성으로 변환하면 과적합 되는 문제가 발생하기 때문이다.



 타겟 데이터를 변환하는 방법은 주로 로그 변환 방법이다. 