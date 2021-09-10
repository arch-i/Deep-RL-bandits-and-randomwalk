from gym.envs.registration import register

register(
    id='bernoulli-bandit-v0',
    entry_point='my_envs.envs:bernoulliBandit',
)
register(
    id='gaussian-bandit-v0',
    entry_point='my_envs.envs:gaussianBandit',
)
register(
    id='random-walk-v0',
    entry_point='my_envs.envs:randomWalk',
)
