import gym
import numpy as np
import random as rand

max_steps = 20
epoch = 500
generations = 50
learning_rate = 0.2
discount_factor = 0.1

#init state and action matrix
v = np.zeros((500, 6))
f = 0
pf = 0

env = gym.make("Taxi-v3", render_mode="ansi")
for i in range(generations):
    print(f"generation {i}")
    for j in range(epoch):
        env.reset()

        if j == epoch-1:
            print(env.render())
        
        for k in range(max_steps):
            
            #pick action
            a = np.argmax(v[env.s])
            while env.action_mask(env.s)[a] == 0:
                v[env.s][a] = -500
                a = np.argmax(v[env.s])
            
            #get feedback
            f = env.step(a)

            if j == epoch-1:
                print(env.render())

            #update table
            if pf != 0:
                v[pf[0]][a] = v[pf[0]][a] + learning_rate * (pf[1]+ discount_factor * np.max(v[env.s]) - v[pf[0]][a])
            
            #if we finished then go to next one
            if f[2]:
                break

            pf = f

print(v)