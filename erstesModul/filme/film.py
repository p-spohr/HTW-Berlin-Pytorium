# %%

class Film:
    
    def __init__(self, name, jahr, sterne):
        
        self.name = name
        self.jahr = jahr
        self.sterne = sterne

    def review(self):

        print(f'Es hat {self.sterne} Sterne')
        
    def info(self):
        
        print(f'{self.name} war in {self.jahr} veröffentlicht.')

# %%

