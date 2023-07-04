class Employee:

    raise_ant = 1.06

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'
    
    @property
    def fullname(self):
        return f'{self.last}, {self.first}'
    
   
    def apply_raise(self):
        self.pay = int(self.pay + self.raise_ant)
