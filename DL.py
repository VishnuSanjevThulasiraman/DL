# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 05:47:29 2019

@author: JENNISH DHARMA J J
"""

import numpy as np

#np.random.seed(0)

X = np.array([[0,0] , [0, 1], [1, 0], [1, 1]])
X = X.T
Y= np.array([0,1,1,0])
Y = Y.reshape(1,4)

A = {}
A[1] = np.zeros((2, 4))
A[2] = np.zeros((1, 4))

Z = {}
Z[1] = np.zeros((2, 4))
Z[2] = np.zeros((1, 4))

W= {}
b= {}
W = {1: np.array([[-1.51564262,  0.88023096],
       [ 0.89157467, -1.02362262]]), 2: np.array([[1.13606486, 1.12161037]])}
#W[1] = np.random.randn(2,2)*0.01
#W[2] = np.random.randn(1,2)*0.01
b[1] = np.zeros((2, 1))
b[2] = 0

W_in = W
b_in = b

def der_lu(x):
    der = x>0
    der = der*1
    return der
    
def relu(x):
    val = x*(x>0)
    return val

def frwd_prop(W, b):
    Z[1] = np.dot(W[1], X )
    A[1] = relu(Z[1])
    Z[2] = np.dot(W[2], A[1])
    A[2] = relu(Z[2])
    return Z ,A
    
def cost(A):
    cost_1 = np.dot((A-Y), (A.T - Y.T))
    cost_1 = np.squeeze(cost_1)
    return cost_1/2
    
    
#print(relu(-5))
for i in range(100):
   # print("################", i)
    Z, A = frwd_prop(W, b)
    
    cost_2 = cost(A[2])
    
    #print(cost(A[2]))
    dA_2 = A[2] - Y
    dZ_2 = dA_2*der_lu(Z[2])
    dW_2 = np.dot(dZ_2, A[1].T)
    db_2 = np.sum(dZ_2)
    
    dA_1 = np.dot(W[2].T, dZ_2)
    dZ_1 = dA_1*der_lu(Z[1])
    dW_1 = np.dot(dZ_1, X.T)
    db_1 = np.sum(dZ_1, axis = 0)
    
    #print(dW_1, dW_2, db_1, db_2)
    #print(W[1], W[2], b[1], b[2])
    
    W[2] = W[2] - 0.9*dW_2
    W[1] = W[1] - 0.9*dW_1
    b[2] = b[2] - 0.9*db_2
    b[1] = b[1] - 0.9*db_1
    
    #print(W[1], W[2], b[1], b[2])
    
e,r = frwd_prop(W,b)
print(r[2])