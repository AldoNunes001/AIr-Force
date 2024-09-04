<h1 align="center">Desafio TechBiz - Mapeamento de Dados</h1>

###

<div align="center">
  <img height="200" src="https://image.slidesharecdn.com/institucionaltechbizforensedigital-100701092914-phpapp02/85/institucional-techbiz-forense-digital-1-320.jpg?cb=1670119558"  />
</div>
<div align="center">
  <img height="100" src="https://github.com/user-attachments/assets/f428608e-3af5-4ca2-b9a9-93ca130472a6"  />
</div>
  



<div align="center">
  <img height="100" src="https://github.com/user-attachments/assets/bb8d4ffb-df43-4643-8f96-386d841c5548"  />
</div>

<h2 align="left">Equipe AIr-Force 🤖</h2>

###

- Aldo Nunes - https://github.com/AldoNunes001
- Daniel Correia - https://github.com/dancorreia-swe
- Iago Maurício - https://github.com/iagomauricioo

###



## Visão Geral
Este projeto visa resolver o desafio de transformar inputs de dados em diversos formatos (XML, JSON, CSV, HTML, etc.) em um modelo JSON padronizado. Dada a complexidade e a variabilidade desses formatos, uma abordagem tradicional baseada em regras se mostraria insuficiente para lidar com as ambiguidades e a estrutura hierárquica dos dados.

## Solução Proposta
Nossa solução adota uma abordagem inovadora utilizando "Large Language Models"(LLMs) para identificar e extrair informações importantes dos dados de entrada, transformando-os em um JSON estruturado. Esta metodologia permite a extração inteligente de informações, lidando eficazmente com diferentes níveis de ambiguidade e complexidade dos formatos de entrada.

## Fluxograma da Solução
<div align="center">
  <img height="auto" src="https://github.com/user-attachments/assets/ac6537eb-db3f-4ac9-a8ae-a7556daae2f3"  />
</div>

### Componentes da Solução
A solução é centrada em um algoritmo que executa as seguintes tarefas principais:
1. **Identificação e Extração de Entidades:** O LLM analisa o conteúdo dos dados de entrada, independentemente do formato (HTML, CSV, JSON, etc.), para identificar entidades e campos importantes e extrair suas informações, estruturando as entidades identificadas em um formato JSON estruturado, sendo capaz de aninhar entidades ou atributos dentro de outros quando contextualmente fizer sentido.
2. **Padronização de Nomes (Busca Vetorial):** Após a extração dos dados, a solução realiza uma busca por similaridade em um banco de dados vetorial. Esse banco contém os nomes corretos de entidades e atributos, garantindo que a saída JSON gerada pelo LLM seja padronizada conforme os termos corretos encontrados no banco. Com base nos resultados da busca vetorial, os nomes das entidades e atributos extraídos pelo LLM são substituídos pelos nomes corretos, resultando em um JSON final padronizado e em conformidade com o banco de dados de referência.

### Principais Benefícios da Abordagem
1. **Flexibilidade e Escalabilidade:** A utilização de LLMs permite que a solução se adapte a uma vasta gama de formatos de entrada, sem necessidade de ajustes manuais para cada novo tipo de dado.
2. **Organização e Conformidade:** A estrutura de saída em JSON é padronizada e pode incluir relações complexas entre entidades, com validação incorporada para garantir que todos os dados relevantes sejam capturados corretamente.
3. **Simplicidade na Implementação e Manutenção:** A abordagem centralizada em LLM permite uma implementação mais simples, com manutenção facilitada e escalabilidade para futuros aprimoramentos.

### Exemplo de Funcionamento
Ao receber uma entrada, o algoritmo gera uma saída JSON estruturada. Por exemplo, para um dado em XML contendo uma lista de produtos, a saída poderia ser:
<h4 align="left">Exemplo de entrada de dados não tratados</h4>

```xml
<Products>
    <ID>123</ID>
    <Name>Product X</Name>
    <Price>100.0</Price>
    <LastUpdated>2023-09-01T12:00:00</LastUpdated>
    <ReviewedBy>John Doe</ReviewedBy>
    <InternalCode>PX100</InternalCode>
    <WarehouseLocation>Shelf A3</WarehouseLocation>
    <Notes>N/A</Notes>
</Products>
<Products>
    <ID>456</ID>
    <Price>150.0</Price>
    <Name>Product Y</Name>
    <LastUpdated>2023-09-01T12:00:00</LastUpdated>
    <ReviewedBy>Jane Doe</ReviewedBy>
    <InternalCode>PY150</InternalCode>
    <WarehouseLocation>Shelf B5</WarehouseLocation>
    <Notes>Special Handling Required</Notes>
</Products>
```



