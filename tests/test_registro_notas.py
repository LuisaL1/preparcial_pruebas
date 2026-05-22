import pytest

from app.services.registro_notas_service import RegistroNotasService


def test_registrar_nota_valida():
    service = RegistroNotasService()

    resultado = service.registrar_nota(
        materia="Matemáticas",
        semestre="2026-1",
        nota=4.5
    )

    assert resultado["nota"] == 4.5


def test_no_permitir_notas_duplicadas_mismo_semestre():
    service = RegistroNotasService()

    service.registrar_nota("Matemáticas", "2026-1", 4.0)

    with pytest.raises(Exception):
        service.registrar_nota("Matemáticas", "2026-1", 3.5)


def test_permitir_misma_materia_en_semestre_diferente():
    service = RegistroNotasService()

    service.registrar_nota("Matemáticas", "2026-1", 4.0)

    resultado = service.registrar_nota(
        "Matemáticas",
        "2026-2",
        3.5
    )

    assert resultado["semestre"] == "2026-2"