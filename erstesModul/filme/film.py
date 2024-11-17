# %%

class Film:
    
    def __init__(self, name : str, jahr : int, sterne : int):
        
        self.name = name
        self.jahr = jahr
        self.sterne = sterne

    def review(self) -> None:
        """
        Print out the rating.
        """
        if self.sterne > 3:
            print(f'Der Film war beliebt mit {self.sterne} Sterne.')
        else:
            print(f'Der Film war nicht gut mit {self.sterne} Sterne.')
        
    def info(self) -> None:
        """
        Print out detailed information.
        """
        print(f'{self.name} war in {self.jahr} veröffentlicht.')

# %%

