from app.services.registro_notas_service import RegistroNotasService


def test_calcular_promedio_de_varias_notas():
    service = RegistroNotasService()

    notas = [3.0, 4.0, 5.0]

    resultado = service.calcular_promedio(notas)

    assert resultado == 4.0


def test_calcular_promedio_con_una_nota():
    service = RegistroNotasService()

    notas = [4.5]

    resultado = service.calcular_promedio(notas)

    assert resultado == 4.5


def test_calcular_promedio_sin_notas():
    service = RegistroNotasService()

    notas = []

    resultado = service.calcular_promedio(notas)

    assert resultado == 0