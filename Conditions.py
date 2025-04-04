from Structures import Condition, Comparison

class StateCondition(Condition):
    def __init__(self, check_if_true, *options):
        self.check_if_true = check_if_true
        self.options = options

    def evaluate(self, object):
        for option in self.options:
            if object.get_state() == option:
                return self.check_if_true
        return not self.check_if_true

class PositionCondition(Condition):                 
    def __init__(self, index, value, comparison):
        self.index = index
        self.value = value
        self.comparison = comparison

    def evaluate(self, object):
        position_value = object.position[self.index]
        if self.comparison == Comparison.LESS_THAN:                                                     
            return position_value < self.value
        elif self.comparison == Comparison.GREATER_THAN:                                                       
            return position_value > self.value

class TimerCondition(Condition):
    def __init__(self, interval):
        self.interval = interval
        self.timer = 0.0

    def evaluate(self, object):
        self.timer += object.get_time_step()
        if self.timer >= self.interval:
            self.timer = 0.0
            return True
        return False    
    
class AlwaysCondition(Condition):
    def evaluate(self, object):
        return True                                    
                                               