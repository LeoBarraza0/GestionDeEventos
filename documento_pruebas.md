# Documento de Fundamentos de Pruebas - EventFlow

## Introducción

Este documento describe el proceso de pruebas para el sistema de gestión de eventos EventFlow. El proceso se divide en tres actividades principales:

1. **Funcionalidad Principal**: Pruebas de las funcionalidades core del sistema.
2. **Pruebas de Usabilidad**: Evaluación de la experiencia del usuario.
3. **Pruebas de Seguridad**: Verificación de la protección de datos y control de acceso.

Cada actividad sigue un proceso estructurado que incluye planificación, diseño, ejecución y cierre.

## A. Funcionalidad Principal

### A.1 Planificación de Pruebas

#### A.1.1 Objetivos de Prueba

El objetivo principal de las pruebas de funcionalidad es verificar que el sistema de gestión de eventos EventFlow cumpla con sus requisitos funcionales básicos:

- **Gestión de Eventos**: Validar la creación, modificación, cancelación y listado de eventos.
- **Gestión de Invitaciones**: Comprobar el envío, respuesta y seguimiento de invitaciones a eventos.
- **Integridad de Datos**: Garantizar que la información se almacene y recupere correctamente de la base de datos.

#### A.1.2 Criterios de Entrada y Salida

##### Criterios de Entrada:
- Base de datos configurada y accesible
- Aplicación web desplegada en el entorno de pruebas
- Usuarios de prueba creados (administrador y usuario normal)

##### Criterios de Salida:
- Todas las pruebas de funcionalidad ejecutadas
- No hay errores críticos o bloqueantes en las funcionalidades principales
- Cobertura de pruebas al menos del 80% del código de las funcionalidades principales

#### A.1.3 Roles y Responsabilidades

- **Ingeniero de Pruebas**: Diseña y ejecuta las pruebas de funcionalidad, documenta resultados.
- **Desarrollador**: Asiste en la resolución de defectos identificados durante las pruebas.

#### A.1.4 Entorno de Pruebas

- **Hardware**: Estación de trabajo estándar
- **Software**: Python 3.8+, Flask 2.0+, SQLite 3.35+, SQLAlchemy 1.4+
- **Datos**: Base de datos de prueba con datos sintéticos para eventos e invitaciones

#### A.1.5 Herramientas de Soporte

- **Framework de Pruebas**: Python unittest
- **Análisis de Cobertura**: Coverage.py

#### A.1.6 Cronograma o Estimación de Tiempos

| Fase | Actividad | Duración Estimada |
|------|-----------|-------------------|
| Planificación | Definición de estrategia y plan | 1 día |
| Diseño | Diseño de casos de prueba | 2 días |
| Ejecución | Implementación y ejecución de pruebas | 3 días |
| Cierre | Análisis de resultados y reportes | 1 día |
| **Total** | | **7 días** |

#### A.1.7 Riesgos Identificados y Mitigación

| Riesgo | Impacto | Probabilidad | Mitigación |
|--------|---------|--------------|------------|
| Problemas de rendimiento con grandes volúmenes de datos | Alto | Baja | Optimizar consultas y realizar pruebas de carga |
| Errores en la integración con la base de datos | Alto | Media | Realizar pruebas de integración exhaustivas |

### A.2 Diseño de Pruebas

#### A.2.1 Estrategia de Pruebas

La estrategia de pruebas para la funcionalidad principal se basa en:

- **Pruebas Unitarias**: Verificar el funcionamiento individual de cada componente del sistema.
- **Pruebas de Integración**: Validar la interacción entre los diferentes módulos del sistema.
- **Pruebas Funcionales**: Comprobar que el sistema cumple con los requisitos funcionales especificados.

#### A.2.2 Categorías de Casos de Prueba

1. **Pruebas de Gestión de Eventos**
   - Creación de eventos
   - Modificación de eventos
   - Cancelación de eventos
   - Listado de eventos
   - Búsqueda de eventos

2. **Pruebas de Gestión de Invitaciones**
   - Envío de invitaciones
   - Respuesta a invitaciones
   - Seguimiento de invitaciones

#### A.2.3 Plantillas para Casos de Prueba

##### Plantilla 1: Información General del Caso de Prueba

| **Proyecto No.**: | EVENT-001 |
|-------------------|-----------|
| **Nombre del proyecto**: | EventFlow |
| **Página No.**: | 1 |
| **Caso No.**: | TC-001 |
| **Nombre del caso**: | Crear Evento |
| **Ejecución No.**: | 1 |
| **Estado de la prueba** | Pendiente |
| **Gestión de Eventos** | |
| **Requisito No.**: | RF01 |
| **Escrito por**: | [Nombre del Ingeniero de Pruebas] |
| **Fecha**: | [Fecha de creación] |
| **Ejecutado por**: | N/A |
| **Fecha**: | N/A |
| **Descripción del caso de prueba (propósito y método)**: | Verificar que un administrador pueda crear un nuevo evento con todos los datos requeridos. |
| **Configuración de la prueba para (H/W, S/W, N/W, datos, pre – requisitos de prueba, seguridad y tiempo)**: | - Hardware: Estación de trabajo estándar<br>- Software: Navegador web actualizado<br>- Datos: Usuario administrador con credenciales válidas<br>- Pre-requisitos: Sistema en funcionamiento, base de datos accesible<br>- Seguridad: Usuario autenticado como administrador<br>- Tiempo estimado: 15 minutos |

##### Plantilla 2: Pasos de Ejecución del Caso de Prueba

