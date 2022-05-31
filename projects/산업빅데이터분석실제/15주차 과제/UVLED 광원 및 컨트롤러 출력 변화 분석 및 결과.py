# -*- coding: utf-8 -*-
"""

산업 빅데이터 분석 - 탐색적 데이터 분석
2020254011 윤재웅

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('fivethirtyeight')
import warnings
warnings.filterwarnings('ignore')
%matplotlib inline

train_data = pd.read_excel('train.xlsx')
test_data = pd.read_excel('test.xlsx')

"level:광출력레벨 / temp:광원온도 / power:광출력"


"train_data.head()"
train_data.info()
"train_data.describe()"

for col in train_data.columns:
    msg = 'column: {:>10}\t Percent of NaN value: {:.2f}%'.format(col,
                100 * (train_data[col].isnull().sum() / train_data[col].shape[0]))
    print(msg)

"msno.matrix(df=data.iloc[:, :], gifsize=(8, 8), color=(0.8, 0.5, 0.2))"

"f, ax = plt.subplot(1, 2, figsize=(18, 8))"

"data['power'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)"
                                      
"ax[0].set_title('Pie plot - power')"
"ax[0].set_ylabel('')"
"sns.countplot('power', data=data, ax=ax[1])"
"ax[1].set_title('Count plot - power')"
"plt.show()"
"train_data[['level', 'temp']].groupby(['level'], as_index=True).count()"
"pd.crosstab(train_data['level'], train_data['temp'], margins=True).style.background_gradient(cmap='summer_r')"

train_data['level'].value_counts()
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
sns.countplot(x='level', data=train_data)
plt.show()