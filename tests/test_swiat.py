import pytest

from autonomia.domena.bledy import BladScenariusza
from autonomia.domena.ksztalty import Okrag, Prostokat
from autonomia.domena.swiat import Swiat


def test_nowy_swiat_nie_ma_blokow():
    swiat = Swiat(szerokosc=40, wysokosc=25)
    assert swiat.bloki == ()


def test_dodany_blok_pojawia_sie_w_swiecie():
    swiat = Swiat(szerokosc=40, wysokosc=25)
    regal = Prostokat(x=10, y=5, szerokosc=3, wysokosc=12)
    swiat.dodaj_blok(regal)
    assert len(swiat.bloki) == 1
    assert swiat.bloki[0] is regal


def test_bloki_zwraca_krotke():
    swiat = Swiat(szerokosc=40, wysokosc=25)
    assert isinstance(swiat.bloki, tuple)


def test_blok_wystajacy_poza_prawa_krawedz_zglasza_blad_scenariusza():
    swiat = Swiat(szerokosc=40, wysokosc=25)
    with pytest.raises(BladScenariusza):
        swiat.dodaj_blok(Prostokat(x=38, y=5, szerokosc=5, wysokosc=3))


def test_blok_wystajacy_poza_dolna_krawedz_zglasza_blad_scenariusza():
    swiat = Swiat(szerokosc=40, wysokosc=25)
    with pytest.raises(BladScenariusza):
        swiat.dodaj_blok(Prostokat(x=5, y=22, szerokosc=2, wysokosc=5))


def test_okrag_wystajacy_poza_lewa_krawedz_zglasza_blad_scenariusza():
    swiat = Swiat(szerokosc=40, wysokosc=25)
    with pytest.raises(BladScenariusza):
        swiat.dodaj_blok(Okrag(x=1, y=1, promien=2))


def test_blok_dotykajacy_granic_mapy_jest_poprawny():
    swiat = Swiat(szerokosc=40, wysokosc=25)
    swiat.dodaj_blok(Prostokat(x=35, y=20, szerokosc=5, wysokosc=5))
    assert len(swiat.bloki) == 1


def test_szerokosc_swiata_zero_zglasza_blad_scenariusza():
    with pytest.raises(BladScenariusza):
        Swiat(szerokosc=0, wysokosc=25)


def test_wysokosc_swiata_ujemna_zglasza_blad_scenariusza():
    with pytest.raises(BladScenariusza):
        Swiat(szerokosc=40, wysokosc=-1)


def test_punkt_wewnatrz_prostokata_nie_jest_wolny():
    swiat = Swiat(szerokosc=40, wysokosc=25)
    swiat.dodaj_blok(Prostokat(x=10, y=5, szerokosc=3, wysokosc=12))
    assert not swiat.jest_wolne(11, 10)


def test_punkt_wewnatrz_okregu_nie_jest_wolny():
    swiat = Swiat(szerokosc=40, wysokosc=25)
    swiat.dodaj_blok(Prostokat(x=10, y=5, szerokosc=3, wysokosc=12))
    swiat.dodaj_blok(Okrag(x=20, y=20, promien=1.5))
    assert not swiat.jest_wolne(20.5, 20.5)


def test_punkt_w_mapie_poza_blokami_jest_wolny():
    swiat = Swiat(szerokosc=40, wysokosc=25)
    swiat.dodaj_blok(Prostokat(x=10, y=5, szerokosc=3, wysokosc=12))
    assert swiat.jest_wolne(30, 20)


def test_punkt_poza_mapa_nie_jest_wolny():
    swiat = Swiat(szerokosc=40, wysokosc=25)
    assert not swiat.jest_wolne(45, 10)


def test_punkt_na_granicy_mapy_jest_wolny():
    swiat = Swiat(szerokosc=40, wysokosc=25)
    assert swiat.jest_wolne(0, 0)