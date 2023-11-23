#!/usr/bin/env python
# coding: utf-8

# Importing necessary libraries
import gym
import os
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import TensorBoard

# Setting up the environment
environment_name = "CarRacing-v2"
env = gym.make(environment_name, render_mode="human")

# Uncomment the following lines if you want to visualize the environment
# env.reset()
# env.render()

# Running random actions for a few episodes
num_episodes = 5
for i in range(1, num_episodes + 1):
    state = env.reset()
    done = False
    score = 0
    while not done:
        env.render()
        action = env.action_space.sample()
        n_state, reward, done, info, _ = env.step(action)
        score += reward

    print("Episode {}: Score {}".format(i, score))

# Close the environment
env.close()

# Wrapping the environment and setting up logging
env = gym.make(environment_name, render_mode="human")
env = DummyVecEnv([lambda: env])
log_path = os.path.join('Training', 'Logs')

# Initializing and training the PPO model
model = PPO('CnnPolicy', env, verbose=1, tensorboard_log=log_path)
model.learn(total_timesteps=1000)

# Saving the trained model
model.save("PPO_Driving_model")
ppo_path = os.path.join('Training', 'Saved Models', 'PPO_Driving_Model')

# Loading the saved model
del model  # Delete the existing model to load the saved one
model = PPO.load(ppo_path, env)

# Evaluating the model
evaluate_policy(model, env, n_eval_episodes=10, render=True)

# You can upload this code to GitHub with an appropriate title and description.
# Make sure to replace <<Your GitHub Repo Link>> with the actual link to your GitHub repository.
