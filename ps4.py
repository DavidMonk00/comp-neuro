import numpy as np
from matplotlib import pyplot as plt
from math import ceil

def euler(v, dt, tau, I, vt):
    for i in range(len(v)-1):
        v_new = (1-dt/tau)*v[i] + (dt/tau)*I
        if (v_new > vt):
            v_new = 0
        v[i+1] = v_new
    return v

def solveEquation(T, dt, I, tau, vt):
    steps = int(ceil(float(T)/dt))
    v = np.empty(steps)
    v[0] = 0.0
    v = euler(v, dt, tau, I, vt)
    return v

def main():
    dt = 1.0
    T = 200.0
    I = [9.0,11.0,15.0]
    tau = 10.0
    vt = 10
    for i in I:
        v = solveEquation(T, dt, i, tau, vt)
        plt.plot(v)
    plt.show()

if (__name__ == '__main__'):
    main()
