# Desafio de Mapeamento de Dados - Solução Automatizada

## Visão Geral
Este projeto visa resolver o desafio de transformar inputs de dados em diversos formatos (XML, JSON, CSV, HTML, etc.) em um modelo JSON padronizado. Dada a complexidade e a variabilidade desses formatos, uma abordagem tradicional baseada em regras se mostraria insuficiente para lidar com as ambiguidades e a estrutura hierárquica dos dados.

## Solução Proposta
Nossa solução adota uma abordagem inovadora utilizando "Large Language Models"(LLMs) para identificar e extrair informações importantes dos dados de entrada, transformando-os em um JSON estruturado. Esta metodologia permite a extração inteligente de informações, lidando eficazmente com diferentes níveis de ambiguidade e complexidade dos formatos de entrada.

### Componentes da Solução
A solução é centrada em um LLM que executa a seguinte tarefa principal:
1. **Identificação e Extração de Entidades:** O LLM analisa o conteúdo dos dados de entrada, independentemente do formato (HTML, CSV, JSON, etc.), para identificar entidades e campos importantes e extrair suas informações, estruturando as entidades identificadas em um formato JSON padronizado, sendo capaz de aninhar entidades ou atributos dentro de outros quando contextualmente fizer sentido.

### Principais Benefícios da Abordagem
1. **Flexibilidade e Escalabilidade:** A utilização de LLMs permite que a solução se adapte a uma vasta gama de formatos de entrada, sem necessidade de ajustes manuais para cada novo tipo de dado.
2. **Organização e Conformidade:** A estrutura de saída em JSON é padronizada e pode incluir relações complexas entre entidades, com validação incorporada para garantir que todos os dados relevantes sejam capturados corretamente.
3. **Simplicidade na Implementação e Manutenção:** A abordagem centralizada em LLM permite uma implementação mais simples, com manutenção facilitada e escalabilidade para futuros aprimoramentos.

### Exemplo de Funcionamento
Ao receber uma entrada, o LLM gera uma saída JSON estruturada. Por exemplo, para um dado em HTML contendo uma tabela de produtos, a saída poderia ser:
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

## Como testar
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

### 2. **Preparar o Arquivo de Entrada**
Coloque o arquivo de entrada que deseja processar na pasta `data` do projeto.

### 3. **Configurar o Caminho do Arquivo de Entrada**
Abra o arquivo `zExtractor.py` e defina a variável `input_file_path` com o caminho do arquivo de entrada. O caminho deve apontar para o arquivo dentro da pasta `data`. Por exemplo:

```python
input_file_path = "data/seu_arquivo_de_entrada.ext"
```

### 4. **Executar o Código**
Com as dependências instaladas e o caminho do arquivo de entrada configurado, execute o código rodando o seguinte comando:

```python
python zExtractor.py
```

### 5. **Verificar o Resultado**
O resultado será gerado na pasta `output`. O nome do arquivo de saída será o mesmo nome do arquivo de entrada, com o sufixo `_output.json`. Por exemplo, se o arquivo de entrada se chamar `seu_arquivo_de_entrada.ext`, o resultado estará em `output/seu_arquivo_de_entrada_output.json`.

## Integrantes da Equipe
1. Aldo Nunes - https://github.com/AldoNunes001
2. Daniel Correia - https://github.com/dancorreia-swe
3. Iago Maurício - https://github.com/iagomauricioo
