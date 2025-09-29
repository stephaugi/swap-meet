import uuid
class Item:
    def __init__(self, id = None):
        self.id = id if id is not None else uuid.uuid4().int
    
    def get_category(self):
        '''
        Return a string holding the name of the class
        return name_of_class(str)
        '''
        return self.__class__.__name__