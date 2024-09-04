import json
import os

from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import JsonOutputParser

# from langchain_community.embeddings import OpenAIEmbeddings
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

from prompts.prompts import human_prompt, system_prompt
from utils.loaders import read_file_as_text

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()


def load_vector_databases(db_folder="vector_db"):
    embeddings = OpenAIEmbeddings()
    entity_db = FAISS.load_local(
        f"{db_folder}/entity_db", embeddings, allow_dangerous_deserialization=True
    )
    attribute_db = FAISS.load_local(
        f"{db_folder}/attribute_db", embeddings, allow_dangerous_deserialization=True
    )
    return entity_db, attribute_db


def replace_entities_and_attributes(result_dict, entity_db, attribute_db):
    if isinstance(result_dict, dict):
        new_dict = {}
        for key, value in result_dict.items():
            # Substituir o nome da entidade
            closest_entity = entity_db.similarity_search(key, k=1)[0].page_content

            if isinstance(value, dict):
                # Substituir os nomes dos atributos
                new_value = {}
                for sub_key, sub_value in value.items():
                    closest_attribute = attribute_db.similarity_search(sub_key, k=1)[
                        0
                    ].page_content
                    new_value[closest_attribute] = replace_entities_and_attributes(
                        sub_value, entity_db, attribute_db
                    )
                new_dict[closest_entity] = new_value
            elif isinstance(value, list):
                new_dict[closest_entity] = [
                    replace_entities_and_attributes(item, entity_db, attribute_db)
                    for item in value
                ]
            else:
                new_dict[closest_entity] = value
        return new_dict
    elif isinstance(result_dict, list):
        return [
            replace_entities_and_attributes(item, entity_db, attribute_db)
            for item in result_dict
        ]
    else:
        return result_dict


def main():
    # Carrega as variáveis de ambiente do arquivo .env
    load_dotenv()

    # Inicializa o modelo de linguagem ChatOpenAI com a versão e temperatura desejada
    base_model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    #################### CAMINHO DO ARQUIVO DE ENTRADA (ALTERE O CAMINHO AQUI) ####################
    input_file_path = "./data/dados_html1.htm"
    # input_file_path = "./data/dados_html2.htm"
    # input_file_path = "./data/dados_json.json"
    # input_file_path = "./data/dados_xml.xml"
    # input_file_path = "./data/dados_csv.csv"
    ###############################################################################################

    # Lê o conteúdo do arquivo HTML como texto
    input_content = read_file_as_text(input_file_path)

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

    # Carrega os vector databases salvos
    entity_db, attribute_db = load_vector_databases()

    # Substitui as entidades e atributos no resultado com base nos vector databases
    final_result_dict = replace_entities_and_attributes(
        result_dict, entity_db, attribute_db
    )

    # Gera o nome do arquivo de saída com base no nome do arquivo de entrada
    output_file_name = (
        os.path.splitext(os.path.basename(input_file_path))[0] + "_output.json"
    )
    output_file_path = os.path.join("./output", output_file_name)

    # Salva o resultado extraído em um arquivo JSON de saída
    with open(output_file_path, "w", encoding="utf-8") as f:
        json.dump(final_result_dict, f, ensure_ascii=False, indent=4)

    print(f"Resultado salvo em '{output_file_path}'")


if __name__ == "__main__":
    main()
