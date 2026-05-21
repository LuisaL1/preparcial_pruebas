from app.exceptions.exceptions import NotaInvalidaError


class RegistroNotasService:
    """Servicio simple para registrar notas con validación básica."""

    def registrar_nota(self, materia: str, semestre: str, nota: float) -> dict:
        """Registra una nota validando que esté entre 0.0 y 5.0.

        Devuelve un diccionario con los datos de la nota si es válida.
        Lanza `NotaInvalidaError` si la nota está fuera de rango.
        """
        try:
            valor = float(nota)
        except (TypeError, ValueError):
            raise NotaInvalidaError("La nota debe ser un número")

        if valor < 0.0 or valor > 5.0:
            raise NotaInvalidaError("La nota debe estar entre 0.0 y 5.0")

        return {
            "materia": materia,
            "semestre": semestre,
            "nota": valor,
        }
