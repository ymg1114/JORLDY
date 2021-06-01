### PER Pong Config ###

env = {
    "name": "pong",
    "render": False,
    "gray_img": True,
    "img_width": 80,
    "img_height": 80,
    "stack_frame": 4,
}

agent = {
    "name": "per",
    "network": "dqn_cnn",
    "optimizer": "adam",
    "learning_rate": 0.00025/4,
    "gamma": 0.99,
    "epsilon_init": 1.0,
    "epsilon_min": 0.1,
    "explore_step": 1000000,
    "buffer_size": 100000,
    "batch_size": 64,
    "start_train_step": 100000,
    "target_update_period": 500,
    "alpha": 0.6,
    "beta": 0.4,
    "learn_period": 4,
    "uniform_sample_prob": 1e-3,
}

train = {
    "training" : True,
    "load_path" : None,
    "run_step" : 100000000,
    "print_period" : 5000,
    "save_period" : 50000,
    "test_iteration": 5,
    # distributed setting
    "update_period" : agent["learn_period"],
    "num_worker" : 16,
}
