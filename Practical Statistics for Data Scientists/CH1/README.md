# CHAPTER 1 
### 탐색적 데이터 분석(EDA)

대부분 정형화되지 않은 상태의 데이터로 존재하기 때문에 통계적 개념을 활용하기 위해선 정형화된 형태로 변환해야한다.

#### 데이터 종류
- 수치형(numeric) : 숫자를 이용해 표현할 수 있는 데이터
- 연속형(continuous) : f일정 범위 안에서 어떤 값이든 취할 수 있는 데이터(유의어 : 구간형, 실수형, 수치형 데이터)
- 이산형(discrete) : 횟수와 같은 정수 값만 취할 수 있는 데이터
- 범주형(categorical) : 가능한 범주 안의 값만을 취하는 데이터
- 이진(binary) : 두 개의 값(0/1, true/false)
- 순서형(ordinal) : 값들 사이에 분명한 순위가 있는 범주형 데이터

#### 테이블 데이터
- 데이터 프레임(data frame) : 통계와 머신러닝 모델에서 가장 기본이 되는 테이블 형태의 데이터 구조
- 피처(feature) : 일반적으로 테이블의 각 열이 하나의 피처를 의미
- 결과(outcome) : 데이터 과학 목표는 어떤 결과를 예측하는데 있다. 결과를 예측하기 위해 피처를 이용한다.
- 레코드(record) : 일반적으로 테이블의 각 행은 하나의 레코드를 의미

> 물론 테이블 데이터 이외의 구조를 가진 데이터도 존재한다. 시계열, 공간, 그래프 등 

#### 위치 추정
데이터를 살펴보는 기초적인 단계는 각 피처의 대푯값을 구하는 것이다.

- 평균(mean) : 모든 값의 총합을 개수로 나눈 값
- 가중평균(weighted mean) : 가중치를 곱한 값의 총합을 가중치의 총합으로 나눈 값
- 중간값(median) : 데이터에서 가장 가운데 위치한 값
- 백분위수(percentile) : 전체 데이터의 P%를 아래에 두는 값(분위수)
- 가중 중간값(weighted median) : 데이터를 정렬한 후, 각 가중치 값을 위에서부터 더할 때, 총합의 중간이 위치하는 데이터 값
- 절사평균(trimmed mean) : 정해진 개수의 극단값을 제외한 나머지 값들의 평균
    - 극단값의 영향을 제거한다.
- 로버스트하다(robust) : 극단값들에 민감하지 않다는 것을 의미한다.
- 특잇값(outlier) : 대부분의 값과 매우 다른 데이터 값

```
import pandas as pd
from scipy import stats
import wquantiles as wq
import numpy as np

#데이터 불러오기
state = pd.read_csv("./state.csv")

#Population 컬럼 평균
print(state.Population.mean())

#Population 컬럼 절사 평균(0.1 의 경우 양 끝 10% 제외한 후 평균낸다.)
print(stats.trim_mean(state.Population, 0.1))

#Population 중간값
print(state.Population.median())

#Population 가중평균
print(np.average(state['Murder.Rate'], weights=state['Population']))

#Population 가중중간값
print(wq.median(state['Murder.Rate'], weights=state['Population']))

```


#### 변이 추정
변이는 데이터 값이 얼마나 밀집해 있는지 혹은 퍼져 있는지 나타내는 산포도를 나타낸다.

- 편차(deviation) : 관측값과 위치 추정값 사이의 차이
- 분산(variance) : 평균과 편차를 제곱한 값들의 합을 n-1로 나눈 값, n은 데이터 개수
- 표준편차(standard deviation) : 분산의 제곱근
- 평균절대편차(mean absolute deviation) : 평균과의 편차의 절댓값의 평균
- 중간값의 중위절대편차(MAD) : 중간값과의 편차의 절댓값의 중간값
- 범위(range) : 데이터의 최댓값과 최솟값의 차이
- 순서통계량(order statistics) : 최소에서 최대까지 정렬된 데이터 값에 따른 계량형
- 백분위수(percentile) : 어떤 값들의 P퍼센트가 이 값 혹은 더 작은 값을 갖고, (100-P)퍼센트가 이 값 혹은 더 큰 값을 갖도록 하는 값
- 사분위범위(IQR) : 75번째 백분위수와 25번째 백분위수 사이의 차이

