from .item import Item

class Clothing(Item):
    '''Clothing Class(inherits from Item Class)

    override __init__
    attribute: id(unique integer), fabric=“Unknown”
    super() for id

    __str__()
    returns "An object of type Clothing with id <id value>. It is made from <fabric value> fabric."
    '''
    def __init__(self, condition, id=None, fabric="Unknown"):
        self.fabric = fabric
        self.condition = condition
        super().__init__(id)

    def __str__(self):
        first_part = super().__str__()
        return first_part + f" It is made from {self.fabric} fabric."

    def get_category(self):
        '''
        Return a string holding the name of the class
        return name_of_class(str)
        '''
        return "Clothing"
