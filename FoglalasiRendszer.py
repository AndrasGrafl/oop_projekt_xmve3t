from datetime import datetime
from LegiTarsasag import LegiTarsasag
from JaratFactory import JaratFactory
from JegyFoglalas import JegyFoglalas

class FoglalasiRendszer:
    def __init__(self):
        self._legitarsasag = LegiTarsasag("Hungarian Airlines")
        self._foglalasok = []
        self._init_data()

    def _init_data(self):
        self._legitarsasag.jaratok = JaratFactory.create_jarat("Belfoldi", "B01", "Debrecen", 15000)
        self._legitarsasag.jaratok = JaratFactory.create_jarat("Nemzetkozi", "N01", "London", 45000)
        self._legitarsasag.jaratok = JaratFactory.create_jarat("Nemzetkozi", "N02", "Parizs", 55000)
        
        self.foglalas("B01", "Kovacs Janos", "2026-06-01", is_init=True)
        self.foglalas("B01", "Szabo Eva", "2026-06-02", is_init=True)
        self.foglalas("N01", "Toth Peter", "2026-07-10", is_init=True)
        self.foglalas("N01", "Kiss Anna", "2026-07-15", is_init=True)
        self.foglalas("N02", "Nagy Gabor", "2026-08-20", is_init=True)
        self.foglalas("N02", "Farkas Zita", "2026-08-25", is_init=True)

    @property
    def legitarsasag(self):
        return self._legitarsasag

    @property
    def foglalasok(self):
        return self._foglalasok

    def foglalas(self, jaratszam, utas_nev, datum_str, is_init=False):
        try:
            datum = datetime.strptime(datum_str, "%Y-%m-%d")
            if datum < datetime.now() and not is_init:
                raise ValueError("A datum nem lehet a multban.")
        except ValueError as e:
            raise ValueError(f"Hibas datum: {e}")

        keresett_jarat = next((j for j in self._legitarsasag.jaratok if j.jaratszam == jaratszam), None)
        if not keresett_jarat:
            raise ValueError("Ilyen jaratszam nem letezik.")

        uj_foglalas = JegyFoglalas(keresett_jarat, utas_nev, datum)
        self._foglalasok.append(uj_foglalas)
        return keresett_jarat.jegyar

    def lemondas(self, jaratszam, utas_nev, datum_str):
        try:
            datum = datetime.strptime(datum_str, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Hibas datum formatum (YYYY-MM-DD szukseges).")

        keresett = None
        for f in self._foglalasok:
            if f.jarat.jaratszam == jaratszam and f.utas_nev == utas_nev and f.datum == datum:
                keresett = f
                break
        
        if keresett:
            self._foglalasok.remove(keresett)
        else:
            raise ValueError("Nem talalhato ilyen foglalas.")
