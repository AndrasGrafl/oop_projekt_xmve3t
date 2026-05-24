class LegiTarsasag:
    def __init__(self, nev):
        self._nev = nev
        self._jaratok = []

    @property
    def nev(self):
        return self._nev

    @property
    def jaratok(self):
        return self._jaratok

    @jaratok.setter
    def jaratok(self, uj_jarat):
        self._jaratok.append(uj_jarat)
