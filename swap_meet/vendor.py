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
    
    def swap_items(self, other_vendor, my_item, their_item):
        '''
        parameters: 3 arguments. 
        instance of another vendor(other_vendor)
        instance of item(my_item)
        instance of item(their_item)

        return: True
        edgecase: if this vendor's inventory doesn't contain my_item
        the friend's inventory doesn't contain their_item, the method
        returns False

        '''
        vendor1_has_item = self.get_by_id(my_item.id)
        vendor2_has_item = other_vendor.get_by_id(their_item.id)

        if not vendor1_has_item or not vendor2_has_item:
            return False
        
        my_item = self.remove(my_item)
        other_vendor.add(my_item)
        their_item = other_vendor.remove(their_item)
        self.add(their_item)

        return True
