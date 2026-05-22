import pytest

from app.services.registro_notas_service import RegistroNotasService
from app.exceptions.exceptions import NotaInvalidaError


def test_no_permitir_nota_menor_a_cero():
    service = RegistroNotasService()

    with pytest.raises(NotaInvalidaError):
        service.registrar_nota(
            materia="Matemáticas",
            semestre="2026-1",
            nota=-1.0
        )


def test_no_permitir_nota_mayor_a_cinco():
    service = RegistroNotasService()

    with pytest.raises(NotaInvalidaError):
        service.registrar_nota(
            materia="Matemáticas",
            semestre="2026-1",
            nota=5.5
        )


def test_estudiante_aprueba_con_nota_mayor_o_igual_a_tres():
    service = RegistroNotasService()

    resultado = service.aprobo_materia(3.0)

    assert resultado is True


def test_estudiante_reprueba_con_nota_menor_a_tres():
    service = RegistroNotasService()

    resultado = service.aprobo_materia(2.9)

    assert resultado is False