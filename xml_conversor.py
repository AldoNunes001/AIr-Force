import json

from dotenv import load_dotenv
from langchain.output_parsers.openai_functions import JsonOutputFunctionsParser
from langchain.prompts import ChatPromptTemplate
from langchain_core.utils.function_calling import convert_to_openai_function
from langchain_openai import ChatOpenAI

from schema.xml_schema import RootXML
from utils.loaders import read_file_as_text

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Inicializa o modelo de linguagem ChatOpenAI com a versão e temperatura desejada
base_model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# Lê o conteúdo do arquivo HTML como texto
xml_input_content = read_file_as_text("./data/dados_json.xml")

# Define o template do prompt com as mensagens do sistema e do usuário
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Extract the relevant information, if not explicitly provided do not guess.",
        ),
        ("human", "{input}"),
    ]
)

# Converte o esquema RootXML em uma função utilizável pelo OpenAI
xml_extract_function = [convert_to_openai_function(RootXML)]

# Liga o modelo base com as funções de extração, configurando para chamar a função "RootXML"
xml_extract_model = base_model.bind(
    functions=xml_extract_function, function_call={"name": "RootXML"}
)

# Cria a cadeia de extração que inclui o prompt, o modelo de extração e o parser de funções xml
xml_extract_chain = prompt | xml_extract_model | JsonOutputFunctionsParser()

# Invoca a cadeia de extração com o conteúdo do xml como input
result = xml_extract_chain.invoke({"input": xml_input_content})

# Extrai o resultado do xml gerado, utilizando a chave "root_xml"
result_dict = result.get("root_xml", result)

# Salva o resultado extraído em um arquivo xml de saída
with open("./output/xml_output.json", "w", encoding="utf-8") as f:
    json.dump(result_dict, f, ensure_ascii=False, indent=4)

print("Resultado salvo em './output/xml_output.json'")
