#파일 직접 업로드하기
from google.colab import files
myfile = files.upload()

#io와 pandas 모듈 import
import io
import pandas as pd

#pd.read_csv로 csv파일 불러오기
data = pd.read_csv(io.BytesIO(myfile['UVMETER.csv']))
data.head()

import numpy as np
import csv
from sklearn.linear_model import LinearRegression
from sklearn.isotonic import IsotonicRegression

r= open("UVMETER.csv", 'r')
data = csv.reader(r)

header = next(data)
CONT_8BIT = []
ADC_VALUE = []
CONT_12BIT_DEMO = []
CONT_12BIT = []
for rr in data:
    CONT_8BIT.append(rr[0])
    ADC_VALUE.append(rr[1])
    CONT_12BIT_DEMO.append(rr[2])
    CONT_12BIT.append([float(rr[0]), float(rr[1])])

lr = LinearRegression()
lr.fit(CONT_12BIT, ADC_VALUE)
resultLinear = lr.predict(CONT_12BIT)

ir = IsotonicRegression()
resultIso = ir.fit_transform(CONT_8BIT, ADC_VALUE)

gapThreshold = 1

wfile = open("UVMETER_Regression.csv", 'w', newline ='')
write = csv.writer(wfile)
write.writerow(['CONT_8BIT','ADC_VALUE','CONT_12BIT_DEMO','CONT_12BIT'])
for i in range(0,len(CONT_12BIT_DEMO)):
   gapIso = (float)(ADC_VALUE[i]) - resultIso[i]
   gapLinear = (float)(ADC_VALUE[i]) - resultLinear[i]
   strResultIso = 'Pass'
   strResultLinear = 'Pass'
   if abs(gapLinear) > gapThreshold:
       strResultLinear = '불량 의심'
   if abs(gapIso) > gapThreshold:
       strResultIso = '불량 의심'
   write.writerow([CONT_8BIT[i],ADC_VALUE[i],CONT_12BIT_DEMO[i], resultLinear[i])

print("complete! Please Check [UVMETER_Regression.csv]")

from google.colab import drive
drive.mount('/content/drive')

cflu_data = pd.read_csv('/content/CFLU_Data_Regression.csv')
cflu_data .head()