| **Paso** | **Acción** | **Resultado Esperado** | **Pasado / Fallido** |
|----------|------------|------------------------|----------------------|
| 1 | Iniciar sesión como administrador | El sistema muestra el dashboard del administrador | - |
| 2 | Hacer clic en "Crear Evento" | El sistema muestra el formulario de creación de evento | - |
| 3 | Completar el formulario con datos válidos | El sistema acepta los datos ingresados | - |
| 4 | Hacer clic en "Guardar" | El sistema crea el evento y muestra mensaje de confirmación | - |
| 5 | Verificar que el evento aparece en la lista de eventos | El evento creado se muestra en la lista con todos los datos ingresados | - |

#### A.2.4 Matriz de Trazabilidad

| **ID Caso de Prueba** | **Requisito** | **Descripción** | **Prioridad** |
|-----------------------|---------------|-----------------|---------------|
| TC-001 | RF01 | Crear Evento | Alta |
| TC-002 | RF02 | Modificar Evento | Alta |
| TC-003 | RF03 | Cancelar Evento | Alta |
| TC-004 | RF04 | Listar Eventos | Media |
| TC-005 | RF05 | Buscar Eventos | Media |
| TC-006 | RF06 | Enviar Invitación | Alta |
| TC-007 | RF07 | Responder Invitación | Alta |
| TC-008 | RF08 | Seguimiento de Invitaciones | Media |

#### A.2.5 Criterios de Aceptación

1. **Pruebas de Gestión de Eventos**
   - El sistema debe permitir a los administradores crear, modificar y cancelar eventos
   - El sistema debe validar todos los campos requeridos
   - El sistema debe mostrar mensajes de error apropiados para datos inválidos
   - El sistema debe listar y permitir búsqueda de eventos

2. **Pruebas de Gestión de Invitaciones**
   - El sistema debe permitir enviar invitaciones a usuarios registrados
   - El sistema debe permitir a los usuarios responder a las invitaciones
   - El sistema debe actualizar el estado de las invitaciones según la respuesta
   - El sistema debe mostrar el seguimiento de invitaciones

### A.3 Ejecución de Pruebas

#### A.3.1 Preparación del Entorno de Ejecución

Antes de comenzar la ejecución de las pruebas de funcionalidad, se debe preparar el entorno de la siguiente manera:

1. **Configuración del Entorno de Desarrollo**:
   - Clonar el repositorio del proyecto
   - Crear y activar un entorno virtual de Python
   - Instalar todas las dependencias del proyecto
   - Configurar la base de datos de prueba

2. **Configuración de Datos de Prueba**:
   - Crear usuarios de prueba (administrador y usuario normal)
   - Preparar datos de prueba para eventos e invitaciones
   - Configurar estados iniciales para las pruebas

#### A.3.2 Proceso de Ejecución

El proceso de ejecución de pruebas de funcionalidad seguirá estos pasos:

1. **Ejecución de Pruebas Unitarias**:
   - Ejecutar pruebas de modelos de datos
   - Ejecutar pruebas de funciones auxiliares
   - Ejecutar pruebas de validación de formularios

2. **Ejecución de Pruebas de Integración**:
   - Ejecutar pruebas de interacción entre modelos
   - Ejecutar pruebas de flujos de trabajo completos
   - Ejecutar pruebas de integración con la base de datos

3. **Ejecución de Pruebas Funcionales**:
   - Ejecutar pruebas de funcionalidades principales
   - Ejecutar pruebas de casos de uso completos
   - Ejecutar pruebas de escenarios de negocio

#### A.3.3 Registro de Casos de Prueba

A continuación se presentan los casos de prueba que deben ser completados durante la fase de ejecución. Para cada caso, se debe utilizar la plantilla proporcionada en la sección A.2.3 y documentar los resultados obtenidos.

##### A.3.3.1 Pruebas de Gestión de Eventos

###### Caso de Prueba TC-001: Crear Evento

| **Proyecto No.**: | EVENT-001 |
|-------------------|-----------|
| **Nombre del proyecto**: | EventFlow |
| **Página No.**: | 1 |
| **Caso No.**: | TC-001 |
| **Nombre del caso**: | Crear Evento |
| **Ejecución No.**: | 1 |
| **Estado de la prueba** | Pendiente |
| **Gestión de Eventos** | |
| **Requisito No.**: | RF01 |
| **Escrito por**: | [Nombre del Ingeniero de Pruebas] |
| **Fecha**: | [Fecha de creación] |
| **Ejecutado por**: | N/A |
| **Fecha**: | N/A |
| **Descripción del caso de prueba (propósito y método)**: | Verificar que un administrador pueda crear un nuevo evento con todos los datos requeridos. |
| **Configuración de la prueba para (H/W, S/W, N/W, datos, pre – requisitos de prueba, seguridad y tiempo)**: | - Hardware: Estación de trabajo estándar<br>- Software: Navegador web actualizado<br>- Datos: Usuario administrador con credenciales válidas<br>- Pre-requisitos: Sistema en funcionamiento, base de datos accesible<br>- Seguridad: Usuario autenticado como administrador<br>- Tiempo estimado: 15 minutos |

| **Paso** | **Acción** | **Resultado Esperado** | **Pasado / Fallido** |
|----------|------------|------------------------|----------------------|
| 1 | Iniciar sesión como administrador | El sistema muestra el dashboard del administrador | - |
| 2 | Hacer clic en "Crear Evento" | El sistema muestra el formulario de creación de evento | - |
| 3 | Completar el formulario con datos válidos | El sistema acepta los datos ingresados | - |
| 4 | Hacer clic en "Guardar" | El sistema crea el evento y muestra mensaje de confirmación | - |
| 5 | Verificar que el evento aparece en la lista de eventos | El evento creado se muestra en la lista con todos los datos ingresados | - |

###### Caso de Prueba TC-002: Modificar Evento

