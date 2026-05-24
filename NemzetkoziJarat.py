from Jarat import Jarat

class NemzetkoziJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar):
        super().__init__(jaratszam, celallomas, jegyar)
        
    def jarat_info(self):
        return f"Nemzetkozi jarat: {self.jaratszam} - {self.celallomas} ({self.jegyar} Ft)"
