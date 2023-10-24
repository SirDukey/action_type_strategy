"""
MOCK SOME BASIC LOGIC
"""

def open_promotion(promotion_id):
    """simple mock of opening a promotion"""
    return {'_id': promotion_id}


def create_promotion(status=None):
    """simple mock to create a promotion"""
    promotion_id = 456
    promotion_data = {'_id': promotion_id}
    if status:
        promotion_data['status'] = status
    return promotion_id, promotion_data


def check_action_type(action_id):
    """simple mock of how action id is translated to action type in TPM"""
    action_type_lookup = {'1': 'open', '2': 'close', '3': 'create', '4': 'create_quick', '5': '1'}
    action_type = action_type_lookup.get(str(action_id))
    post_action_id = action_type if str(action_id) == '5' else None
    return action_type, post_action_id