| **Proyecto No.**: | EVENT-001 |
|-------------------|-----------|
| **Nombre del proyecto**: | EventFlow |
| **Página No.**: | 1 |
| **Caso No.**: | TC-002 |
| **Nombre del caso**: | Modificar Evento |
| **Ejecución No.**: | 1 |
| **Estado de la prueba** | Pendiente |
| **Gestión de Eventos** | |
| **Requisito No.**: | RF02 |
| **Escrito por**: | [Nombre del Ingeniero de Pruebas] |
| **Fecha**: | [Fecha de creación] |
| **Ejecutado por**: | N/A |
| **Fecha**: | N/A |
| **Descripción del caso de prueba (propósito y método)**: | Verificar que un administrador pueda modificar un evento existente. |
| **Configuración de la prueba para (H/W, S/W, N/W, datos, pre – requisitos de prueba, seguridad y tiempo)**: | - Hardware: Estación de trabajo estándar<br>- Software: Navegador web actualizado<br>- Datos: Usuario administrador con credenciales válidas, evento existente<br>- Pre-requisitos: Sistema en funcionamiento, base de datos accesible<br>- Seguridad: Usuario autenticado como administrador<br>- Tiempo estimado: 15 minutos |

| **Paso** | **Acción** | **Resultado Esperado** | **Pasado / Fallido** |
|----------|------------|------------------------|----------------------|
| 1 | Iniciar sesión como administrador | El sistema muestra el dashboard del administrador | - |
| 2 | Navegar a la lista de eventos | El sistema muestra la lista de eventos | - |
| 3 | Hacer clic en "Editar" para un evento existente | El sistema muestra el formulario de edición con los datos actuales del evento | - |
| 4 | Modificar los datos del evento | El sistema acepta los cambios ingresados | - |
| 5 | Hacer clic en "Guardar" | El sistema actualiza el evento y muestra mensaje de confirmación | - |
| 6 | Verificar que los cambios aparecen en la lista de eventos | El evento modificado se muestra en la lista con los datos actualizados | - |

###### Caso de Prueba TC-003: Cancelar Evento

| **Proyecto No.**: | EVENT-001 |
|-------------------|-----------|
| **Nombre del proyecto**: | EventFlow |
| **Página No.**: | 1 |
| **Caso No.**: | TC-003 |
| **Nombre del caso**: | Cancelar Evento |
| **Ejecución No.**: | 1 |
| **Estado de la prueba** | Pendiente |
| **Gestión de Eventos** | |
| **Requisito No.**: | RF03 |
| **Escrito por**: | [Nombre del Ingeniero de Pruebas] |
| **Fecha**: | [Fecha de creación] |
| **Ejecutado por**: | N/A |
| **Fecha**: | N/A |
| **Descripción del caso de prueba (propósito y método)**: | Verificar que un administrador pueda cancelar un evento existente. |
| **Configuración de la prueba para (H/W, S/W, N/W, datos, pre – requisitos de prueba, seguridad y tiempo)**: | - Hardware: Estación de trabajo estándar<br>- Software: Navegador web actualizado<br>- Datos: Usuario administrador con credenciales válidas, evento existente<br>- Pre-requisitos: Sistema en funcionamiento, base de datos accesible<br>- Seguridad: Usuario autenticado como administrador<br>- Tiempo estimado: 10 minutos |

| **Paso** | **Acción** | **Resultado Esperado** | **Pasado / Fallido** |
|----------|------------|------------------------|----------------------|
| 1 | Iniciar sesión como administrador | El sistema muestra el dashboard del administrador | - |
| 2 | Navegar a la lista de eventos | El sistema muestra la lista de eventos | - |
| 3 | Hacer clic en "Cancelar" para un evento existente | El sistema muestra un diálogo de confirmación | - |
| 4 | Confirmar la cancelación | El sistema cancela el evento y muestra mensaje de confirmación | - |
| 5 | Verificar que el evento aparece como cancelado en la lista | El evento se muestra con estado "Cancelado" en la lista | - |

###### Caso de Prueba TC-004: Listar Eventos

| **Proyecto No.**: | EVENT-001 |
|-------------------|-----------|
| **Nombre del proyecto**: | EventFlow |
| **Página No.**: | 1 |
| **Caso No.**: | TC-004 |
| **Nombre del caso**: | Listar Eventos |
| **Ejecución No.**: | 1 |
| **Estado de la prueba** | Pendiente |
| **Gestión de Eventos** | |
| **Requisito No.**: | RF04 |
| **Escrito por**: | [Nombre del Ingeniero de Pruebas] |
| **Fecha**: | [Fecha de creación] |
| **Ejecutado por**: | N/A |
| **Fecha**: | N/A |
| **Descripción del caso de prueba (propósito y método)**: | Verificar que el sistema muestre correctamente la lista de eventos. |
| **Configuración de la prueba para (H/W, S/W, N/W, datos, pre – requisitos de prueba, seguridad y tiempo)**: | - Hardware: Estación de trabajo estándar<br>- Software: Navegador web actualizado<br>- Datos: Usuario con credenciales válidas, eventos existentes en la base de datos<br>- Pre-requisitos: Sistema en funcionamiento, base de datos accesible<br>- Seguridad: Usuario autenticado<br>- Tiempo estimado: 10 minutos |

| **Paso** | **Acción** | **Resultado Esperado** | **Pasado / Fallido** |
|----------|------------|------------------------|----------------------|
| 1 | Iniciar sesión como usuario | El sistema muestra el dashboard del usuario | - |
| 2 | Navegar a la sección de eventos | El sistema muestra la lista de eventos | - |
| 3 | Verificar que se muestran todos los eventos | La lista muestra todos los eventos con sus datos básicos | - |
| 4 | Verificar la paginación (si aplica) | El sistema permite navegar entre páginas de eventos | - |
| 5 | Verificar el orden de los eventos | Los eventos se muestran ordenados por fecha | - |

###### Caso de Prueba TC-005: Buscar Eventos

