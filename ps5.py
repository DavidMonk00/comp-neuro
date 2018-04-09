from __future__ import division
import numpy as np
from matplotlib import pyplot as plt

tau = 5

def calcHExt(theta0, c, epsilon, theta):
    return c*((1 - epsilon) + epsilon * np.cos(2 * (theta - theta0)))

def g(h):
    T = 0
    beta = 0.1
    if (h <= T):
        return 0
    if (h > (T + 1/beta)):
        return 1
    else:
        return beta*(h-T)

def J(theta_i, theta_j):
    J0 = 86
    J2 = 112
    return -J0 + J2*np.cos(2*(theta_i - theta_j))

def calcH(theta, m, h):
    for i in range(len(h)):
        for j in range(len(m)):
            h[i] += J(theta[i], theta[j])*m[j]
    return h

def euler(m, g, dt, h):
    m_new = np.empty(len(m))
    for i in range(len(m)):
        m_new[i] = m[i]*(1-dt/tau) + (dt * g(h[i]) / tau)
    return m_new

def solve(m_init, theta0, N, Ni, epsilon, c):
    theta = np.linspace(-np.pi/2, np.pi/2, N)
    h = calcHExt(theta0, c, epsilon, theta)
    dt = 1
    m = np.empty(N*Ni).reshape(N,Ni)
    m[:,0] = m_init
    for t in range(1,Ni):
        h = calcH(theta, m[:,t-1], h)
        # plt.scatter(theta, h)
        # plt.show()
        m[:,t] = euler(m[:,t-1], g, dt, h)
    return m

def main(N):
    # f, axarr = plt.subplots(1,3)
    # epsilon = 0.9
    # c = 1.5
    # m = solve(0, 50, 30, epsilon, c)
    # axarr[0].imshow(m)
    # c = 1.2
    # m = solve(0, 50, 30, epsilon, c)
    # axarr[1].imshow(m)
    # c = 4
    # m = solve(0, 50, 30, epsilon, c)
    # axarr[2].imshow(m)
    # plt.show()

    # theta = np.linspace(-np.pi/2, np.pi/2, 50)
    # z = np.empty(50*50).reshape(50,50)
    # for i in range(50):
    #     for j in range(50):
    #         z[i,j] = J(theta[i], theta[j])
    # plt.imshow(z)
    # plt.show()

    m_init = np.zeros(50)
    f, axarr = plt.subplots(1,2,sharey=True)
    epsilon = 0.9
    c = 12
    m = solve(m_init, 0, 50, 30, epsilon, c)
    axarr[0].imshow(m)
    m_init = m[:,-1]
    m_second = solve(m_init, 2*np.pi/3, 50, 500, epsilon, c)
    axarr[1].imshow(m_second)
    plt.show()

if (__name__ == "__main__"):
    main(50)
