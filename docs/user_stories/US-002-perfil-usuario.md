\---

id: US-002

titulo: Gestión de Perfil de Usuario - Sistema de Mejora Continua (SMC)

prioridad: Alta

story\_points: 3

sprint: 1

estado: COMPLETADO

filosofia: Lean Six Sigma

\---



\# US-002: Gestión de Perfil de Usuario - SMC



\## Descripción (RDM 2.1 - Entender necesidades)



\*\*Como\*\* usuario autenticado del Sistema de Mejora Continua (SMC)

\*\*Quiero\*\* gestionar mi perfil de usuario

\*\*Para\*\* mantener actualizada mi información personal y de contacto



\## Criterios de Aceptación (RDM 2.2 - Transformar necesidades en requisitos)



\- \[x] El sistema debe permitir editar nombre y apellidos

\- \[x] El sistema debe permitir cambiar email (con validación de formato)

\- \[x] El sistema debe permitir cambiar contraseña (con confirmación)

\- \[x] El sistema debe mostrar mensajes de confirmación al guardar cambios

\- \[x] El sistema debe mostrar mensajes de error si los datos son inválidos

\- \[x] Los cambios deben reflejarse inmediatamente en el perfil



\## Aprobación (RDM 2.3 - Entendimiento común)



\- \*\*Product Owner:\*\* María Rodríguez (aprobado: 2026-08-02)

\- \*\*Stakeholders:\*\* Equipo de UX (validated: 2026-08-02)

\- \*\*Champion Lean:\*\* Carlos Pérez (po: aprobado 2026-08-03)



\## Trazabilidad (RDM 2.5 - Trazabilidad bidireccional)



\### Código Fuente

| Archivo | Descripción | Commit |

|---------|-------------|--------|

| src/perfil/editar.py | Lógica de edición de perfil | 4b5c6d7 |

| src/perfil/validar.py | Validación de datos | 8e9f0a1 |



\### Pruebas

| Archivo | Descripción | Estado |

|---------|-------------|--------|

| tests/test\_perfil.py | Tests de gestión de perfil | ✅ PASSED |

| tests/test\_validacion.py | Tests de validación | ✅ PASSED |



\### Tareas Técnicas

| ID | Tarea | Responsable | Horas |

|----|-------|-------------|-------|

| TASK-004 | Diseñar formulario de perfil | Ana | 3 |

| TASK-005 | Implementar edición de perfil | Carlos | 5 |

| TASK-006 | Implementar validaciones | Luis | 2 |



\## Cambios (RDM 2.4 - Gestión de cambios)

| Fecha | Cambio | Justificación |

|-------|--------|---------------|

| 2026-08-02 | Requisito creado | Necesidad de gestión de usuarios |

| 2026-08-05 | Añadida validación de email | Mejora de UX |



\## Métricas de Mejora Continua

\- \*\*Tiempo de desarrollo:\*\* 10 horas (vs 12 estimadas)

\- \*\*Eficiencia:\*\* 83%

\- \*\*Defectos encontrados:\*\* 1 (corregido)

\- \*\*Satisfacción del equipo:\*\* 4.8/5



\## Definition of Done (RDM 2.6 - Consistencia)

\- \[x] Código completado y revisado

\- \[x] Tests unitarios pasados (100% cobertura)

\- \[x] Tests de integración pasados

\- \[x] Documentación actualizada

\- \[x] Desplegado en entorno de pruebas

\- \[x] Aprobado por Product Owner

\- \[x] Revisión de calidad Lean Six Sigma

\- \[x] No hay desperdicios identificados (8 tipos Lean)



\*\*DoD verificada:\*\* Todos los items completados ✅