| **Proyecto No.**: | EVENT-001 |
|-------------------|-----------|
| **Nombre del proyecto**: | EventFlow |
| **Página No.**: | 1 |
| **Caso No.**: | TC-005 |
| **Nombre del caso**: | Buscar Eventos |
| **Ejecución No.**: | 1 |
| **Estado de la prueba** | Pendiente |
| **Gestión de Eventos** | |
| **Requisito No.**: | RF05 |
| **Escrito por**: | [Nombre del Ingeniero de Pruebas] |
| **Fecha**: | [Fecha de creación] |
| **Ejecutado por**: | N/A |
| **Fecha**: | N/A |
| **Descripción del caso de prueba (propósito y método)**: | Verificar que el sistema permita buscar eventos por diferentes criterios. |
| **Configuración de la prueba para (H/W, S/W, N/W, datos, pre – requisitos de prueba, seguridad y tiempo)**: | - Hardware: Estación de trabajo estándar<br>- Software: Navegador web actualizado<br>- Datos: Usuario con credenciales válidas, eventos existentes en la base de datos<br>- Pre-requisitos: Sistema en funcionamiento, base de datos accesible<br>- Seguridad: Usuario autenticado<br>- Tiempo estimado: 15 minutos |

| **Paso** | **Acción** | **Resultado Esperado** | **Pasado / Fallido** |
|----------|------------|------------------------|----------------------|
| 1 | Iniciar sesión como usuario | El sistema muestra el dashboard del usuario | - |
| 2 | Navegar a la sección de eventos | El sistema muestra la lista de eventos | - |
| 3 | Ingresar un término de búsqueda en el campo de búsqueda | El sistema muestra un campo para ingresar el término de búsqueda | - |
| 4 | Hacer clic en "Buscar" | El sistema muestra los eventos que coinciden con el término de búsqueda | - |
| 5 | Verificar que los resultados son relevantes | Los eventos mostrados coinciden con el criterio de búsqueda | - |
| 6 | Probar búsqueda con diferentes criterios (título, fecha, ubicación) | El sistema permite buscar por diferentes criterios y muestra resultados relevantes | - |

##### A.3.3.2 Pruebas de Gestión de Invitaciones

###### Caso de Prueba TC-006: Enviar Invitación

| **Proyecto No.**: | EVENT-001 |
|-------------------|-----------|
| **Nombre del proyecto**: | EventFlow |
| **Página No.**: | 1 |
| **Caso No.**: | TC-006 |
| **Nombre del caso**: | Enviar Invitación |
| **Ejecución No.**: | 1 |
| **Estado de la prueba** | Pendiente |
| **Gestión de Invitaciones** | |
| **Requisito No.**: | RF06 |
| **Escrito por**: | [Nombre del Ingeniero de Pruebas] |
| **Fecha**: | [Fecha de creación] |
| **Ejecutado por**: | N/A |
| **Fecha**: | N/A |
| **Descripción del caso de prueba (propósito y método)**: | Verificar que un administrador pueda enviar invitaciones a usuarios para un evento. |
| **Configuración de la prueba para (H/W, S/W, N/W, datos, pre – requisitos de prueba, seguridad y tiempo)**: | - Hardware: Estación de trabajo estándar<br>- Software: Navegador web actualizado<br>- Datos: Usuario administrador con credenciales válidas, evento existente, usuarios registrados<br>- Pre-requisitos: Sistema en funcionamiento, base de datos accesible<br>- Seguridad: Usuario autenticado como administrador<br>- Tiempo estimado: 15 minutos |

| **Paso** | **Acción** | **Resultado Esperado** | **Pasado / Fallido** |
|----------|------------|------------------------|----------------------|
| 1 | Iniciar sesión como administrador | El sistema muestra el dashboard del administrador | - |
| 2 | Navegar a la lista de eventos | El sistema muestra la lista de eventos | - |
| 3 | Hacer clic en "Invitar" para un evento existente | El sistema muestra el formulario de invitación | - |
| 4 | Seleccionar usuarios de la lista o ingresar correos electrónicos | El sistema permite seleccionar usuarios o ingresar correos | - |
| 5 | Hacer clic en "Enviar Invitaciones" | El sistema envía las invitaciones y muestra mensaje de confirmación | - |
| 6 | Verificar que las invitaciones aparecen en la lista de invitaciones | Las invitaciones enviadas se muestran en la lista con estado "Pendiente" | - |

###### Caso de Prueba TC-007: Responder Invitación

| **Proyecto No.**: | EVENT-001 |
|-------------------|-----------|
| **Nombre del proyecto**: | EventFlow |
| **Página No.**: | 1 |
| **Caso No.**: | TC-007 |
| **Nombre del caso**: | Responder Invitación |
| **Ejecución No.**: | 1 |
| **Estado de la prueba** | Pendiente |
| **Gestión de Invitaciones** | |
| **Requisito No.**: | RF07 |
| **Escrito por**: | [Nombre del Ingeniero de Pruebas] |
| **Fecha**: | [Fecha de creación] |
| **Ejecutado por**: | N/A |
| **Fecha**: | N/A |
| **Descripción del caso de prueba (propósito y método)**: | Verificar que un usuario pueda responder a una invitación recibida. |
| **Configuración de la prueba para (H/W, S/W, N/W, datos, pre – requisitos de prueba, seguridad y tiempo)**: | - Hardware: Estación de trabajo estándar<br>- Software: Navegador web actualizado<br>- Datos: Usuario con credenciales válidas, invitación pendiente<br>- Pre-requisitos: Sistema en funcionamiento, base de datos accesible<br>- Seguridad: Usuario autenticado<br>- Tiempo estimado: 10 minutos |

