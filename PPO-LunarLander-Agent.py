#!/usr/bin/env python
# coding: utf-8

import gym
import os
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy

def create_environment(environment_name):
    env = gym.make(environment_name, render_mode="human")
    env = DummyVecEnv([lambda: env])
    return env

def train_ppo_model(env, learning_rate=0.00001, total_timesteps=30000):
    model = PPO('MlpPolicy', env, verbose=1, learning_rate=learning_rate)
    model.learn(total_timesteps=total_timesteps)
    model.save("PPO_LunarLander_30000")
    return model

def evaluate_ppo_model(model, env, n_eval_episodes=10, render=True):
    return evaluate_policy(model, env, n_eval_episodes=n_eval_episodes, render=render)

if __name__ == "__main__":
    environment_name = "LunarLander-v2"
    env = create_environment(environment_name)

    train_ppo_model(env)

    # Evaluation
    env_eval = create_environment(environment_name)
    evaluation_results = evaluate_ppo_model(model, env_eval)

    print("Evaluation Results:", evaluation_results)

    # Close the environments
    env.close()
    env_eval.close()
