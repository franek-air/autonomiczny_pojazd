"""Sygnały sterujące wysyłane do napędu robota."""
from autonomia.domena.bledy import BladSterowania

class Sterowanie:
    """Sygnały wysyłane do silnika i hamulców w jednym kroku symulacji."""

    def __init__(self, gaz=0.0, hamulec=0.0, omega=0.0):
        if not 0.0 <= gaz <= 1.0:
            raise BladSterowania(f"gaz poza zakresem [0, 1]: {gaz}")
        if not 0.0 <= hamulec <= 1.0:
            raise BladSterowania(f"hamulec poza zakresem [0, 1]: {hamulec}")
        if gaz > 0.0 and hamulec > 0.0:
            raise BladSterowania(f"hamulec ({hamulec}) i gaz ({gaz}) wcisniete na raz")
        self._gaz = gaz
        self._hamulec = hamulec
        self._omega = omega

    @property
    def gaz(self):
        return self._gaz

    @property
    def hamulec(self):
        return self._hamulec

    @property
    def omega(self):
        return self._omega