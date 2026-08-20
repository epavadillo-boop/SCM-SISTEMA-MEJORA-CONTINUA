\---

id: US-003

titulo: Dashboard con Indicadores Lean - Sistema de Mejora Continua (SMC)

prioridad: Alta

story\_points: 8

sprint: 2

estado: EN\_PROGRESO

filosofia: Lean Six Sigma

\---



\# US-003: Dashboard con Indicadores Lean - SMC



\## Descripción (RDM 2.1 - Entender necesidades)



\*\*Como\*\* profesional de mejora continua del Sistema de Mejora Continua (SMC)

\*\*Quiero\*\* visualizar un dashboard con indicadores Lean

\*\*Para\*\* monitorear la eficiencia operativa y tomar decisiones basadas en datos



\## Criterios de Aceptación (RDM 2.2 - Transformar necesidades en requisitos)



\- \[ ] El sistema debe mostrar el indicador OEE (Overall Equipment Effectiveness)

\- \[ ] El sistema debe mostrar el Takt Time

\- \[ ] El sistema debe mostrar el Cycle Time

\- \[ ] Los indicadores deben actualizarse en tiempo real

\- \[ ] El dashboard debe mostrar gráficos de tendencia

\- \[ ] El usuario debe poder filtrar por período de tiempo

\- \[ ] El dashboard debe ser responsive (adaptable a móvil)



\## Aprobación (RDM 2.3 - Entendimiento común)



\- \*\*Product Owner:\*\* María Rodríguez (aprobado: 2026-08-03)

\- \*\*Stakeholders:\*\* Equipo de Operaciones (validated: 2026-08-03)

\- \*\*Champion Lean:\*\* Carlos Pérez (po: aprobado 2026-08-04)



\## Trazabilidad (RDM 2.5 - Trazabilidad bidireccional)



\### Código Fuente

| Archivo | Descripción | Commit |

|---------|-------------|--------|

| src/dashboard/metricas.py | Cálculo de métricas Lean | 2b3c4d5 |

| src/dashboard/graficos.py | Generación de gráficos | 6e7f8a9 |



\### Pruebas

| Archivo | Descripción | Estado |

|---------|-------------|--------|

| tests/test\_dashboard.py | Tests del dashboard | ⏳ PENDIENTE |

| tests/test\_metricas.py | Tests de métricas | ⏳ PENDIENTE |



\## Cambios (RDM 2.4 - Gestión de cambios)

| Fecha | Cambio | Justificación |

|-------|--------|---------------|

| 2026-08-03 | Requisito creado | Necesidad de visibilidad de KPIs |

| 2026-08-10 | Añadidos filtros por período | Solicitud de usuarios |



\## Definition of Done (RDM 2.6 - Consistencia)

\- \[ ] Código completado y revisado

\- \[ ] Tests unitarios pasados (100% cobertura)

\- \[ ] Tests de integración pasados

\- \[ ] Documentación actualizada

\- \[ ] Desplegado en entorno de pruebas

\- \[ ] Aprobado por Product Owner

\- \[ ] Revisión de calidad Lean Six Sigma



\*\*DoD pendiente:\*\* Items en progreso 🔄

