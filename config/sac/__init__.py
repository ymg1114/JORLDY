### SAC Config ###

agent = {
    "name":"sac",
    "actor":"sac_actor",
    "critic":"sac_critic",
    "actor_optimizer":"adam",
    "critic_optimizer":"adam",
    "alpha_optimizer":"adam",
    "actor_lr":5e-4,
    "critic_lr":1e-3,
    "alpha_lr":3e-4,
    "use_dynamic_alpha":False,
    "gamma":0.99,
    "tau":5e-3,
    "buffer_size":50000,
    "batch_size":64,
    "start_train_step":5000,
    "static_log_alpha":-2.0,
}
