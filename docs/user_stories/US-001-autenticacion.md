\---

id: US-001

titulo: Autenticación de Usuarios - Sistema de Mejora Continua (SMC)

prioridad: Alta

story\_points: 5

sprint: 1

estado: COMPLETADO

filosofia: Lean Six Sigma

\---



\# US-001: Autenticación de Usuarios - SMC



\## RDM 2.1 - User Stories (Como... Quiero... Para...)

\*\*Como\*\* usuario registrado

\*\*Quiero\*\* iniciar sesión

\*\*Para\*\* acceder al sistema



\*\*Como\*\* usuario autenticado

\*\*Quiero\*\* editar mi perfil

\*\*Para\*\* mantener mis datos actualizados



\*\*Como\*\* auditor

\*\*Quiero\*\* auditar procesos

\*\*Para\*\* medir la calidad



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



\## RDM 2.5 - Trazabilidad

\- US-001

\- US-002

\- US-003

\- commit: 3f4a2b1

\- commit: 7c8d9e0

\- commit: 1a2b3c4

\- test\_login.py

\- test\_perfil.py

\- test\_dashboard.py



\## Descripción (RDM 2.1 - Entender necesidades)

\*\*Como\*\* profesional de mejora continua del Sistema de Mejora Continua (SMC)

\*\*Quiero\*\* iniciar sesión con mi email y contraseña

\*\*Para\*\* acceder de forma segura a las herramientas de Lean Six Sigma y auditoría de procesos



\## Criterios de Aceptación (RDM 2.2 - Transformar necesidades en requisitos)

\- \[x] El sistema debe mostrar un formulario de login con campos: email y contraseña

\- \[x] El email debe ser validado con formato correcto (nombre@dominio.com)

\- \[x] La contraseña debe ser hasheada con bcrypt antes de almacenarse

\- \[x] Al autenticarse correctamente, redirigir al dashboard de mejora continua

\- \[x] Mostrar mensaje de error para credenciales inválidas

\- \[x] La sesión debe persistir mediante JWT (expiración 24h)

\- \[x] El sistema debe permitir cerrar sesión

\- \[x] Registrar logs de acceso para auditoría de seguridad



\## Aprobación (RDM 2.3 - Entendimiento común)

\- \*\*Product Owner:\*\* María Rodríguez (aprobado: 2026-08-02)

\- \*\*Stakeholders:\*\* Equipo de Calidad (validated: 2026-08-02)

\- \*\*Champion Lean:\*\* Carlos Pérez (po: aprobado 2026-08-03)

\- \*\*Auditoría:\*\* Documento validado por el equipo completo



\## Trazabilidad (RDM 2.5 - Trazabilidad bidireccional)

\### Código Fuente

| Archivo | Descripción | Commit |

|---------|-------------|--------|

| src/login.py | Lógica de autenticación | 3f4a2b1 |



\### Pruebas

| Archivo | Descripción | Estado |

|---------|-------------|--------|

| tests/test\_login.py | Tests de autenticación | ✅ PASSED |



\## Cambios (RDM 2.4 - Gestión de cambios)

| Fecha | Cambio | Justificación |

|-------|--------|---------------|

| 2026-08-01 | Requisito creado | Necesidad de seguridad |

| 2026-08-03 | Añadido JWT | Mejora de seguridad |



\## Definition of Done (RDM 2.6 - Consistencia)

\- \[x] Código completado y revisado

\- \[x] Tests unitarios pasados (100% cobertura)

\- \[x] Tests de integración pasados

\- \[x] Documentación actualizada

\- \[x] Desplegado en entorno de pruebas

\- \[x] Aprobado por Product Owner

\- \[x] Revisión de calidad Lean Six Sigma



\*\*DoD verificada:\*\* Todos los items completados ✅

