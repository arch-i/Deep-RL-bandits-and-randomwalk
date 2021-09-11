import gym 
from gym import Env
import numpy as np



class bernoulliBandit(Env):
  
  def __init__(self, alpha=1, beta=1, seed=None):
    
    # input parameters for env creation : 
    # alpha, beta, seed
    # actions space: 0 (left), 1(right)
    
    self.action_space = [0,1]
    self.observation_space=[0,1,2]
    self.state=1
    self.alpha = alpha
    self.beta = beta
    self.rng = np.random.default_rng(seed)
  
  def __str__(self):
    return '2 armed Bernoulli Bandit \n Alpha:'+str(self.alpha)+ ' Beta:'+str(self.beta)

  def step(self, action):
    if action:
      reward = self.rng.binomial(1,self.beta)
    else:
      reward = self.rng.binomial(1,1-self.alpha)
    self.state +=  2*reward - 1
    return reward

  def render(self):
    pass
  
  def reset(self):
    self.state=1
    
    
    
class gaussianBandit(Env):
  
  def __init__(self,seed=None):
    
    # input parameters for env creation : 
    # seed
    # action space = [0,1,2 ... 9] 
    
    self.action_space = np.arange(10)
    self.observation_space=np.arange(11)
    self.state=0
    self.rng = np.random.default_rng(seed)
    self.rewards = np.zeros(10)
    for i in range(10):
      self.rewards[i]= rng.normal(0,1,1)
  
  def __str__(self):
    return '10 armed Gaussian Bandit with rewards: ' + str(self.rewards)

  def step(self, action):
    reward = rng.normal(self.rewards[action],1,1)
    self.state = action+1
    return reward

  def render(self):
    pass
  
  def reset(self):
    self.state=0
