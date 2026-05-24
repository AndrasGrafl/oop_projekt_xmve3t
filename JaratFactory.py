from BelfoldiJarat import BelfoldiJarat
from NemzetkoziJarat import NemzetkoziJarat

class JaratFactory:
    @staticmethod
    def create_jarat(tipus, jaratszam, celallomas, jegyar):
        if tipus == "Belfoldi":
            return BelfoldiJarat(jaratszam, celallomas, jegyar)
        elif tipus == "Nemzetkozi":
            return NemzetkoziJarat(jaratszam, celallomas, jegyar)
        else:
            raise ValueError(f"Ismeretlen jarat tipus: {tipus}")