<h4 align="left">Exemplo de JSON padronizado</h4>

```json
{
    "sinapses.Products": [
        {
            "sinapses.Name": "Product X",
            "sinapses.Price": 100.0
        },
        {
            "sinapses.Name": "Product Y",
            "sinapses.Price": 150.0
        }
    ]
}
```

## Como testar (Versão Estável - SEM Banco de Dados) ✅
Para testar o código, siga as etapas abaixo:

### 1. **Instalação de Dependências**
Este projeto usa Python e as dependências são gerenciadas com o Poetry. Você pode instalar as dependências de duas maneiras:

#### Usando Poetry
Se você já tem o Poetry instalado, basta rodar o comando abaixo no diretório do projeto para instalar todas as dependências:

```bash
poetry install
```

#### Usando pip e requirements.txt
Se você preferir usar pip, pode instalar as dependências diretamente a partir do arquivo requirements.txt:

```bash
pip install -r requirements.txt
```

### 2. **Configurando Arquivo `.env`**
Crie um arquivo `.env`na raiz do projeto e adicione sua OpenAI API Key. Exemplo:

```bash
OPENAI_API_KEY=sk-WmwqA1Gn6e3yLISvDcINqbf66zHtVZZvIwXXmjfF5ETlNoE2ftpor
```

### 3. **Preparar o Arquivo de Entrada**
Coloque o arquivo de entrada que deseja processar na pasta `data` do projeto.

### 4. **Configurar o Caminho do Arquivo de Entrada**
Abra o arquivo `zExtractor.py` e defina a variável `input_file_path` com o caminho do arquivo de entrada. O caminho deve apontar para o arquivo dentro da pasta `data`. Por exemplo:

```python
input_file_path = "data/seu_arquivo_de_entrada.ext"
```

### 5. **Executar o Código**
Com as dependências instaladas e o caminho do arquivo de entrada configurado, execute o código rodando o seguinte comando:

```python
python zExtractor.py
```

### 6. **Verificar o Resultado**
O resultado será gerado na pasta `output`. O nome do arquivo de saída será o mesmo nome do arquivo de entrada, com o sufixo `_output.json`. Por exemplo, se o arquivo de entrada se chamar `seu_arquivo_de_entrada.ext`, o resultado estará em `output/seu_arquivo_de_entrada_output.json`.

<br>

## Como testar (Versão Inacabada - COM Banco de Dados) 🚧
Esta versão está inacabada, com funcionalidades para implementar e bugs para resolver.
Para testar o código, siga as etapas abaixo:

### 1. **Instalação de Dependências**
Este projeto usa Python e as dependências são gerenciadas com o Poetry. Você pode instalar as dependências de duas maneiras:

#### Usando Poetry
Se você já tem o Poetry instalado, basta rodar o comando abaixo no diretório do projeto para instalar todas as dependências:

```bash
poetry install
```

#### Usando pip e requirements.txt
Se você preferir usar pip, pode instalar as dependências diretamente a partir do arquivo requirements.txt:

```bash
pip install -r requirements.txt
```

### 2. **Configurando Arquivo `.env`**
Crie um arquivo `.env`na raiz do projeto e adicione sua OpenAI API Key. Exemplo:

```bash
OPENAI_API_KEY=sk-WmwqA1Gn6e3yLISvDcINqbf66zHtVZZvIwXXmjfF5ETlNoE2ftpor
```

### 3. **Criar o Banco de Dados (se necessário)**
Antes de executar o código, verifique se o banco de dados vetorial já existe. Caso contrário, você pode criá-lo rodando o script `criar_banco.py`:

```bash
python criar_banco.py
```

### 4. **Preparar o Arquivo de Entrada**
Coloque o arquivo de entrada que deseja processar na pasta `data` do projeto.

### 5. **Configurar o Caminho do Arquivo de Entrada**
Abra o arquivo `zExtractor_DB.py` e defina a variável `input_file_path` com o caminho do arquivo de entrada. O caminho deve apontar para o arquivo dentro da pasta `data`. Por exemplo:

```python
input_file_path = "data/seu_arquivo_de_entrada.ext"
```

### 6. **Executar o Código**
Com as dependências instaladas e o caminho do arquivo de entrada configurado, execute o código rodando o seguinte comando:

```python
python zExtractor_DB.py
```

### 6. **Verificar o Resultado**
O resultado será gerado na pasta `output`. O nome do arquivo de saída será o mesmo nome do arquivo de entrada, com o sufixo `_output.json`. Por exemplo, se o arquivo de entrada se chamar `seu_arquivo_de_entrada.ext`, o resultado estará em `output/seu_arquivo_de_entrada_output.json`.

## Contato
- aldonunes001@gmail.com
