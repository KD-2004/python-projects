#!/usr/bin/env python
# coding: utf-8

import gym
import os
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import TensorBoard


def train_ppo_model(env, total_timesteps=500000):
    model = PPO('MlpPolicy', env, verbose=1)
    model.learn(total_timesteps=total_timesteps)
    model.save("PPO_Mountain_car_500000")
    return model


def evaluate_ppo_model(model, env, n_eval_episodes=10, render=True):
    return evaluate_policy(model, env, n_eval_episodes=n_eval_episodes, render=render)


if __name__ == "__main__":
    environment_name = "MountainCar-v0"
    env = gym.make(environment_name, render_mode="human")
    env = DummyVecEnv([lambda: env])

    train_ppo_model(env)
    evaluation_results = evaluate_ppo_model(model, env)

    print("Evaluation Results:", evaluation_results)

    # Close the environment
    env.close()