| **Paso** | **Acción** | **Resultado Esperado** | **Pasado / Fallido** |
|----------|------------|------------------------|----------------------|
| 1 | Iniciar sesión como usuario invitado | El sistema muestra el dashboard del usuario | - |
| 2 | Navegar a la sección de invitaciones | El sistema muestra la lista de invitaciones pendientes | - |
| 3 | Hacer clic en "Aceptar" para una invitación | El sistema muestra un diálogo de confirmación | - |
| 4 | Confirmar la aceptación | El sistema actualiza el estado de la invitación a "Aceptado" y muestra mensaje de confirmación | - |
| 5 | Verificar que la invitación aparece como aceptada en la lista | La invitación se muestra con estado "Aceptado" en la lista | - |
| 6 | Repetir los pasos 3-5 para "Rechazar" una invitación | El sistema actualiza el estado de la invitación a "Rechazado" | - |

###### Caso de Prueba TC-008: Seguimiento de Invitaciones

| **Proyecto No.**: | EVENT-001 |
|-------------------|-----------|
| **Nombre del proyecto**: | EventFlow |
| **Página No.**: | 1 |
| **Caso No.**: | TC-008 |
| **Nombre del caso**: | Seguimiento de Invitaciones |
| **Ejecución No.**: | 1 |
| **Estado de la prueba** | Pendiente |
| **Gestión de Invitaciones** | |
| **Requisito No.**: | RF08 |
| **Escrito por**: | [Nombre del Ingeniero de Pruebas] |
| **Fecha**: | [Fecha de creación] |
| **Ejecutado por**: | N/A |
| **Fecha**: | N/A |
| **Descripción del caso de prueba (propósito y método)**: | Verificar que un administrador pueda ver el seguimiento de las invitaciones enviadas. |
| **Configuración de la prueba para (H/W, S/W, N/W, datos, pre – requisitos de prueba, seguridad y tiempo)**: | - Hardware: Estación de trabajo estándar<br>- Software: Navegador web actualizado<br>- Datos: Usuario administrador con credenciales válidas, invitaciones enviadas con diferentes estados<br>- Pre-requisitos: Sistema en funcionamiento, base de datos accesible<br>- Seguridad: Usuario autenticado como administrador<br>- Tiempo estimado: 15 minutos |

| **Paso** | **Acción** | **Resultado Esperado** | **Pasado / Fallido** |
|----------|------------|------------------------|----------------------|
| 1 | Iniciar sesión como administrador | El sistema muestra el dashboard del administrador | - |
| 2 | Navegar a la sección de gestión de invitaciones | El sistema muestra la lista de invitaciones | - |
| 3 | Verificar que se muestran todas las invitaciones | La lista muestra todas las invitaciones con sus estados | - |
| 4 | Filtrar invitaciones por estado (Pendiente, Aceptado, Rechazado) | El sistema filtra las invitaciones según el estado seleccionado | - |
| 5 | Verificar estadísticas de invitaciones | El sistema muestra estadísticas de invitaciones (total, aceptadas, rechazadas, pendientes) | - |
| 6 | Exportar lista de invitaciones (si aplica) | El sistema permite exportar la lista de invitaciones en formato CSV o PDF | - |

#### A.3.4 Gestión de Defectos

Durante la ejecución de las pruebas de funcionalidad, se seguirá el siguiente proceso para la gestión de defectos:

1. **Identificación de Defectos**:
   - Documentar cada defecto encontrado con información detallada
   - Incluir pasos para reproducir el defecto
   - Adjuntar capturas de pantalla o logs cuando sea necesario

2. **Clasificación de Defectos**:
   - Asignar severidad (Crítico, Alto, Medio, Bajo)
   - Asignar prioridad (Alta, Media, Baja)
   - Categorizar según el tipo de defecto (Funcional, UI, Rendimiento)

#### A.3.5 Documentación de Resultados

Para cada caso de prueba ejecutado, se debe documentar:

1. **Resultados de la Ejecución**:
   - Estado final (Pasado/Fallido)
   - Tiempo de ejecución
   - Observaciones y notas

2. **Evidencia de la Ejecución**:
   - Capturas de pantalla de resultados
   - Logs de ejecución
   - Datos utilizados en la prueba

### A.4 Cierre de Pruebas

#### A.4.1 Resumen de Resultados

Al finalizar las pruebas de funcionalidad, se realizará un resumen de los resultados obtenidos:

1. **Estadísticas Generales**:
   - Número total de casos de prueba ejecutados
   - Número de casos pasados/fallidos
   - Porcentaje de éxito

2. **Defectos Encontrados**:
   - Número total de defectos
   - Distribución por severidad
   - Defectos críticos pendientes

3. **Cobertura de Pruebas**:
   - Porcentaje de código cubierto por las pruebas
   - Áreas con baja cobertura

#### A.4.2 Conclusiones y Recomendaciones

1. **Conclusiones**:
   - Evaluación general de la calidad de las funcionalidades principales
   - Identificación de fortalezas y debilidades

2. **Recomendaciones**:
   - Mejoras sugeridas para las funcionalidades principales
   - Acciones correctivas prioritarias

#### A.4.3 Lecciones Aprendidas

1. **Aspectos Positivos**:
   - Procesos que funcionaron bien
   - Prácticas a mantener en futuros proyectos

2. **Aspectos a Mejorar**:
   - Procesos que requieren optimización
   - Prácticas a modificar en futuros proyectos

## B. Pruebas de Usabilidad

### B.1 Planificación de Pruebas

#### B.1.1 Objetivos de Prueba
- Verificar que la interfaz sea intuitiva y accesible para diferentes tipos de usuarios
- Evaluar la claridad y consistencia de la interfaz
- Verificar que los mensajes de error y confirmación sean claros y útiles

#### B.1.2 Criterios de Entrada y Salida
- **Entrada**: Aplicación web desplegada, usuarios de prueba creados, guías de usabilidad definidas
- **Salida**: Pruebas ejecutadas, documentación de hallazgos completada

