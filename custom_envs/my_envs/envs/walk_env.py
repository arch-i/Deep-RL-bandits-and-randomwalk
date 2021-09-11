import gym 
from gym import Env
import numpy as np


class randomWalk(Env):
  def __init__(self, seed):
    #actions 0 (left), 1(right)
    self.action_space = [0,1]
    self.observation_space=np.arange(7)
    self.state=3
    self.t_state = [0,6]
    self.rng = np.random.default_rng(seed)
  
  def __str__(self):
    return 'Random Walk Environment'

  def step(self, action):
    self.state += self.rng.choice([1,-1])
    reward =0
    if self.state in self.t_state:
      if self.state == 6:
        reward = 1
      done = True
    else: 
      done = False
    return self.state, reward, done

  def render(self):
    pass
  def reset(self):
    self.state=3
