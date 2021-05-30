
import uuid

class Snake:
    
    def __init__(self, start,end):
        self.start = start
        self.end = end


class Ladder:

    def __init__(self, start,end):
        self.start = start
        self.end = end



class Player :
    
    def __init__(self, name):
        self.name = name
        self.id = str(uuid.uuid4())



