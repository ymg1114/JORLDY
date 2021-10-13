from collections import deque
import random
import numpy as np

from .base import BaseBuffer

class ReplayBuffer(BaseBuffer):
    def __init__(self, buffer_size):
        self.buffer = np.zeros(buffer_size, dtype=dict) # define replay buffer
        self.buffer_index = 0
        self.buffer_size = buffer_size
        self.buffer_counter = 0
        
        self.first_store = True
    
    def store(self, transitions):
        if self.first_store:
            self.check_dim(transitions[0])
        
        for transition in transitions:
            self.buffer[self.buffer_index] = transition
            self.buffer_index = (self.buffer_index + 1) % self.buffer_size
            self.buffer_counter = min(self.buffer_counter + 1, self.buffer_size)
                
                
    def sample(self, batch_size):
        batch_idx = np.random.randint(self.buffer_counter, size=batch_size)
        batch = self.buffer[batch_idx]
        
        transitions = {}
        for key in batch[0].keys():
            transitions[key] = np.stack([b[key][0] for b in batch], axis=0)
            
        return transitions
    
    @property
    def size(self):
        return self.buffer_counter        
