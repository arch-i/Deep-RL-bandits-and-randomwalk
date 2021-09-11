## INSTALLATION:
To install the custom environments created 

``` pip install -e custom_envs```

## Structure of the directory
```
custom_envs/
  setup.py
  my_envs/
    __init__.py      ## registering envs
    envs/
      __init__.py    ## importing envs
      bandit_env.py  ## has 2-armed and 10-armed bandit envs
      walk_env.py    ## has random walk env
```
