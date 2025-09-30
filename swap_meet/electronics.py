from .item import Item

class Electronics(Item):
    '''attribute: type=“Unknown”

    __str__()
    returns "An object of type Electronics with id <id value>. This is a <type value> device."
    '''
    def __init__(self, condition=0, id=None, type="Unknown"):
        self.condition = condition
        self.type = type
        super().__init__(id=id, condition=condition)

    def __str__(self):
        first_part = super().__str__()

        return first_part + f" This is a {self.type} device."

    def get_category(self):
        '''
        Return a string holding the name of the class
        return name_of_class(str)
        '''
        return "Electronics"
