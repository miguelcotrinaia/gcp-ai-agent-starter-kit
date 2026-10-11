# GCP AI Agent Starter Kit — Agentes de IA con LangChain y LangGraph

Aprende a **construir, integrar y desplegar una aplicación real de IA generativa en Google Cloud**, con un agente conversacional que consulta información mediante **RAG**, mantiene **memoria por conversación** y permite observar sus ejecuciones con **LangSmith**.

Este repositorio es el **punto de entrada de una serie práctica de 13 episodios (00–12)**, más un video de bienvenida. Es una evolución del [taller original](https://youtu.be/n1KShZnmcXM): aquí organizamos los materiales por episodio, actualizamos las prácticas de seguridad y desplegamos **backend y frontends en Google Cloud Run**.

> **¿Qué conocimientos se esperan?** Bases de Python, Git, APIs HTTP, Docker y uso general de Google Cloud. La serie se enfoca en integrar las piezas de la solución, no en enseñar cada tecnología desde cero.

## 🏗️ Arquitectura de la solución

![Arquitectura de componentes del agente de IA en Google Cloud](informacion-complementaria/arquitectura_gcp_para_agente_ia.png)

**Componentes principales:**

| Componente | Tecnología / servicio | Función |
|---|---|---|
| Frontend sin login | Next.js en **Cloud Run** | Chat web sin autenticación de Google; con sesiones anónimas aisladas. |
| Frontend con login | Next.js + Google OAuth en **Cloud Run** | Chat web para usuarios autenticados. |
| API del agente | Python + Flask en **Cloud Run** | Recibe solicitudes y ejecuta el agente. |
| Orquestación de IA | **LangChain + LangGraph** | Herramientas, flujo del agente y manejo del estado. |
| RAG | **Elasticsearch en Compute Engine** | Recuperación de información relevante desde el índice vectorial. |
| Memoria | **Cloud SQL for PostgreSQL** | Persistencia de checkpoints y contexto conversacional. |
| Secretos | **Secret Manager** | Administración de credenciales y configuración sensible. |
| Modelos y embeddings | **OpenAI** | Generación de respuestas y representaciones vectoriales. |
| Observabilidad | **LangSmith** | Trazas y análisis de ejecuciones del agente. |

Los dos frontends son **alternativas independientes**: puedes usar solo uno. Ambos se conectan al mismo backend desplegado en Cloud Run. El acceso al historial debe permanecer aislado y validado en el servidor, tanto para usuarios autenticados como para sesiones anónimas.

## 📚 Repositorios que forman la solución

| Repositorio | Contenido | Episodios |
|---|---|---|
| **[gcp-ai-agent-starter-kit](https://github.com/miguelcotrinaia/gcp-ai-agent-starter-kit)** | Infraestructura, notebooks, agente, API, documentación y servicio de backend para Cloud Run. | 00–09 y 12 |
| **[agentui-withoutlogin](https://github.com/miguelcotrinaia/agentui-withoutlogin)** | Frontend Next.js **sin login**, preparado para integrarse con el agente. | 10 |
| **[agentui-withlogin](https://github.com/miguelcotrinaia/agentui-withlogin)** | Frontend Next.js **con Google Login**, integrado con el agente. | 11 |

Cada frontend mantiene su propio repositorio y código de despliegue. Las carpetas `10-frontend-sin-login/` y `11-frontend-con-login/` de este repositorio contienen las guías de los episodios y los enlaces correspondientes; no duplican los proyectos Next.js.

## 🎬 Episodios de la serie

La **bienvenida** presenta el proyecto, los tres repositorios, la arquitectura final y lo que se construirá. No lleva número de episodio. El contenido se publicará progresivamente y cada carpeta contendrá los recursos necesarios para su video.

| Episodio | Tema | Material |
|:---:|---|---|
| **00** | Arquitectura del agente de IA en Google Cloud | [00-arquitectura-agente-ia-gcp](./00-arquitectura-agente-ia-gcp/) |
| **01** | Preparar Google Cloud para la solución | [01-preparar-google-cloud](./01-preparar-google-cloud/) |
| **02** | Elasticsearch en Compute Engine | [02-elasticsearch-compute-engine](./02-elasticsearch-compute-engine/) |
| **03** | RAG con LangChain y Elasticsearch | [03-rag-langchain-elasticsearch](./03-rag-langchain-elasticsearch/) |
| **04** | Cloud SQL con PostgreSQL | [04-cloud-sql-postgresql](./04-cloud-sql-postgresql/) |
| **05** | Gestión de secretos con Secret Manager | [05-secret-manager](./05-secret-manager/) |
| **06** | Construir un agente con LangGraph y RAG | [06-agente-langgraph-rag](./06-agente-langgraph-rag/) |
| **07** | Memoria con LangGraph y PostgreSQL | [07-memoria-langgraph-postgresql](./07-memoria-langgraph-postgresql/) |
| **08** | Trazabilidad y observabilidad con LangSmith | [08-trazabilidad-langsmith](./08-trazabilidad-langsmith/) |
| **09** | API del agente y despliegue con Docker en Cloud Run | [09-despliegue-docker-cloud-run](./09-despliegue-docker-cloud-run/) |
| **10** | Frontend Next.js sin login en Cloud Run | [10-frontend-sin-login](./10-frontend-sin-login/) |
| **11** | Frontend Next.js con Google Login en Cloud Run | [11-frontend-con-login](./11-frontend-con-login/) |
| **12** | Pruebas, seguridad y costos de la solución | [12-pruebas-seguridad-costos](./12-pruebas-seguridad-costos/) |

> **Nota sobre Flask:** la construcción de la API forma parte del **episodio 09**; no hay un episodio independiente de introducción a Flask. Los enlaces a los videos se incorporarán a medida que se publiquen.

## 🗂️ Organización del repositorio

- **`00-` a `12-`**: material de aprendizaje por episodio (README, notebooks, scripts o documentación cuando corresponda).
- **[`cloud-run-service/`](./cloud-run-service/)**: código del servicio backend que se prepara para desplegar en Cloud Run. Su implementación se irá completando y verificando durante la serie.
- **[`informacion-complementaria/`](./informacion-complementaria/)**: diagramas y recursos compartidos, como la arquitectura mostrada arriba.
- **[`version-anterior-1.0/`](./version-anterior-1.0/)**: material conservado del taller original, separado de la versión nueva.

## 🚀 Cómo seguir el proyecto

1. **Clona el repositorio principal:** `git clone https://github.com/miguelcotrinaia/gcp-ai-agent-starter-kit.git`.
2. **Empieza por el episodio 00** para comprender los componentes y el flujo de la aplicación; continúa en el orden de la tabla.
3. **Consulta el README de cada episodio** para conocer requisitos, archivos, instrucciones de ejecución y recursos asociados.
4. **Configura credenciales mediante mecanismos seguros** del entorno correspondiente; no las escribas en notebooks ni las subas a Git.
5. **Elige el frontend** sin login o con Google Login y continúa en su repositorio al llegar al episodio 10 u 11.

### Seguridad y costos

Esta solución usa recursos de GCP y servicios externos que **pueden generar cargos**, incluso durante pruebas. Configura presupuestos y alertas de facturación, revisa permisos IAM, restringe el acceso a los servicios y elimina recursos que ya no utilices. Las credenciales deben gestionarse fuera del código fuente, por ejemplo mediante Secret Manager. No compartas contraseñas, tokens ni archivos `.env`.

## 🕘 Versión anterior del taller (1.0)

La carpeta **[`version-anterior-1.0/`](./version-anterior-1.0/)** conserva los materiales del taller inicial: notebook del agente, carga de datos en Elasticsearch, catálogo CSV, presentación, diagrama y código de despliegue original.

El taller inicial utilizaba una arquitectura con **backend en Cloud Run** y **frontend en Vercel**. En esta nueva serie, los **tres servicios de aplicación se desplegarán en Cloud Run**.

📺 [Ver el taller original completo en YouTube](https://youtu.be/n1KShZnmcXM)

## 💬 Comunidad y contribuciones

La idea es aprender, compartir experiencias y construir agentes de IA en comunidad.

- **[Unirme al grupo de WhatsApp](https://chat.whatsapp.com/IuQp9F3ZZNC0qbcYcITiNp)**
- **[Reportar problemas o sugerir mejoras](https://github.com/miguelcotrinaia/gcp-ai-agent-starter-kit/issues)** mediante GitHub Issues.
- **Contribuir:** abre un Pull Request en el repositorio correspondiente e indica el episodio o componente al que se refiere el cambio.

Si el contenido te resulta útil, puedes apoyar el proyecto dejando una ⭐ en los repositorios y compartiendo la serie.

## 🤝 Conecta conmigo

Soy **Miguel Ángel Cotrina Espinoza**. Comparto recursos y proyectos de inteligencia artificial, agentes y datos.

- **LinkedIn:** [Miguel Cotrina](https://www.linkedin.com/in/miguelcotrinaia/)
- **YouTube:** [Taller GenAI: crea tu primera aplicación](https://www.youtube.com/@miguelcotrinaia)
- **GitHub:** [miguelcotrinaia](https://github.com/miguelcotrinaia)

**IA & Data con propósito.**
