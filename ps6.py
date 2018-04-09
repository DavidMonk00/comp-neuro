from __future__ import division
import numpy as np
from matplotlib import pyplot as plt

def euler(v, dt, tau_m, Itot, vt):
    v = (1-dt/tau_m)*v + (dt/tau_m)*Itot
    return v

def main(N):
    # Define parameters
    vt = 1
    tau_m = 10
    g_m = 1
    Nsig = 0.5
    Nmean = 0.75
    tau_I = 10
    NE = int(0.5*N)
    NI = int(0.5*N)
    dt = 1
    T = int(300/dt)
    W = 2/np.sqrt(N)

    # Initialisation
    np.random.seed(100)
    v = np.random.random(N)*vt
    vv = np.zeros(N)
    Iback = np.zeros(N)
    SP = 0
    Ichem = np.zeros(N)
    Iext = np.zeros(N)
    raster = [np.empty(0),np.empty(0)]
    Iout = []

    # Iterate over time
    for t in range(T):
        Iback = Iback + (dt/tau_I)*(-Iback + np.random.normal(size=N))
        Iext = Iback/np.sqrt(1/(2*(tau_I/dt)))*Nsig+Nmean
        Ichem[:NE] = Ichem[:NE] + dt/tau_I*(-Ichem[:NE] + W*(np.sum(vv[:NE]) - vv[:NE]) - W*(np.sum(vv[NE:])))
        Ichem[NE:] = Ichem[NE:] + dt/tau_I*(-Ichem[NE:] - W*(np.sum(vv[NE:]) - vv[NE:]) + W*(np.sum(vv[:NE])))
        Iout.append(Ichem[0])
        Itot = Iext + Ichem
        v = euler(v, dt, tau_m, Itot, vt)
        vv = v>=vt
        v = (1-vv)*v
        SP = np.nonzero(vv)[0]
        raster[0] = np.append(raster[0],SP)
        raster[1] = np.append(raster[1],t*np.ones(len(SP)))
    # plt.scatter(raster[1],raster[0],s=0.5)
    # plt.show()
    plt.plot(Iout)

if (__name__ == "__main__"):
    N = [5,50,500,5000,50000,500000]
    for i in N:
        main(i)
    plt.show()
