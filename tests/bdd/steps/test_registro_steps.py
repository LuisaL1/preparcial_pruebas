from pytest_bdd import (
    scenarios,
    given,
    when,
    then,
    parsers
)

from app.services.registro_notas_service import (
    RegistroNotasService
)

from app.exceptions.exceptions import (
    NotaDuplicadaError
)

scenarios("../features/registro_notas.feature")


@given(
    "el sistema de notas está disponible",
    target_fixture="sistema_notas"
)
def sistema_notas():

    return RegistroNotasService()

@when(parsers.parse(
    "el estudiante registra una nota de {nota:f}"
))
def registrar_nota(sistema_notas, nota):

    sistema_notas.resultado = (
        sistema_notas.aprobo_materia(nota)
    )


@then(parsers.parse(
    "el resultado de aprobación debe ser {resultado}"
))
def validar_aprobacion(
    sistema_notas,
    resultado
):

    esperado = resultado == "True"

    assert sistema_notas.resultado == esperado


@when(
    "el estudiante tiene las notas 3.0, 4.0 y 5.0"
)
def calcular_promedio(sistema_notas):

    sistema_notas.promedio = (
        sistema_notas.calcular_promedio(
            [3.0, 4.0, 5.0]
        )
    )


@then("el promedio debe ser 4.0")
def validar_promedio(sistema_notas):

    assert sistema_notas.promedio == 4.0


@given(
    "ya existe una nota registrada para Matemáticas en 2026-1"
)
def nota_existente(sistema_notas):

    sistema_notas.registrar_nota(
        "Matemáticas",
        "2026-1",
        4.0
    )


@when(
    "se intenta registrar otra nota para Matemáticas en 2026-1"
)
def registrar_duplicada(sistema_notas):

    try:

        sistema_notas.registrar_nota(
            "Matemáticas",
            "2026-1",
            3.5
        )

    except NotaDuplicadaError as error:

        sistema_notas.error = str(error)


@then(
    "el sistema debe mostrar un error de nota duplicada"
)
def validar_error(sistema_notas):

    assert (
        sistema_notas.error
        == "Ya existe una nota registrada para esta materia y semestre"
    )