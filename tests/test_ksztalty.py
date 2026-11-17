import pytest

from autonomia.domena.bledy import BladScenariusza
from autonomia.domena.ksztalty import Prostokat, Okrag, Ksztalt


def test_punkt_w_srodku_nalezy_do_prostokata():
    p = Prostokat(x=10, y=5, szerokosc=3, wysokosc=12)
    assert p.zawiera_punkt(11.5, 11)


def test_punkt_poza_prostokatem_nie_nalezy():
    p = Prostokat(x=10, y=5, szerokosc=3, wysokosc=12)
    assert not p.zawiera_punkt(9, 6)


def test_punkt_w_rogu_nalezy_do_prostokata():
    p = Prostokat(x=1, y=2, szerokosc=5, wysokosc=6)
    assert p.zawiera_punkt(1, 2)


def test_punkt_na_krawedzi_nalezy_do_prostokata():
    p = Prostokat(x=0, y=0, szerokosc=2, wysokosc=5)
    assert p.zawiera_punkt(2, 3)


def test_szerokosc_zero_zglasza_blad_scenariusza():
    with pytest.raises(BladScenariusza):
        Prostokat(x=0, y=0, szerokosc=0, wysokosc=5)


def test_szerokosc_ujemna_zglasza_blad_scenariusza():
    with pytest.raises(BladScenariusza):
        Prostokat(x=0, y=0, szerokosc=-1, wysokosc=5)


def test_wysokosc_zero_zglasza_blad_scenariusza():
    with pytest.raises(BladScenariusza):
        Prostokat(x=0, y=0, szerokosc=2, wysokosc=0)


def test_wysokosc_ujemna_zglasza_blad_scenariusza():
    with pytest.raises(BladScenariusza):
        Prostokat(x=0, y=0, szerokosc=2, wysokosc=-2)


def test_punkt_blisko_dolnej_krawedzi_nalezy_do_prostokata():
    p = Prostokat(x=10, y=5, szerokosc=3, wysokosc=12)
    assert p.zawiera_punkt(11.5, 16)


def test_srodek_okregu_nalezy_do_niego():
    o = Okrag(x=1, y=1, promien=2)
    assert o.zawiera_punkt(1, 1)


def test_punkt_wyraznie_poza_okregiem_nie_nalezy_do_niego():
    o = Okrag(x=1, y=1, promien=2)
    assert not o.zawiera_punkt(10, 10)


def test_punkt_na_brzegu_nalezy_do_okregu():
    o = Okrag(x=1, y=1, promien=5)
    assert o.zawiera_punkt(4, 5)


def test_promien_zero_zglasza_blad_scenariusza():
    with pytest.raises(BladScenariusza):
        Okrag(x=1, y=1, promien=0)


def test_promien_ujemny_zglasza_blad_scenariusza():
    with pytest.raises(BladScenariusza):
        Okrag(x=1, y=1, promien=-2)


def test_punkt_w_rogu_kwadratu_opisanego_na_okregu_ale_poza_okregiem_nie_nalezy():
    o = Okrag(x=1, y=1, promien=2)
    assert not o.zawiera_punkt(3, 3)


def test_nie_mozna_utworzyc_obiektu_klasy_abstrakcyjnej():
    with pytest.raises(TypeError):
        Ksztalt()


def test_prostokat_i_okrag_to_ksztalty():
    p = Prostokat(x=1, y=1, szerokosc=3, wysokosc=4)
    o = Okrag(x=3, y=4, promien=7)
    assert isinstance(p, Ksztalt)
    assert isinstance(o, Ksztalt)


def test_polimorfizm_punkt_w_wielu_ksztaltach():
    p = Prostokat(x=1, y=1, szerokosc=4, wysokosc=4)
    o = Okrag(x=0, y=0, promien=4)
    ksztalty = [p, o]
    for k in ksztalty:
        assert k.zawiera_punkt(2, 2)