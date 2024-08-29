import json

from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI

from prompts.prompts import human_prompt, system_prompt
from utils.loaders import read_file_as_text

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Inicializa o modelo de linguagem ChatOpenAI com a versão e temperatura desejada
base_model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# Lê o conteúdo do arquivo HTML como texto
input_content = read_file_as_text("./data/input_dados.xml")

# Define o template do prompt com as mensagens do sistema e do usuário
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", human_prompt),
    ]
)

# Cria a cadeia de extração que inclui o prompt, o modelo de extração e o parser JSON
extract_chain = prompt | base_model | JsonOutputParser()

# Invoca a cadeia de extração com o conteúdo do arquivo como input
result = extract_chain.invoke({"input": input_content})

# Extrai o resultado do JSON gerado, utilizando a chave "sinapses.Page"
result_dict = result.get("sinapses.Page", result)

# Salva o resultado extraído em um arquivo JSON de saída
with open("./output/zzzzzzz_output.json", "w", encoding="utf-8") as f:
    json.dump(result_dict, f, ensure_ascii=False, indent=4)

print("Resultado salvo em './output/zzzzzzzz_output.json'")
