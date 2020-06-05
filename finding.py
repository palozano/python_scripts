import numpy as np

class Finder:

    def __init__(self, lista):
        # Has a number as an identifier of the individual
        # that enters the shop as number. Start at 1
        self.l = lista

    def log_clients(self, client):
        """Adds a new client"""
        self.l.append(client)

    def find_repeat(self):
        """Finds the first repetition of a client"""
        tmp_dict = {}
        for item in self.l:
            if str(item) in tmp_dict:
                tmp_dict[str(item)] += 1 
            else:
                tmp_dict[str(item)] = 0 
            if tmp_dict[str(item)] >= 1:
                return item

    def find_uniques(self):
        """Finds all the unique clients"""
        return [i for i in self.lista if self.lista.count(i)==1][0]

    def print_first_non_repeat(self):
        """Returns the first non-repeated client"""
        return self.l[self.l.index(self.find_repeat()) + 1]


lista = [1, 2, 3, 4, 5, 1, 7]

F = Finder(lista)
print(F.print_first_non_repeat())
