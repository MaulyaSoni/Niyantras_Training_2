from abc import ABC , abstractmethod

class Bill(ABC):
    def __init__(self, items , total):
        self.items = items
        self.total = total

    @abstractmethod
    def calc_discount(self):
        pass
    
    def discount(self,discount):
        self.discount = discount
        disc_temp = self.discount / 100
        disc_temp *= self.total
        discounted_total = self.total - disc_temp
        return discounted_total 