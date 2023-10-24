"""
MOCK OF SOME ACTIONS
"""

from tools import *
from base import BasePromotionAction


class PromotionOpen(BasePromotionAction):
    def execute(self):
        print('opening promotion {}...'.format(self.promotion_id))
        self.promotion_data = open_promotion(self.promotion_id)
        return True


class PromotionClose(BasePromotionAction):
    def execute(self):
        print('closing promotion {}...'.format(self.promotion_id))
        return True


class PromotionCreate(BasePromotionAction):
    def execute(self, **kwargs):
        self.promotion_id, self.promotion_data = create_promotion(**kwargs)
        print('created promotion {}'.format(self.promotion_id))
        return True


ACTION_LOOKUP = {
    'open': PromotionOpen,
    'close': PromotionClose,
    'create': PromotionCreate,
    'create_quick': (PromotionCreate, {'status': 5}),
}