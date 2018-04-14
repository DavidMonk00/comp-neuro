import numpy as np
import pylab as pl

trials = 100
time = 20
time_reward = 20
time_cue = 5
time_endCue = time_reward
n = time_endCue - time_cue

gamma = 1
alpha = 0.8

def main():
    X = np.zeros((n, time))
    X[:,time_cue:time_endCue] = np.eye(n)
    # print X[:,time_cue-1:time_endCue]
    V = np.zeros((time, trials))
    w = np.zeros(n)
    r = np.zeros((time,trials))
    r[time_reward-1,:] = 1
    r[time_reward-1, 50] = 0
    delta = np.zeros((time, trials))
    for i in range(trials):
        V[:,i] = np.dot(w, X)
        delta[:,i] = r[:,i] + gamma * np.append(V[1:,i],0) - V[:,i]
        w = w + alpha*np.dot(X,delta[:,i])
    pl.imshow(delta)
    pl.show()
    pl.imshow(V)
    pl.show()

if (__name__ == "__main__"):
    main()
