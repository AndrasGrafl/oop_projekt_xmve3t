class FelhasznaloiFelulet:
    def __init__(self, rendszer):
        self._rendszer = rendszer

    def user_interact(self):
        while True:
            print("\n--- Repulojegy Foglalasi Rendszer ---")
            print("1. Jegy foglalasa")
            print("2. Foglalas lemondasa")
            print("3. Foglalasok listazasa")
            print("4. Kilepes")

            valasztas = input("Valasszon menupontot (1-4): ")
            if valasztas == "1":
                self._menupont_foglalas()
            elif valasztas == "2":
                self._menupont_lemondas()
            elif valasztas == "3":
                self._menupont_listazas()
            elif valasztas == "4":
                break
            else:
                print("Ervenytelen valasztas.")
                
    def _menupont_foglalas(self):
        print("\nElerheto jaratok:")
        for j in self._rendszer.legitarsasag.jaratok:
            print(f"- {j.jarat_info()}")
        
        jaratszam = input("Adja meg a jaratszamot: ")
        utas_nev = input("Adja meg az utas nevet: ")
        datum_str = input("Adja meg a datumot (YYYY-MM-DD formatumban): ")
        try:
            ar = self._rendszer.foglalas(jaratszam, utas_nev, datum_str)
            print(f"Sikeres foglalas! Ar: {ar} Ft")
        except ValueError as e:
            print(f"Hiba: {e}")
            
    def _menupont_lemondas(self):
        jaratszam = input("Adja meg a torlendo foglalas jaratszamat: ")
        utas_nev = input("Adja meg az utas nevet: ")
        datum_str = input("Adja meg a datumot (YYYY-MM-DD): ")
        try:
            self._rendszer.lemondas(jaratszam, utas_nev, datum_str)
            print("Keresett foglalas sikeresen lemondva.")
        except ValueError as e:
            print(f"Hiba: {e}")

    def _menupont_listazas(self):
        print("\nAktualis foglalasok:")
        foglalasok = self._rendszer.foglalasok
        if not foglalasok:
            print("Nincs egyetlen aktualis foglalas sem.")
            return
        
        for f in foglalasok:
            print(f"Utas: {f.utas_nev}, Jarat: {f.jarat.jaratszam} ({f.jarat.celallomas}), Datum: {f.datum.strftime('%Y-%m-%d')}")
