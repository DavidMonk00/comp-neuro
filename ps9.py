import numpy as np
from matplotlib import pyplot as plt

trials = 100
time = 20
time_reward = 20
time_cue = 5
time_endCue = time_reward
n = time_endCue - time_cue + 1

gamma = 1
alpha = 0.6

def main():
    X = np.zeros((n, trials))
    X[:,time_cue-1:time_endCue] = np.eye(n)
    print X.shape
    # print X[:,time_cue-1:time_endCue]
    V = np.zeros((time, trials))
    w = np.zeros((n,1))
    r = np.zeros((time,trials))
    r[time_reward-1,:] = 1
    delta = np.zeros((time, trials))

    for i in range(trials):
        print w[:,0].shape, X[:,i].shape
        print np.dot(w[:,0],X[:,i])
        V[:,i] = np.dot(w[:,0], X[:,i])
        print V.shape
        delta[:,i] = r[:,i] + gamma * np.append(V[1:,i],0) - V[:,i]
        print X.shape, delta[:,i].shape
        w = w + alpha*np.dot(X,delta[:,i])
        # print V

if (__name__ == "__main__"):
    main()