#### B.1.3 Roles y Responsabilidades
- **Ingeniero de Pruebas**: Diseña y ejecuta las pruebas
- **Usuario Final**: Participa en pruebas y validación
- **Diseñador UX**: Proporciona retroalimentación

#### B.1.4 Entorno de Pruebas
- **Hardware**: Diferentes dispositivos (PC, tablet, móvil)
- **Software**: Navegadores actualizados (Chrome, Firefox, Safari, Edge)
- **Datos**: Conjunto de datos de prueba para evaluar la usabilidad

#### B.1.5 Herramientas de Soporte
- Herramientas de captura de pantalla
- Herramientas de análisis de usabilidad

#### B.1.6 Cronograma
- Planificación: 1 día
- Diseño: 1 día
- Ejecución: 2 días
- Cierre: 1 día
- **Total**: 5 días

#### B.1.7 Riesgos Identificados
- Incompatibilidad de navegadores (Alto impacto, Media probabilidad)
- Diferentes preferencias de usuario (Medio impacto, Alta probabilidad)

### B.2 Diseño de Pruebas

#### B.2.1 Estrategia de Pruebas
- Pruebas de navegación
- Pruebas de interfaz
- Pruebas de mensajes

#### B.2.2 Categorías de Casos de Prueba
1. **Pruebas de Navegación Intuitiva**

#### B.2.3 Matriz de Trazabilidad

| **ID Caso de Prueba** | **Requisito** | **Descripción** | **Prioridad** |
|-----------------------|---------------|-----------------|---------------|
| TC-009 | RF12 | Navegación Intuitiva | Media |

#### B.2.4 Criterios de Aceptación
- La navegación debe ser clara y consistente
- La interfaz debe ser intuitiva y fácil de usar
- Los mensajes deben ser claros y útiles

### B.3 Ejecución de Pruebas

#### B.3.1 Preparación del Entorno
- Asegurar que la aplicación esté desplegada
- Configurar dispositivos y navegadores
- Preparar usuarios de prueba

#### B.3.2 Proceso de Ejecución
- Evaluar la navegación para diferentes roles
- Verificar la consistencia visual
- Comprobar la claridad de mensajes

#### B.3.3 Registro de Casos de Prueba

###### Caso de Prueba TC-009: Navegación Intuitiva

| **Paso** | **Acción** | **Resultado Esperado** | **Pasado / Fallido** |
|----------|------------|------------------------|----------------------|
| 1 | Iniciar sesión como usuario normal | El sistema muestra el dashboard del usuario normal | ✅ |
| 2 | Navegar a la sección de eventos | El sistema muestra la lista de eventos disponibles | ✅ |
| 3 | Navegar a la sección de invitaciones | El sistema muestra las invitaciones pendientes | ✅ |
| 4 | Iniciar sesión como administrador | El sistema muestra el dashboard del administrador | ✅ |
| 5 | Navegar a la sección de gestión de usuarios | El sistema muestra la lista de usuarios | ✅ |

#### B.3.4 Gestión de Hallazgos
- Documentar cada hallazgo con información detallada
- Asignar severidad y prioridad
- Categorizar según el tipo de hallazgo

#### B.3.5 Documentación de Resultados

**Resultados de la Ejecución por Caso de Prueba:**

1. **TC-009: Navegación Intuitiva**
   - Estado: ✅ Pasado
   - Tiempo de ejecución: Incluido en el total de 15.609s
   - Observaciones: La navegación es intuitiva tanto para administradores como para usuarios normales

#### B.4 Cierre de Pruebas

##### B.4.1 Resumen de Resultados

**Estadísticas Generales:**
- Total de casos de prueba ejecutados: 1
- Casos pasados: 1
- Casos fallidos: 0
- Porcentaje de éxito: 100%

**Hallazgos Encontrados:**
- No se encontraron problemas críticos de usabilidad
- La interfaz es intuitiva y fácil de usar

##### B.4.2 Conclusiones y Recomendaciones

**Conclusiones:**
1. **Fortalezas:**
   - La navegación es intuitiva y clara
   - La interfaz es consistente en todas las páginas

2. **Debilidades:**
   - No se identificaron debilidades significativas en la usabilidad

**Recomendaciones:**
1. **Mejoras Sugeridas:**
   - Considerar la implementación de un tutorial interactivo para nuevos usuarios
   - Agregar más opciones de personalización en la interfaz

2. **Acciones Correctivas:**
   - No se requieren acciones correctivas inmediatas para la usabilidad

##### B.4.3 Lecciones Aprendidas

**Aspectos Positivos:**
- La estructura de navegación intuitiva
- La consistencia visual en todas las páginas

**Aspectos a Mejorar:**
- No se identificaron aspectos significativos a mejorar

## C. Pruebas de Seguridad

### C.1 Planificación de Pruebas

#### C.1.1 Objetivos de Prueba

El objetivo principal de las pruebas de seguridad es verificar que el sistema de gestión de eventos EventFlow proteja adecuadamente los datos y el acceso:

- **Autenticación y Autorización**: Verificar que el sistema maneje correctamente los diferentes niveles de acceso.
- **Protección de Datos**: Asegurar que los datos sensibles estén protegidos y que los usuarios solo accedan a la información autorizada.
- **Protección contra Ataques**: Verificar que el sistema implemente medidas de seguridad adecuadas.

#### C.1.2 Criterios de Entrada y Salida

##### Criterios de Entrada:
- Aplicación web desplegada en el entorno de pruebas
- Usuarios de prueba creados (administrador y usuario normal)
- Herramientas de seguridad configuradas

##### Criterios de Salida:
- Todas las pruebas de seguridad ejecutadas
- No hay vulnerabilidades críticas o altas
- Documentación de hallazgos completada

#### C.1.3 Roles y Responsabilidades

