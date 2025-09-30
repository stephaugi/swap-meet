import uuid
class Item:
    def __init__(self, id = None, condition=0):
        self.condition = condition
        self.id = id if id is not None else uuid.uuid4().int


    def __str__(self):
        '''
        Converts item to string using str().
        returns: "An object of type Item with id <id value>."
        Operator overloading
        '''
        category = self.get_category()
        return f"An object of type {category} with id {self.id}."

    
    def get_category(self):
        '''
        Return a string holding the name of the class
        return name_of_class(str)
        '''
        return "Item"

    def condition_description(self):
        if self.condition > 2:
            return "Yikes. Don't wanna touch that."
        elif self.condition < 3:
            return "Gimme more. Good stuff."
        else:
            return "Not bad. I'll buy it for a dollar."