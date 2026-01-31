from kalkulator import *

def test_addisjon():
    resultat = addisjon(2, 3)
    assert resultat == 5

def test_subtraksjon():
    resultat = subtraksjon(10,2)
    assert resultat == 8

def test_multiplikasjon():
    resultat = multiplikasjon(3,4)
    assert resultat == 12