"""Scenariusz: świat oraz punkty startu i celu robota."""
from autonomia.domena.bledy import BladScenariusza


class Scenariusz:
    """Świat razem z punktem startu i celu robota.

    Start i cel to pary (x, y) w metrach. Oba punkty muszą leżeć w mapie
    i poza blokami, inaczej konstruktor zgłasza BladScenariusza. Klasa nie
    wie nic o plikach: obiekt można zbudować z YAML, z testu lub z edytora.
    Obiekt jest niezmienny.
    """

    def __init__(self, nazwa, swiat, start, cel):
        for opis, punkt in (("start", start), ("cel", cel)):
            if not swiat.jest_wolne(*punkt):
                raise BladScenariusza(
                    f"{opis} {punkt} lezy poza mapa lub w bloku"
                )
        self._nazwa = nazwa
        self._swiat = swiat
        self._start = start
        self._cel = cel

    @property
    def nazwa(self):
        return self._nazwa

    @property
    def swiat(self):
        return self._swiat

    @property
    def start(self):
        return self._start

    @property
    def cel(self):
        return self._cel