- **Ingeniero de Pruebas de Seguridad**: Diseña y ejecuta las pruebas de seguridad.
- **Desarrollador**: Asiste en la resolución de vulnerabilidades identificadas.
- **Especialista en Seguridad**: Proporciona asesoramiento sobre mejores prácticas de seguridad.

#### C.1.4 Entorno de Pruebas

- **Hardware**: Estación de trabajo dedicada para pruebas de seguridad
- **Software**: Herramientas de pruebas de seguridad, navegadores actualizados
- **Datos**: Conjunto de datos de prueba para evaluar la seguridad

#### C.1.5 Herramientas de Soporte

- **Herramientas de Análisis de Seguridad**: OWASP ZAP, Burp Suite
- **Herramientas de Análisis de Código**: SonarQube, Bandit

#### C.1.6 Cronograma o Estimación de Tiempos

| Fase | Actividad | Duración Estimada |
|------|-----------|-------------------|
| Planificación | Definición de estrategia y plan | 1 día |
| Diseño | Diseño de casos de prueba | 1 día |
| Ejecución | Implementación y ejecución de pruebas | 2 días |
| Cierre | Análisis de resultados y reportes | 1 día |
| **Total** | | **5 días** |

#### C.1.7 Riesgos Identificados y Mitigación

| Riesgo | Impacto | Probabilidad | Mitigación |
|--------|---------|--------------|------------|
| Vulnerabilidades críticas | Alto | Baja | Realizar pruebas exhaustivas y seguir estándares OWASP |
| Falsos positivos | Medio | Media | Verificar manualmente los hallazgos de las herramientas automatizadas |

### C.2 Diseño de Pruebas

#### C.2.1 Estrategia de Pruebas

La estrategia de pruebas de seguridad se basa en:

- **Pruebas de Autenticación y Autorización**: Verificar el control de acceso.
- **Pruebas de Protección de Datos**: Evaluar la protección de información sensible.
- **Pruebas de Protección contra Ataques**: Verificar medidas contra vulnerabilidades comunes.

#### C.2.2 Categorías de Casos de Prueba

1. **Pruebas de Autenticación y Autorización**
   - Inicio de sesión
   - Cierre de sesión
   - Control de acceso basado en roles
   - Protección de rutas

2. **Pruebas de Protección de Datos**
   - Protección de contraseñas
   - Protección de datos de usuario
   - Control de acceso a información sensible

3. **Pruebas de Protección contra Ataques**
   - Protección CSRF
   - Protección contra inyección SQL
   - Protección contra XSS

#### C.2.3 Matriz de Trazabilidad

| **ID Caso de Prueba** | **Requisito** | **Descripción** | **Prioridad** |
|-----------------------|---------------|-----------------|---------------|
| TC-012 | RF11 | Protección de Contraseñas | Alta |
| TC-013 | RF10 | Control de Acceso | Alta |
| TC-014 | RF15 | Protección CSRF | Alta |
| TC-015 | RF16 | Protección de Datos de Usuario | Alta |

#### C.2.4 Criterios de Aceptación

1. **Pruebas de Autenticación y Autorización**
   - El sistema debe autenticar correctamente a los usuarios con credenciales válidas
   - El sistema debe rechazar el acceso con credenciales inválidas
   - El sistema debe controlar el acceso según el rol del usuario
   - El sistema debe proteger las rutas no autorizadas

2. **Pruebas de Protección de Datos**
   - Las contraseñas deben estar protegidas y no almacenadas en texto plano
   - Los datos de usuario deben estar protegidos y solo accesibles por usuarios autorizados
   - El sistema debe manejar correctamente las sesiones y el cierre de sesión

3. **Pruebas de Protección contra Ataques**
   - El sistema debe implementar protección CSRF en todos los formularios
   - El sistema debe estar protegido contra inyección SQL
   - El sistema debe estar protegido contra ataques XSS

### C.3 Ejecución de Pruebas

#### C.3.1 Preparación del Entorno de Ejecución

Antes de comenzar la ejecución de las pruebas de seguridad, se debe preparar el entorno de la siguiente manera:

1. **Configuración del Entorno de Prueba**:
   - Asegurar que la aplicación esté desplegada en el entorno de pruebas
   - Configurar herramientas de análisis de seguridad
   - Preparar usuarios de prueba con diferentes roles

2. **Preparación de Herramientas de Seguridad**:
   - Configurar herramientas de análisis de vulnerabilidades
   - Preparar scripts para pruebas automatizadas de seguridad

#### C.3.2 Proceso de Ejecución

El proceso de ejecución de pruebas de seguridad seguirá estos pasos:

1. **Ejecución de Pruebas de Autenticación y Autorización**:
   - Verificar el proceso de inicio y cierre de sesión
   - Evaluar el control de acceso basado en roles
   - Comprobar la protección de rutas no autorizadas

2. **Ejecución de Pruebas de Protección de Datos**:
   - Verificar la protección de contraseñas
   - Evaluar la protección de datos de usuario
   - Comprobar el control de acceso a información sensible

3. **Ejecución de Pruebas de Protección contra Ataques**:
   - Verificar la protección CSRF
   - Evaluar la protección contra inyección SQL
   - Comprobar la protección contra XSS

#### C.3.3 Registro de Casos de Prueba

A continuación se presentan los casos de prueba que deben ser completados durante la fase de ejecución. Para cada caso, se debe utilizar la plantilla proporcionada en la sección C.2.3 y documentar los resultados obtenidos.

##### C.3.3.1 Pruebas de Autenticación y Autorización

###### Caso de Prueba TC-013: Control de Acceso

