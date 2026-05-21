# Registro de Notas Académicas

Proyecto desarrollado para la actividad preparatoria del primer parcial de Pruebas de Software.

---

# Descripción

El sistema permite:

- Registrar notas de estudiantes
- Validar notas entre 0.0 y 5.0
- Determinar aprobación o reprobación
- Calcular promedio de notas
- Evitar notas duplicadas por materia y semestre

---

# Tecnologías Utilizadas

- Python
- pytest
- pytest-bdd
- GitHub Actions

---

# Estructura del Proyecto

```plaintext
registro_notas/
│
├── app/
├── tests/
│   ├── unit/
│   └── bdd/
├── .github/workflows/
├── requirements.txt
└── README.md
```

---

# Parte 1 — Análisis

## Particiones de Equivalencia

| Partición | Valor | Resultado |
|---|---|---|
| Nota válida | 3.5 | Válida |
| Nota menor a 0 | -1.0 | Error |
| Nota mayor a 5 | 5.5 | Error |

---

## Valores Límite

| Valor | Resultado |
|---|---|
| -0.1 | Error |
| 0.0 | Válida |
| 5.0 | Válida |
| 5.1 | Error |

---

## Preguntas al Product Owner

1. ¿Se puede modificar una nota ya registrada?  
Esto afecta las pruebas relacionadas con duplicados.

2. ¿“Matemáticas” y “matemáticas” cuentan como la misma materia?  
Esto impacta las validaciones de comparación.

---

# Parte 2 — Casos de Prueba

| ID | Req | Descripción | Resultado Esperado |
|---|---|---|---|
| CP-01 | R1 | Registrar nota válida | Nota registrada |
| CP-02 | R1 | Registrar nota menor a 0 | Error |
| CP-03 | R1 | Registrar nota mayor a 5 | Error |
| CP-04 | R2 | Nota igual a 3.0 | Aprueba |
| CP-05 | R2 | Nota menor a 3.0 | Reprueba |
| CP-06 | R3 | Calcular promedio | Promedio correcto |
| CP-07 | R3 | Estudiante sin notas | Resultado controlado |
| CP-08 | R4 | Nota duplicada mismo semestre | Error |
| CP-09 | R4 | Misma materia diferente semestre | Registro válido |

---

# Parte 3 — TDD

El desarrollo se realizó siguiendo el ciclo:

- 🔴 RED
- 🟢 GREEN
- 🔵 REFACTOR

## Cobertura

```bash
pytest --cov=app
```

Cobertura obtenida: **95%**

---

# Parte 4 — BDD

Se implementaron escenarios Gherkin para:

- Aprobación
- Promedios
- Validación de duplicados

Ejemplo:

```gherkin
Scenario: Aprobar una materia
  When el estudiante registra una nota de 4.0
  Then el estudiante aprueba la materia
```

---

# Parte 5 — CI/CD

Se configuró GitHub Actions para:

- Ejecutar tests unitarios
- Ejecutar tests BDD
- Validar cobertura

---

# Reflexión

Diseñar pruebas antes de programar ayudó a identificar escenarios importantes desde el inicio y facilitó la implementación.

Lo más difícil del TDD fue evitar escribir lógica antes de crear los tests.