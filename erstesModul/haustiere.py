
class Haustier:
    
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
        
    def eat(self):
        print('Chomp!')
        
    def drink(self):
        print('Slurp!')
        

class Hund(Haustier):
    
    def __init__(self, name, alter):
        Haustier.__init__(self, name, alter)
        
    def bark(self):
        print('Woof!')


class Katze(Haustier):
    
    def __init__(self, name, alter):
        Haustier.__init__(self, name, alter)
        
    def meow(self):
        print('Meow!')

# %%
