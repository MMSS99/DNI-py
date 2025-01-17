import pytest
from src.codigo_control import CodigoControl

def test_asignarLetra():
    assert CodigoControl().asignarLetra(3445523) == 'P'
    assert CodigoControl().asignarLetra(91409311) == 'C'
    assert CodigoControl().asignarLetra(32830547) == 'W'

def test_comprobarLetra():
    assert CodigoControl().comprobarLetra(3445523, 'P') == True
    assert CodigoControl().comprobarLetra(91409311, 'C') == True
    assert CodigoControl().comprobarLetra(32830547, 'C') == False