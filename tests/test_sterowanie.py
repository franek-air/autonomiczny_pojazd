import pytest

from autonomia.domena.bledy import BladSterowania
from autonomia.domena.sterowanie import Sterowanie


def test_domyslne_sterowanie_to_stan_spoczynku():
    s = Sterowanie()
    assert s.gaz == 0.0
    assert s.hamulec == 0.0
    assert s.omega == 0.0


def test_poprawne_wartosci_sa_zapamietane():
    s = Sterowanie(gaz=0.6, omega=-0.5)
    assert s.gaz == 0.6
    assert s.hamulec == 0.0
    assert s.omega == -0.5


def test_gaz_powyzej_zakresu_zglasza_blad():
    with pytest.raises(BladSterowania):
        Sterowanie(gaz=1.1)


def test_gaz_ponizej_zakresu():
    with pytest.raises(BladSterowania):
        Sterowanie(gaz=-0.1)


def test_hamulec_powyzej_zakresu():
    with pytest.raises(BladSterowania):
        Sterowanie(hamulec=1.1)


def test_hamulec_ponizej_zakresu():
    with pytest.raises(BladSterowania):
        Sterowanie(hamulec=-0.1)


def test_gaz_i_hamulec_jednoczesnie():
    with pytest.raises(BladSterowania):
        Sterowanie(gaz=0.2, hamulec=0.2)


def test_przypadek_brzegowy():
    s = Sterowanie(hamulec=1.0)
    assert s.hamulec == 1.0


def test_tylko_do_odczytu():
    s = Sterowanie()
    with pytest.raises(AttributeError):
        s.gaz = 0.5
