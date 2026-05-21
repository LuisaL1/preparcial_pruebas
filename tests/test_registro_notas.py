import pytest

from app.services.registro_notas_service import RegistroNotasService
from app.exceptions.exceptions import NotaInvalidaError


def test_registrar_nota_valida():
    service = RegistroNotasService()

    resultado = service.registrar_nota(
        materia="Matemáticas",
        semestre="2026-1",
        nota=4.5
    )

    assert resultado["nota"] == 4.5


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