from app.services.registro_notas_service import RegistroNotasService


def test_registrar_nota_valida():
    service = RegistroNotasService()

    resultado = service.registrar_nota(
        materia="Matemáticas",
        semestre="2026-1",
        nota=4.5
    )

    assert resultado["nota"] == 4.5