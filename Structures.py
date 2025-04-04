from abc import ABC, abstractmethod
from enum import Enum                                

class Comparison(Enum):
    LESS_THAN = 1
    GREATER_THAN = 2

class Condition(ABC):
    @abstractmethod
    def evaluate(self, object):
        pass
		
class Stage():
    def __init__(self, steps = 10, interval = 1, objects = []):
        self.objects = objects
        self.time = 0
        self.steps = steps
        self.interval = interval

    def act(self, time):
        self.time += time
        for object in self.objects:
            object.act(time)                                   

    def add(self, *objects):
        for obj in objects:
            self.objects.append(obj)

    def clear(self):
        self.objects.clear()
        self.time = 0

    def run(self, steps = None, interval = None):
        use_steps =  self.steps if steps is None else steps
        use_interval = self.interval if interval is None else interval   
        for _ in range(use_steps):
            self.act(use_interval)
                                                                         
class Instruction():
    def __init__(self, action, *conditions, instructions = []):
        self.action = action
        self.conditions = conditions
        self.instructions = instructions        

    def apply(self, object):
        for condition in self.conditions:
            if not condition.evaluate(object):
                return
        self.action(object)                           
        for instruction in self.instructions:
            instruction.apply(object)

class Actor():
    def __init__(self, name, *instructions):
        super().__init__()
        self.name = name             
        self.instructions = instructions   
        self.state = "initial"
        self.time_step = 0.0
        self.position = [0.0, 0.0]

    def act(self, time):
        self.time_step = time
        for instruction in self.instructions:
            instruction.apply(self)

    def set_state(self, state):
        self.state = state
                                                        
    def get_state(self):
        return self.state

    def get_time_step(self):
        return self.time_step

    def move(self, x, y):
        self.position[0] += x
        self.position[1] += y                 
                                                     