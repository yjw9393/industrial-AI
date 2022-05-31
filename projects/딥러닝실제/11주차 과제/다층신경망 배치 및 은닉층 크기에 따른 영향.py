pip install scikit-learn
pip install scipy

from sklearn.datasets import fetch_openml
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
import numpy as np
import time
start = time.time() 
mnist=fetch_openml('mnist_784')
x_train=mnist.data[:60000]; x_test=mnist.data[60000:]
y_train=np.int16(mnist.target[:60000]); y_test=np.int16(mnist.target[60000:])
mlp=MLPClassifier(hidden_layer_sizes=(100), 
                  learning_rate_init=0.001,
                  batch_size=128,   
                  max_iter=300,
                  solver='adam',   
                  verbose=True)
mlp.fit(x_train,y_train)   
res=mlp.predict(x_test) 
conf=np.zeros((10,10),dtype=np.int16)   
for i in range(len(res)):   
    conf[res[i]][y_test[i]]+=1  
print(conf)
no_correct=0
for i in range(10):
    no_correct+=conf[i][i]  
accuracy=no_correct/len(res)    

print("테스트 집합에 대한 정확률은", accuracy*100, "%입니다.")
print("수행시간: {0}초".format(str(time.time() - start)))
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(10,7))
sns.set(font_scale=2)
sns.heatmap(conf, annot=True)   #heatmap graph
