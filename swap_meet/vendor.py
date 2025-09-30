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
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        
        self.remove(my_item)
        other_vendor.add(my_item)
        other_vendor.remove(their_item)
        self.add(their_item)

        return True

    def swap_first_item(self, other_vendor):

        '''
        Swaps first item in this inventory and friend's inventory.

        parameters: instance of another Vendor(other_vendor)

        returns: True if successful
        False if either have empty inventory
        '''
        
        if not self.inventory or not other_vendor.inventory:
            return False
        
        my_first_item = self.inventory[0]
        their_first_item = other_vendor.inventory[0]

        self.swap_items(other_vendor, my_first_item, their_first_item)

        return True