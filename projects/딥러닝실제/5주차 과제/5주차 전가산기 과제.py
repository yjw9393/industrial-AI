# keyword : 퍼셉트론, 가중치, 편향

import numpy as np

def AND(x1, x2):
 x = np.array([x1, x2])
 w = np.array([0.5, 0.5])
 b = -0.7
 temp = np.sum(x * w) + b
 if temp <= 0:
  return 0
 else:
  return 1

def OR(x1, x2):
 x = np.array([x1, x2])
 w = np.array([0.5, 0.5])
 b = -0.2
 temp = np.sum(x * w) + b
 if temp <= 0:
  return 0
 else:
  return 1

def NAND(x1, x2):
 x = np.array([x1, x2])
 w = np.array([-0.5, -0.5])
 b = 0.7
 temp = np.sum(x * w) + b
 if temp <= 0:
  return 0
 elif temp > 0:
  return 1  

def XOR(x1, x2):
 a = NAND(x1, x2)
 b = OR(x1, x2)
 y = AND(a, b)
 return y

# Full Adder는
# S = XOR(XOR(x, y), z)
# C = OR(AND(x, y), AND(XOR(x, y, z))
def Full_Adder(x, y, z):
 S = XOR(XOR(x, y), z)
 C = OR(AND(z,XOR(x,y)),AND(x,y))
 return 'x = {0}, y = {1}, z = {2}\nC = {3}, S = {4}'.format(x, y, z, C, S)

# 입력값 안받고 출력
print('\nx = 0, y = 0, z = 0일 때\n')
print((Full_Adder(0, 0, 0)))
print('\nx = 0, y = 1, z = 0일 때\n')
print((Full_Adder(0, 1, 0)))
print('\nx = 1, y = 0, z = 0일 때\n')
print((Full_Adder(1, 0, 0)))
print('\nx = 1, y = 0, z = 1일 때\n')
print((Full_Adder(1, 0, 1)))
print('\nx = 1, y = 1, z = 0일 때\n')
print((Full_Adder(1, 1, 0)))
print('\nx = 0, y = 1, z = 1일 때\n')
print((Full_Adder(0, 1, 1)))
print('\nx = 1, y = 1, z = 1일 때\n')
print((Full_Adder(1, 1, 1)))


# 입력값 받고 출력
#x,y,z = input('x, y, z를 입력\n').split()
#x = int(x)
#y = int(y)
#z = int(z)
#if ((x < 2) & (y < 2) & (z < 2)):
#  Full_Adder(x, y, z)
#else:
#  print('값 확인')

