Feature: Registro de notas académicas

  Como coordinador académico
  Quiero registrar notas de estudiantes
  Para controlar aprobación y desempeño académico

  Background:
    Given el sistema de notas está disponible

  @smoke
  Scenario Outline: Validar aprobación de estudiantes

    When el estudiante registra una nota de <nota>
    Then el resultado de aprobación debe ser <resultado>

    Examples:
      | nota | resultado |
      | 2.5  | False      |
      | 3.0  | True       |
      | 4.5  | True       |

  @critical
  Scenario: Calcular promedio de notas

    When el estudiante tiene las notas 3.0, 4.0 y 5.0
    Then el promedio debe ser 4.0

  @regression
  Scenario: No permitir notas duplicadas

    Given ya existe una nota registrada para Matemáticas en 2026-1
    When se intenta registrar otra nota para Matemáticas en 2026-1
    Then el sistema debe mostrar un error de nota duplicada