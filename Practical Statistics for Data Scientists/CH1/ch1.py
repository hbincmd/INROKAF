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
