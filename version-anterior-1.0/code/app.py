from langchain_openai import ChatOpenAI
import os
from flask import Flask, jsonify, request
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage
from langchain_openai import OpenAIEmbeddings
from langchain_elasticsearch import ElasticsearchStore
from psycopg_pool import ConnectionPool
from langgraph.checkpoint.postgres import PostgresSaver
from langgraph.prebuilt import create_react_agent


## datos de trazabilidad
os.environ["LANGSMITH_ENDPOINT"]="https://api.smith.langchain.com"
os.environ["LANGCHAIN_API_KEY"] = "lsv2_pt...."
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "gcpaiagent"
os.environ["OPENAI_API_KEY"] ="sk-proj....."


app = Flask(__name__)

@app.route('/agent', methods=['GET'])
def main():
    #Capturamos variables enviadas
    id_agente = request.args.get('idagente')
    msg = request.args.get('msg')
    #datos de configuracion
    DB_URI = os.environ.get(
        "DB_URI",
        "postgresql://usuario:password@0.0.0.0:5432/basededatos?sslmode=disable"
    )
    connection_kwargs = {
        "autocommit": True,
        "prepare_threshold": 0,
    }
    db_query = ElasticsearchStore(
        es_url="http://0.0.0.0:9200",
        es_user="elastic",
        es_password="clave",
        index_name="lg-proddata",
        embedding=OpenAIEmbeddings())

    # Herramienta RAG
    retriever = db_query.as_retriever()
    tool_rag = retriever.as_tool(
        name="busqueda_productos",
        description="Consulta en la informacion de computadoras, y articulos de computo",
    )
    # Inicializamos la memoria
    with ConnectionPool(
            # Example configuration
            conninfo=DB_URI,
            max_size=20,
            kwargs=connection_kwargs,
    ) as pool:
        checkpointer = PostgresSaver(pool)

        # Inicializamos el modelo
        model = ChatOpenAI(model="gpt-4.1-2025-04-14")

        # Agrupamos las herramientas
        tolkit = [tool_rag]

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system",
                 """
                 Eres un asistente gentil de ventas de computadoras especializado.
                 Utiliza únicamente las herramientas disponibles para responder y brindar infromacion.
                 Si no cuentas con una herramienta específica para resolver una pregunta, infórmalo claramente e indica como pueded ayudar.
 
                 Tu objetivo es guiar al cliente de forma amigable, breve y conversacional, como si fueras un amigo experto en tecnología. Sigue estos pasos:
 
                 1. Saluda y pregunta: Da un saludo cálido, pregunta qué busca el cliente y si tiene una idea clara de lo que necesita (ej. laptop para gaming, PC de oficina, accesorios). Si no sabe, sugiere 2-3 opciones populares, priorizando productos con más stock.
                 2. Consulta productos: Usa la información de productos segun su necesidad para responder con detalles de productos relevantes (nombre, descripción, precio, stock). Destaca los que tienen mayor disponibilidad.
                 3. Envío o tienda: Pregunta si prefiere recoger en tienda o entrega a domicilio (costo adicional de S/20 para compras menores a S/500; gratis si supera S/500). Si no alcanza los S/50, sugiere añadir algo  para obtener envío gratis o confirma si ya lo logró.
                 4. Confirmar pedido: Resume el pedido y pregunta si quiere añadir algo más.
                 5. Método de pago:
                   - Si elige tienda, pregunta si pagará en efectivo o por transferencia. Solicita su nombre y apellido para generar un código de pedido (formato: AAAAMMDD_HHMMSS_NombreApellido, ej. 20250414_153022_JuanPerez).
                   - Si elige domicilio, pide una dirección completa y confirma que el pago será por transferencia.
                 6. Cierre de compra:
                   - Para transferencias, proporciona el número de cuenta 12730317292820 en BankaNet y pide confirmar el pago.
                   - Para pago en tienda, entrega el código de pedido.
                 7. Estilo: Sé breve, usa un tono entusiasta y natural. Evita tecnicismos a menos que el cliente los mencione. Responde solo lo necesario para avanzar la conversación.
 
                 """),
                ("human", "{messages}"),
            ]
        )
        # inicializamos el agente
        agent_executor = create_react_agent(model, tolkit, checkpointer=checkpointer, prompt=prompt)
        # ejecutamos el agente
        config = {"configurable": {"thread_id": id_agente}}
        response = agent_executor.invoke({"messages": [HumanMessage(content=msg)]}, config=config)
        return response['messages'][-1].content


if __name__ == '__main__':
    # La aplicación escucha en el puerto 8080, requerido por Cloud Run
    app.run(host='0.0.0.0', port=8080)