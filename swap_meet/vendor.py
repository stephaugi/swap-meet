class Vendor:
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory

    def __contains__(self, item):
        return self.lower <= item <= self.upper

    def add(self, item):
        '''
        Adds the item to inventory
        parameter: item
        return: item added
        '''
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        '''
        Removes the item from the inventory
        parameter: item
        return: item removed
        '''

        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item
    
    def get_by_id(self, item_id):
        '''
        Returns the item with the matching id from inventory
        parameter: item_id (int)
        return: item with the matching id or None if not found
        '''
        for item in self.inventory:
            if item.id == item_id:
                return item
        return None