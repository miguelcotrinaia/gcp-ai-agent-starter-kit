# Agentes de IA con LangChain, LangGraph y Google Cloud

Repositorio principal de la serie educativa para construir y desplegar una aplicación conversacional de IA con **RAG**, **memoria de conversaciones**, **trazabilidad** y una interfaz web. Es una evolución del taller anterior, no un curso de programación desde cero.

## Arquitectura objetivo

- **Backend del agente:** Flask, LangChain y LangGraph en **Cloud Run**.
- **Conocimiento RAG:** Elasticsearch en **Compute Engine**.
- **Checkpoints de memoria:** PostgreSQL en **Cloud SQL**.
- **Secretos:** Google Secret Manager; accesos mediante IAM.
- **Observabilidad:** LangSmith.
- **Frontend:** Next.js en **Cloud Run** en dos variantes independientes, una sin login y otra con Google Login.

La solución puede utilizar **uno u otro frontend**: no es obligatorio desplegar los dos a la vez.

## Repositorios de esta solución

| Componente | Repositorio | Episodio |
|---|---|---|
| Backend, notebooks, infraestructura y documentación central | [gcp-ai-agent-starter-kit](https://github.com/miguelcotrinaia/gcp-ai-agent-starter-kit) | 00–09 y 12 |
| Next.js sin login | [agentui-withoutlogin](https://github.com/miguelcotrinaia/agentui-withoutlogin) | 10 |
| Next.js con Google Login | [agentui-withlogin](https://github.com/miguelcotrinaia/agentui-withlogin) | 11 |

## Playlist y ruta de aprendizaje

**Bienvenida:** video de presentación de la playlist, sin número de episodio. La serie se irá publicando progresivamente; la numeración indica el orden recomendado para aprender, no el orden en que se grabarán o publicarán los videos.

| Episodio | Tema | Material | Estado |
|---|---|---|---|
| [00](./00-arquitectura-agente-ia-gcp/README.md) | Arquitectura del agente de IA en Google Cloud | Repositorio principal | En preparación |
| [01](./01-preparar-google-cloud/README.md) | Preparar Google Cloud para el proyecto | Repositorio principal | En preparación |
| [02](./02-elasticsearch-compute-engine/README.md) | Elasticsearch en Compute Engine | Repositorio principal | En preparación |
| [03](./03-rag-langchain-elasticsearch/README.md) | RAG con LangChain y Elasticsearch | Repositorio principal | En preparación |
| [04](./04-cloud-sql-postgresql/README.md) | PostgreSQL en Cloud SQL | Repositorio principal | En preparación |
| [05](./05-secret-manager/README.md) | Secret Manager para el agente de IA | Repositorio principal | En preparación |
| [06](./06-agente-langgraph-rag/README.md) | Agente con LangGraph y RAG | Repositorio principal | En preparación |
| [07](./07-memoria-langgraph-postgresql/README.md) | Memoria de LangGraph con PostgreSQL | Repositorio principal | En preparación |
| [08](./08-trazabilidad-langsmith/README.md) | Trazabilidad con LangSmith | Repositorio principal | En preparación |
| [09](./09-despliegue-docker-cloud-run/README.md) | API Flask, Docker y Cloud Run | Repositorio principal | En preparación |
| [10](./10-frontend-sin-login/README.md) | Frontend Next.js sin login | Frontend externo | En preparación |
| [11](./11-frontend-con-login/README.md) | Frontend Next.js con Google Login | Frontend externo | En preparación |
| [12](./12-pruebas-seguridad-costos/README.md) | Pruebas, seguridad y costos | Repositorio principal | En preparación |

El **episodio 09** incluye la adaptación de la lógica del agente a una **API Flask** y su despliegue mediante **Docker en Cloud Run**; no hay un tutorial independiente de Flask desde cero.

## ¿Dónde está el código desplegable?

- [`cloud-run-service/`](./cloud-run-service/) — código final del backend cuando se complete y valide con los archivos de despliegue del autor.
- [`09-despliegue-docker-cloud-run/`](./09-despliegue-docker-cloud-run/) — guía educativa del episodio y comprobaciones.
- [`10-frontend-sin-login/`](./10-frontend-sin-login/) y [`11-frontend-con-login/`](./11-frontend-con-login/) — guías y enlaces a los repositorios del frontend, sin duplicar su código.

## Conocimientos recomendados

Se asumen bases de Python, HTTP/REST, Git, Docker y uso básico de Google Cloud. Cada episodio indica lo mínimo que necesita; no repetiremos un curso introductorio de estas tecnologías.

## Seguridad y costos

No se publicarán claves o contraseñas, ni código que dependa de valores de ejemplo embebidos. Se utilizarán mecanismos de secretos apropiados para Colab, entornos locales y Google Cloud, junto con validación de identidad y aislamiento de conversaciones. Las máquinas virtuales, bases de datos, Cloud Run y las llamadas a modelos pueden generar costos; revisa presupuestos y apaga los recursos de prueba que no uses.

## Taller anterior (versión 1.0)

La carpeta [`version-anterior-1.0/`](./version-anterior-1.0/) conservará el material histórico una vez saneadas posibles credenciales y salidas de notebooks. La arquitectura del taller anterior usaba Vercel para el frontend. [Video original del taller](https://youtu.be/n1KShZnmcXM).

## Comunidad

Se agradecen reportes de problemas y contribuciones mediante issues y pull requests a cada repositorio, indicando el episodio afectado.
