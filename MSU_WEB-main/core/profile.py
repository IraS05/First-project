from json import loads , dumps
from . import DATA_DST

class Profile():
    #name , proff_scills , #wantToLearn
    def __init__(self , id):
        with open(DATA_DST + id + '.txt') as f:
            temp = loads( f.read() )

        self.data = temp

    def get(self):
        return  self.data