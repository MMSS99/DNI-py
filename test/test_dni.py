import pytest
from src.dni import Dni


def test_getNumero():
    assert Dni('3445523P').getNumero() == 3445523
    assert Dni('91409311C').getNumero() == 91409311
    assert Dni('32830547C').getNumero() == 32830547

def test_darLetra():
    assert Dni('3445523').darLetra() == '3445523P'
    assert Dni('91409311').darLetra() == '91409311C'
    assert Dni('32830547').darLetra() == '32830547W'

def test_comprobarLetra():
    assert Dni('3445523P').comprobarDni() == True
    assert Dni('91409311C').comprobarDni() == True
    assert Dni('32830547C').comprobarDni() == False