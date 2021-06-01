### Multistep DQN CratPole Config ###

env = {
    "name":"cartpole",
    "mode":"discrete",
    "render":False,
}

agent = {
    "name": "multistep",
    "network": "dqn",
    "optimizer": "adam",
    "learning_rate": 0.00025,
    "n_step": 4,
    "gamma": 0.99,
    "epsilon_init": 1.0,
    "epsilon_min": 0.1,
    "explore_step": 20000,
    "buffer_size": 10000,
    "batch_size": 32,
    "start_train_step": 10000,
    "target_update_period": 200,
}

train = {
    "training" : True,
    "load_path" : None,
    "run_step" : 100000,
    "print_period" : 1000,
    "save_period" : 10000,
    "test_iteration": 5,
    # distributed setting
    "update_period" : 8,
    "num_worker" : 8,
}
