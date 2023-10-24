"""
SETUP A PARENT CLASS
"""

from abc import ABCMeta, abstractmethod
from tools import *



class BasePromotionAction:
    """Class to prepare the object before executing a promotion action"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self):
        raise NotImplementedError("All subclasses must implement the 'execute' method")

    def __init__(self, promotion_id=None, action_id=None):
        self.promotion_id = promotion_id
        self.action_id = action_id

        self.promotion_data = None
        self.result = None
        self.action_type, self.post_action_id = check_action_type(action_id)



    def __repr__(self):
        return 'PromotionAction({}, {})'.format(self.promotion_id, self.action_id)

    def __str__(self):
        return 'promotion_id: {}\naction_type: {}'.format(self.promotion_id, self.action_type)
