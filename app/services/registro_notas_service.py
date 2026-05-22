from app.exceptions.exceptions import NotaInvalidaError


class RegistroNotasService:
    """Servicio para registrar notas académicas."""

    def registrar_nota(self, materia: str, semestre: str, nota: float) -> dict:

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

    def aprobo_materia(self, nota: float) -> bool:
        return nota >= 3.0

    def calcular_promedio(self, notas: list) -> float:

        if len(notas) == 0:
            return 0

        return sum(notas) / len(notas)