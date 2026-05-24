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

    def foglalas(self, jaratszam, utas_nev, datum_str, is_init=False):
        try:
            datum = datetime.strptime(datum_str, "%Y-%m-%d")
            if datum < datetime.now() and not is_init:
                raise ValueError("A datum nem lehet a multban.")
        except ValueError as e:
            print(f"Hiba: {e}")
            return None

        keresett_jarat = next((j for j in self._legitarsasag.jaratok if j.jaratszam == jaratszam), None)
        if not keresett_jarat:
            print("Hiba: Ilyen jaratszam nem letezik.")
            return None

        uj_foglalas = JegyFoglalas(keresett_jarat, utas_nev, datum)
        self._foglalasok.append(uj_foglalas)
        if not is_init:
            print(f"Sikeres foglalas! Ar: {keresett_jarat.jegyar} Ft")
        return keresett_jarat.jegyar

    def lemondas(self, jaratszam, utas_nev, datum_str):
        try:
            datum = datetime.strptime(datum_str, "%Y-%m-%d")
        except ValueError:
            print("Hiba: Hibas datum formatum.")
            return

        keresett = None
        for f in self._foglalasok:
            if f.jarat.jaratszam == jaratszam and f.utas_nev == utas_nev and f.datum == datum:
                keresett = f
                break
        
        if keresett:
            self._foglalasok.remove(keresett)
            print("Keresett foglalas sikeresen lemondva.")
        else:
            print("Hiba: Nem talalhato ilyen foglalas.")

    def listazas(self):
        if not self._foglalasok:
            print("Nincs egyetlen aktualis foglalas sem.")
            return
        
        for f in self._foglalasok:
            print(f"Utas: {f.utas_nev}, Jarat: {f.jarat.jaratszam} ({f.jarat.celallomas}), Datum: {f.datum.strftime('%Y-%m-%d')}")

    def user_interact(self):
        while True:
            print("\n--- Repulojegy Foglalasi Rendszer ---")
            print("1. Jegy foglalasa")
            print("2. Foglalas lemondasa")
            print("3. Foglalasok listazasa")
            print("4. Kilepes")

            valasztas = input("Valasszon menupontot (1-4): ")
            if valasztas == "1":
                print("\nElerheto jaratok:")
                for j in self._legitarsasag.jaratok:
                    print(f"- {j.jarat_info()}")
                
                jaratszam = input("Adja meg a jaratszamot: ")
                utas_nev = input("Adja meg az utas nevet: ")
                datum_str = input("Adja meg a datumot (YYYY-MM-DD formatumban): ")
                self.foglalas(jaratszam, utas_nev, datum_str)
                
            elif valasztas == "2":
                jaratszam = input("Adja meg a torlendo foglalas jaratszamat: ")
                utas_nev = input("Adja meg az utas nevet: ")
                datum_str = input("Adja meg a datumot (YYYY-MM-DD): ")
                self.lemondas(jaratszam, utas_nev, datum_str)
                
            elif valasztas == "3":
                print("\nAktualis foglalasok:")
                self.listazas()
                
            elif valasztas == "4":
                break
            else:
                print("Ervenytelen valasztas.")
