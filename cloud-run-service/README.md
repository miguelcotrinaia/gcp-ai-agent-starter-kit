# Servicio del agente para Google Cloud Run

Esta carpeta será la fuente única del **backend ejecutable** del agente (Flask, LangChain, LangGraph, RAG y persistencia).

No es el repositorio de las interfaces. Los frontends viven en `agentui-withoutlogin` y `agentui-withlogin` y también se desplegarán en Cloud Run como servicios independientes.

## Relación con el episodio 09

En [`09-despliegue-docker-cloud-run/`](../09-despliegue-docker-cloud-run/) se explicará cómo integrar el agente con la API Flask, empaquetarlo con Docker y desplegarlo. Aquí se conservará el código probado, no una segunda copia por episodio.

## Estado

Aún falta revisar e integrar los archivos de despliegue que tiene el autor. Por ese motivo no se incluye un Dockerfile ni configuración ficticia que aparenten estar listos para producción.

## Seguridad requerida

- Credenciales fuera del código; usar Secret Manager y permisos IAM mínimos.
- Contrato de API basado en solicitudes POST con JSON, validación y respuesta de errores.
- Control de acceso y autorización en servidor, tanto para usuarios autenticados como anónimos.
- Checkpoints de PostgreSQL aislados por identidad y conversación.
- No enviar valores sensibles en query strings o registros de aplicación.