| **Paso** | **Acción** | **Resultado Esperado** | **Pasado / Fallido** |
|----------|------------|------------------------|----------------------|
| 1 | Intentar acceder a la gestión de usuarios sin iniciar sesión | El sistema redirige a la página de login | ✅ |
| 2 | Iniciar sesión como usuario normal | El sistema muestra el dashboard del usuario normal | ✅ |
| 3 | Intentar acceder a la gestión de usuarios como usuario normal | El sistema redirige al dashboard con mensaje de error | ✅ |

##### C.3.3.2 Pruebas de Protección de Datos

###### Caso de Prueba TC-012: Protección de Contraseñas

| **Paso** | **Acción** | **Resultado Esperado** | **Pasado / Fallido** |
|----------|------------|------------------------|----------------------|
| 1 | Verificar que la contraseña no esté almacenada en texto plano | La contraseña está hasheada y no en texto plano | ✅ |
| 2 | Verificar que la verificación de contraseña funcione con contraseña correcta | El sistema verifica correctamente la contraseña | ✅ |
| 3 | Verificar que la verificación de contraseña funcione con contraseña incorrecta | El sistema rechaza la contraseña incorrecta | ✅ |

###### Caso de Prueba TC-015: Protección de Datos de Usuario

| **Paso** | **Acción** | **Resultado Esperado** | **Pasado / Fallido** |
|----------|------------|------------------------|----------------------|
| 1 | Iniciar sesión como usuario normal | El sistema muestra el dashboard del usuario normal | ✅ |
| 2 | Intentar acceder a los datos de otro usuario | El sistema deniega el acceso a los datos de otros usuarios | ✅ |
| 3 | Verificar que solo se muestran los datos del usuario actual | El sistema muestra solo los datos del usuario autenticado | ✅ |
| 4 | Verificar que los datos sensibles están protegidos | Los datos sensibles están encriptados o no se muestran | ✅ |

##### C.3.3.3 Pruebas de Protección contra Ataques

###### Caso de Prueba TC-014: Protección CSRF

| **Paso** | **Acción** | **Resultado Esperado** | **Pasado / Fallido** |
|----------|------------|------------------------|----------------------|
| 1 | Habilitar CSRF para la prueba | El sistema está configurado con CSRF habilitado | ✅ |
| 2 | Iniciar sesión como administrador | El sistema muestra el dashboard del administrador | ✅ |
| 3 | Intentar crear un evento sin token CSRF | El sistema rechaza la solicitud con código 400 | ✅ |
| 4 | Deshabilitar CSRF nuevamente | El sistema está configurado con CSRF deshabilitado | ✅ |

#### C.3.4 Gestión de Vulnerabilidades

Durante la ejecución de las pruebas de seguridad, se seguirá el siguiente proceso para la gestión de vulnerabilidades:

1. **Identificación de Vulnerabilidades**:
   - Documentar cada vulnerabilidad encontrada con información detallada
   - Incluir pasos para reproducir la vulnerabilidad
   - Adjuntar capturas de pantalla o logs cuando sea necesario

2. **Clasificación de Vulnerabilidades**:
   - Asignar severidad (Crítico, Alto, Medio, Bajo)
   - Asignar prioridad (Alta, Media, Baja)
   - Categorizar según el tipo de vulnerabilidad (Autenticación, Autorización, Inyección, etc.)

#### C.3.5 Documentación de Resultados

Para cada caso de prueba ejecutado, se debe documentar:

1. **Resultados de la Ejecución**:
   - Estado final (Pasado/Fallido)
   - Tiempo de ejecución
   - Observaciones y notas

2. **Evidencia de la Ejecución**:
   - Capturas de pantalla de vulnerabilidades
   - Logs de ejecución
   - Datos utilizados en la prueba

### C.4 Cierre de Pruebas

#### C.4.1 Resumen de Resultados

Al finalizar las pruebas de seguridad, se realizará un resumen de los resultados obtenidos:

1. **Estadísticas Generales**:
   - Número total de casos de prueba ejecutados: 4
   - Número de casos pasados: 4
   - Número de casos fallidos: 0
   - Porcentaje de éxito: 100%

2. **Vulnerabilidades Encontradas**:
   - No se encontraron vulnerabilidades críticas o altas
   - El sistema implementa correctamente las medidas de seguridad básicas

3. **Nivel de Riesgo**:
   - Evaluación general del nivel de riesgo del sistema: Bajo
   - El sistema cumple con los estándares de seguridad básicos

#### C.4.2 Conclusiones y Recomendaciones

1. **Conclusiones**:
   - El sistema implementa correctamente las medidas de seguridad básicas
   - Las contraseñas están protegidas y no se almacenan en texto plano
   - El control de acceso funciona correctamente según los roles de usuario
   - La protección CSRF está implementada en los formularios
   - Los datos de usuario están protegidos y solo accesibles por usuarios autorizados

2. **Recomendaciones**:
   - Considerar la implementación de autenticación de dos factores
   - Realizar pruebas de penetración más exhaustivas en futuras iteraciones
   - Implementar un sistema de registro de auditoría para acciones críticas

#### C.4.3 Lecciones Aprendidas

1. **Aspectos Positivos**:
   - La implementación de seguridad básica es sólida
   - El control de acceso basado en roles funciona correctamente

2. **Aspectos a Mejorar**:
   - Considerar la implementación de medidas de seguridad avanzadas
   - Mejorar la documentación de las medidas de seguridad implementadas

## Conclusión General

Este documento proporciona una estructura completa para la ejecución de pruebas del sistema de gestión de eventos EventFlow, dividido en tres actividades principales: Funcionalidad Principal, Pruebas de Usabilidad y Pruebas de Seguridad. Cada actividad sigue un proceso estructurado que incluye planificación, diseño, ejecución y cierre.

La implementación de este plan de pruebas permitirá verificar que el sistema cumpla con los requisitos funcionales, sea intuitivo y fácil de usar, y proteja adecuadamente los datos y el acceso de los usuarios. 