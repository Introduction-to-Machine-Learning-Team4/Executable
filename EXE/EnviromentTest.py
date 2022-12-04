# %% [markdown]
# ## Usage (Command Line)
# Run the MLAgent Default Model(PPO/SAC) by Anaconda command prompt under the folder with exe
# ```
# mlagents-learn <config path> --env=<exe name> --run-id=<run_name>
# ```
# It should be like
# ```
# mlagents-learn config\player_config.yaml --env="CRML" --run-id=test
# ```

# %% [markdown]
# # Enviroment
# Get the enviroment by calling `UnityEnviroment()` to get the corresponding file name env.<br />
# - Close: `env.close()` close the enviroment. Release the port of commutator. <br />
# - Reset: `env.reset()` resets the enviroment. <br />
# - Set Action: `env.set_actions(behavior_name: str, action: ActionTuple)` set up the actions for next step.More Info down below <br />
# - Step: `env.step()` move the simulation forward. Pass the action to Unity. <br />
# - Get Step: `env.get_steps(behavior_name: str)` get the decision step from Unity.More Info down below <br />
#  

# %%
from mlagents_envs.environment import UnityEnvironment
import numpy as np
# This is a non-blocking call that only loads the environment.
env = UnityEnvironment(file_name="CRML", seed=1, side_channels=[])
# Start interacting with the environment.
env.reset()

# %% [markdown]
# # Behavior Spec
# Contains the specs of the behavior. Including `ActionSpec` and `Observation Spec`<br />
# `env.behavior_specs` is a dictionary of (Name: str, Spec: Behavior_Spec) <br />
# Get the names of Behavior Spec by  `list(env.behavior_specs)` or `list(env.behavior_specs.keys())` <br />
# Get the corresonding Behavior Spec by `env.behavior_specs[behavior_name]` <br />

# %%
# Since there's only one behavior, get the first on the list
behavior_name = list(env.behavior_specs)[0]
print(f"Name of the behavior : {behavior_name}")
spec = env.behavior_specs[behavior_name]
print(f"Behavior spec of {behavior_name} : {spec}")

# %% [markdown]
# # Observation Spec
# Note: this is NOT the Observation Space that observed for agent, but an info spec of it <br />
# Get the Observation Spec by `spec.observation_specs`
# - Shape: numbers of observation
# - Dimension Property:
# - Observation Type:
# - Name:

# %%
# Examine the number of observations per Agent
print("Number of observations : ", len(spec.observation_specs))
print(f"Spec Info : {spec.observation_specs[0]}")
# Is there a visual observation ?
# Visual observation have 3 dimensions: Height, Width and number of channels
vis_obs = any(len(spec.shape) == 3 for spec in spec.observation_specs)
print("Is there a visual observation ?", vis_obs)

# %% [markdown]
# # Action Spec
# Note: this is NOT the Action Space that set for agent, but an info spec of it <br />
# Get the Action Spec by `spec.action_specs` <br />
# Random Action: `action_spec.random_action(n_agent: int)` create an random action for n agents <br />
# Empty Action: `action_spec.empty_action(n_agent: int)` create an empty action for n agents <br />

# %%
# Is the Action continuous or multi-discrete ?
if spec.action_spec.continuous_size > 0:
  print(f"There are {spec.action_spec.continuous_size} continuous actions")
if spec.action_spec.is_discrete():
  print(f"There are {spec.action_spec.discrete_size} discrete actions")

# For discrete actions only : How many different options does each action has ?
if spec.action_spec.discrete_size > 0:
  for action, branch_size in enumerate(spec.action_spec.discrete_branches):
    print(f"Action number {action} has {branch_size} different options")

# %% [markdown]
# # Action Tuple
# Class that's pack NamedTuple as Action
# - `action.discrete`: get the discrete actions
# - `action.continuous`: get the continuous actions
# - `action.add_discrete`: add the discrete actions
# - `action.add_continous`: add the continuous actions
# 
# Axis 0(Rows): Different Agents actions value <br />
# Axis 1(Columns): Different Actions on Same agent<br />

# %%
from mlagents_envs.environment import ActionTuple
action = ActionTuple()
action.add_discrete(np.array([[1,2],[3,4]])) # [1,2] actions on Agent 1, [3,4] actions on Agent 2
print(action.discrete)
action.add_continuous(np.array([[0.5]]))
print(action.continuous)
print(spec.action_spec.random_action(2).discrete) # Get 1 random action under Action Spec for 2 agents

# %% [markdown]
# # Decision Steps / Terminal Steps
# Decision Steps and Terminal Steps are the list that agents called for the need of decision.<br />
# Difference between Decision Steps and Terminal Steps is that terminal step only calls on episode end, while 
# decision step can be called at anytime.
# - Decision Steps: `env.get_steps(Behavior_Name:str)` get the steps from agents requested of the behavior<br />
# - Agent ID: `steps.agent_id()` get the agents id corresponding to the step <br />
# - `len(DecisionSteps)`: Returns the number of agents requesting a decision since the last call to env.step()

# %%
decision_steps, terminal_steps = env.get_steps(behavior_name) 
print(decision_steps.agent_id)

# %% [markdown]
# # Observation and Reward of Steps
# Observation of an agent: `steps[agent_id].obs` <br />
# Reward of an agent: `steps[agent_id].reward` <br /> <br/>
# Observation of all agent: `steps.obs` <br />
# Reward of all agent: `steps.reward` <br />

# %%
agent_id = decision_steps.agent_id[0]
print(f"Observation of Agent {agent_id}: {decision_steps[agent_id].obs}")
print(f"Reward of Agent {agent_id}: {decision_steps[agent_id].reward}")

# %% [markdown]
# # Set the Action and Run
# - `env.set_actions(behavior_name: str, action: ActionTuple)` : Setup Action for next step
# - `env.step()` : Foward to next step

# %%
action = spec.action_spec.random_action(len(decision_steps))
env.set_actions(behavior_name, action)
env.step()

# %% [markdown]
# # Run the enviroment for serval episode

# %%
ep = 2
for episode in range(ep):
  env.reset()
  decision_steps, terminal_steps = env.get_steps(behavior_name) # Get the first step
  tracked_agent = decision_steps.agent_id[0] # Track the agent (Since there's only one)
  done = False # For the tracked_agent
  episode_rewards = 0 # For the tracked_agent
  while not done:
    # Generate an action for all agents
    action = spec.action_spec.random_action(len(decision_steps))
    # Set the actions
    env.set_actions(behavior_name, action)

    # Move the simulation forward
    env.step()

    # Get the new simulation results
    decision_steps, terminal_steps = env.get_steps(behavior_name)
    if tracked_agent in decision_steps: # The agent requested a decision
      episode_rewards += decision_steps[tracked_agent].reward
      print(f"step reward:{decision_steps[tracked_agent].reward}")
    if tracked_agent in terminal_steps: # The agent terminated its episode
      episode_rewards += terminal_steps[tracked_agent].reward
      print(f"step reward:{terminal_steps[tracked_agent].reward}")
      done = True
  print(f"Total rewards for episode {episode} is {episode_rewards}")

# %%
env.close()


