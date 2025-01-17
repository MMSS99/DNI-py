import pytest
from src.codigo_control import CodigoControl

def test_asignarLetra():
    assert CodigoControl(3445523).asignarLetra() == 'P'
    assert CodigoControl(91409311).asignarLetra() == 'C'
    assert CodigoControl(32830547).asignarLetra() == 'W'

def test_comprobarLetra():
    assert CodigoControl(3445523, 'P').comprobarLetra() == True
    assert CodigoControl(91409311, 'C').comprobarLetra() == True
    assert CodigoControl(32830547, 'C').comprobarLetra() == False