class JegyFoglalas:
    def __init__(self, jarat, utas_nev, datum):
        self._jarat = jarat
        self._utas_nev = utas_nev
        self._datum = datum

    @property
    def jarat(self):
        return self._jarat

    @property
    def utas_nev(self):
        return self._utas_nev

    @property
    def datum(self):
        return self._datum
