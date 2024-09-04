import csv
import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

def create_and_save_vector_database(
    dictionary_path="dicionario.csv", db_folder="vector_db"
):
    entity_names = []
    attribute_names = []
    with open(dictionary_path, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) < 2 or not row[0].strip() or not row[1].strip():
                continue  # Pula linhas que não têm duas colunas ou que estão vazias
            entity_names.append(row[0])  # Nome da entidade
            attribute_names.append(row[1])  # Nome do atributo

    embeddings = OpenAIEmbeddings()  # Escolha o modelo de embeddings adequado

    # Criar os vector databases
    entity_db = FAISS.from_texts(texts=entity_names, embedding=embeddings)
    attribute_db = FAISS.from_texts(texts=attribute_names, embedding=embeddings)

    # Criar a pasta para salvar os bancos de dados, se não existir
    os.makedirs(db_folder, exist_ok=True)

    # Salvar os bancos de dados vetoriais em arquivos separados
    entity_db.save_local(f"{db_folder}/entity_db")
    attribute_db.save_local(f"{db_folder}/attribute_db")

    print(f"Bancos de dados vetoriais salvos em {db_folder}")

if __name__ == "__main__":
    create_and_save_vector_database()

# Função para carregar os bancos de dados (para uso futuro)
def load_vector_databases(db_folder="vector_db"):
    embeddings = OpenAIEmbeddings()
    entity_db = FAISS.load_local(f"{db_folder}/entity_db", embeddings)
    attribute_db = FAISS.load_local(f"{db_folder}/attribute_db", embeddings)
    return entity_db, attribute_db