import gym

acts = {
    "w": 1,
    "s": 0,
    "a": 3,
    "d": 2,
    "q": 4,
    "e": 5
}

env = gym.make("Taxi-v3", render_mode="ansi")
env.reset()

print(env.render())
imp = input("Action:")

while imp != "exit":
    feedback = env.step(acts[imp])
    print(feedback)
    print(env.render())
    if feedback[2]:
        print("You did it!!")
        break
    imp = input("Action:")
