from __future__ import division
import numpy as np
from matplotlib import pyplot as plt

T = 1e4
nu = 5e-6
y0 = 10
tau = 50
dt = 1

def updateTheta(theta, dt, tau, y, y0):
    return theta * (1 - dt/tau) + (dt/tau) * y*y/y0

def updateW(w, x, nu, y, theta, dt):
    w_new = w + dt * nu * x * y * (y - theta)
    w_new = w_new * (w_new > 0)
    return w_new

def main():
    x1 = np.array([20,0])
    x2 = np.array([0,20])
    w = np.zeros(2)
    length = int(T/dt)
    y = np.zeros(length)
    w = 0.5 * np.ones((2,length))
    theta = 5 * np.ones(length)
    for i in range(length-1):
        x = x1 if np.random.random() > 0.5 else x2
        y[i] = np.dot(w[:,i], x)
        theta[i+1] = updateTheta(theta[i], dt, tau, y[i], y0)
        w[:,i+1] = updateW(w[:,i], x, nu, y[i], theta[i], dt)
    plt.plot(y)
    for i in w:
        plt.plot(i)
    plt.plot(theta)
    plt.xlim(0,1000)
    plt.show()

if (__name__ == "__main__"):
    main()
