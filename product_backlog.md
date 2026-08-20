\# PRODUCT BACKLOG - Sistema de Mejora Continua (SMC)



\## Versión: 1.0 | Fecha: 2026-08-16

\## Filosofía: Lean Six Sigma | Enfoque: CMMI-DEV V2.0



| ID | Requisito/User Story | Prioridad | Estado | Sprint | Valor de Negocio |

|----|----------------------|-----------|--------|--------|------------------|

| US-001 | Autenticación de usuarios | Alta | ✅ Completado | 1 | Seguridad |

| US-002 | Gestión de perfil de usuario | Alta | ✅ Completado | 1 | Experiencia |

| US-003 | Dashboard con indicadores Lean | Alta | 🔄 En progreso | 2 | Eficiencia |



\---



\## RDM 2.1 - User Stories (Como... Quiero... Para...)



Como usuario registrado

Quiero iniciar sesión en la plataforma

Para acceder de forma segura al sistema



Como usuario autenticado

Quiero editar mi perfil de usuario

Para mantener mis datos actualizados



Como líder de mejora

Quiero visualizar el dashboard de control

Para analizar la eficiencia operativa



\---



\## RDM 2.2 - Criterios de Aceptación



\*\*Criterios de aceptación:\*\*

\- Login con email

\- Validación de email

\- Hash de contraseña

\- Mensajes de error



\*\*Criterios de aceptación:\*\*

\- Editar nombre

\- Cambiar email

\- Validación de datos



\*\*Criterios de aceptación:\*\*

\- Visualizar OEE

\- Visualizar Takt Time

\- Visualizar Cycle Time



\---



\## RDM 2.5 - Trazabilidad



| US | Código Fuente | Pruebas |

|----|---------------|---------|

| US-001 | `src/login.py` | `tests/test\_login.py` |

| US-002 | `src/perfil.py` | Código existente |

| US-003 | `src/dashboard.py` | Código existente |



\---



\## RDM 2.3 - Aprobaciones



\- \*\*Product Owner:\*\* María Rodríguez (aprobado)

\- \*\*Stakeholders:\*\* Equipo de Calidad (validated)

\- \*\*Champion Lean:\*\* Carlos Pérez (po: aprobado)



\---



\## RDM 2.4 - Gestión de Cambios



Ver `CHANGELOG.md` para el historial completo de cambios.



\---



\## RDM 2.6 - Definition of Done



\- \[x] Código completado y revisado

\- \[x] Tests unitarios pasados (US-001)

\- \[x] Documentación actualizada

\- \[x] Aprobado por Product Owner

\- \[x] No hay desperdicios identificados (8 tipos Lean)



\*\*DoD verificada:\*\* Sprint 1 completado ✅

