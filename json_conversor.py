import json

from dotenv import load_dotenv
from langchain.output_parsers.openai_functions import JsonOutputFunctionsParser
from langchain.prompts import ChatPromptTemplate
from langchain_core.utils.function_calling import convert_to_openai_function
from langchain_openai import ChatOpenAI

from schema.json_schema import RootJSON
from utils.loaders import read_file_as_text

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Inicializa o modelo de linguagem ChatOpenAI com a versão e temperatura desejada
base_model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# Lê o conteúdo do arquivo HTML como texto
json_input_content = read_file_as_text("./data/dados_json.json")

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

# Converte o esquema RootJSON em uma função utilizável pelo OpenAI
json_extract_function = [convert_to_openai_function(RootJSON)]

# Liga o modelo base com as funções de extração, configurando para chamar a função "RootJSON"
json_extract_model = base_model.bind(
    functions=json_extract_function, function_call={"name": "RootJSON"}
)

# Cria a cadeia de extração que inclui o prompt, o modelo de extração e o parser de funções JSON
json_extract_chain = prompt | json_extract_model | JsonOutputFunctionsParser()

# Invoca a cadeia de extração com o conteúdo do json como input
result = json_extract_chain.invoke({"input": json_input_content})

# Extrai o resultado do JSON gerado, utilizando a chave "root_json"
result_dict = result.get("root_json", result)

# Salva o resultado extraído em um arquivo JSON de saída
with open("./output/json_output.json", "w", encoding="utf-8") as f:
    json.dump(result_dict, f, ensure_ascii=False, indent=4)

print("Resultado salvo em './output/json_output.json'")
