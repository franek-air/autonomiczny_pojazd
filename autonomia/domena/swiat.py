"""Świat robota: prostokątna mapa z szarymi blokami."""
from autonomia.domena.bledy import BladScenariusza


class Swiat:
    """Prostokątna mapa o stałym rozmiarze z szarymi blokami.

    Układ współrzędnych: (0, 0) to lewy górny róg mapy, x rośnie w prawo,
    a y w dół. Wymiary podajemy w metrach i muszą być dodatnie, inaczej
    konstruktor zgłasza BladScenariusza.

    Świat składa się z kształtów (Ksztalt) i nie wie, czy dany blok jest
    prostokątem, czy okręgiem. Blok można dodać tylko wtedy, gdy mieści się
    w granicach mapy, a dotknięcie granicy jest dozwolone. Lista bloków jest
    prywatna: z zewnątrz widać ją jako krotkę, więc bloki dodaje się wyłącznie
    przez dodaj_blok, które pilnuje poprawności.
    """

    def __init__(self, szerokosc, wysokosc):
        if not szerokosc > 0:
            raise BladScenariusza(f"szerokosc musi byc dodatnia: {szerokosc}")
        if not wysokosc > 0:
            raise BladScenariusza(f"wysokosc musi byc dodatnia: {wysokosc}")

        self._bloki = []
        self._szerokosc = szerokosc
        self._wysokosc = wysokosc

    @property
    def szerokosc(self):
        return self._szerokosc

    @property
    def wysokosc(self):
        return self._wysokosc

    @property
    def bloki(self):
        return tuple(self._bloki)

    def dodaj_blok(self, ksztalt):
        (x_min, y_min, x_max, y_max) = ksztalt.obwiednia()
        if not (x_min >= 0 and y_min >= 0 and x_max <= self.szerokosc and y_max <= self.wysokosc):
            raise BladScenariusza(f"blok nie miesci sie w granicach mapy: {(x_min, y_min, x_max, y_max)}")
        self._bloki.append(ksztalt)

    def jest_wolne(self, px, py):
        if not (0 <= px <= self.szerokosc and 0 <= py <= self.wysokosc):
            return False
        for k in self.bloki:
            if k.zawiera_punkt(px, py):
                return False
        return True