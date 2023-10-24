"""
== Strategy ==

BasePromotionAction: A class that is inherited by each action class, the attributes are initialized here
PromotionAction: A class that can execute an action on a promotion
Child class: Each action can be a child class that is callable from the PromotionAction.execute() method

"""
from base import BasePromotionAction
from promotion_functions import ACTION_LOOKUP


class PromotionAction(BasePromotionAction):
    def execute(self):
        print('executing action: {}'.format(self.action_type))
        action = ACTION_LOOKUP.get(self.action_type)
        if action and isinstance(action, tuple):
            self.result = action[0].execute(self, **action[1])
        elif action and isinstance(action, object):
            self.result = action.execute(self)
        else:
            self.result = False
        if self.post_action_id:
            post_action = PromotionAction(self.promotion_id, self.post_action_id)
            self.result = post_action.execute()
        return self.result



# Using the PromotionAction class to control the execution
for action_id in range(1, 6):
    my_action = PromotionAction(123, action_id)
    my_action.execute()
    print(my_action.result)
    print(my_action.promotion_data)
    print('')

# Each child class can also be used independently
#open_promotion_action = PromotionOpen(123, 1).execute()
#print(open_promotion_action)

