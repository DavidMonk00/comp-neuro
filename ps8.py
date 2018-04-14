from __future__ import division
import numpy as np
from matplotlib import pyplot as plt

b = 1
alpha = 1

def perceptron(yt, x, N, p, n):
    y = 0
    w = np.zeros(n)
    E = np.zeros(N)
    for i in range(N):
        for mu in range(p):
            y = np.heaviside(np.dot(w,x[mu]) - b, 1)
            w += alpha * x[mu] * (yt[mu] - y)
            E[i] += (yt[mu]-y)**2
    plt.plot(E)

def main():
    N = 10
    p = 4
    n = 2
    yt = np.array([[0,1,1,1],[0,1,1,0]])
    x = np.array([[0,0],[0,1],[1,0],[1,1]])
    # for i in yt:
    #     perceptron(i, x, N, p, n)
    # plt.show()
    n = 100
    N = 1500
    p = [50,100,200]
    for i in p:
        yt = np.array(np.random.random(i)>0.5,dtype=float)
        x = np.array(np.random.random((i,n))>0.5,dtype=float)
        perceptron(yt, x, N, i, n)
    plt.show()

if (__name__ == "__main__"):
    main()
