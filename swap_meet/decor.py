from .item import Item

class Decor(Item):
    '''
    override __init__ use super() for id
    attribute: width=0, length=0

    __str__()
    returns "An object of type Decor with id <id value>.
    It takes up a <width value> by <length value> sized space."
    '''
    def __init__(self, condition=0, id=None, width=0, length=0):
        self.condition = condition
        self.width = width
        self.length = length
        super().__init__(id)

    def __str__(self):
        first_part = super().__str__()
        return first_part + f" It takes up a {self.width} by {self.length} sized space."

    def get_category(self):
        '''
        Return a string holding the name of the class
        return name_of_class(str)
        '''
        return "Decor"
