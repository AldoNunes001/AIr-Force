# Desafio de Mapeamento de Dados - Solução Automatizada

## Visão Geral
Este projeto visa resolver o desafio de transformar inputs de dados em diversos formatos (XML, JSON, CSV, HTML) em um modelo JSON padronizado. Dada a complexidade e a variabilidade desses formatos, uma abordagem tradicional baseada em regras se mostraria insuficiente para lidar com as ambiguidades e a estrutura hierárquica dos dados.

## Solução Proposta
Nossa solução adota uma abordagem inovadora utilizando Modelos de Linguagem de Grande Escala (LLMs) para interpretar e transformar dados não estruturados em dados estruturados. Esta metodologia permite a extração inteligente de informações, lidando eficazmente com diferentes níveis de ambiguidade e complexidade dos formatos de entrada.

### Componentes da Solução
A ideia inicial consiste em utilizar mais de um agente baseado em LLMs para a realização da tarefa, existindo, no mínimo:
1. **Agente de Conversão:** responsável por processar os inputs de dados, independentemente do formato, convertendo-os em um modelo JSON estruturado.
2. **Agente de Verificação:** responsável por, após a conversão, verificar o formato e a conformidade do output JSON, assegurando que todas as informações relevantes foram corretamente mapeadas e que o modelo JSON segue a estrutura padronizada esperada.
3. **Agente de Gerenciamento:** responsável por gerenciar as atividades dos demais agentes, funcionando também como estrutura de contigência, garantindo que o processo funcione, eventualmente, de forma iterativa, até que o objetivo seja satisfatoriamente alcançado.

### Principais Benefícios da Abordagem
1. **Flexibilidade e Escalabilidade:** A utilização de LLMs permite que a solução se adapte a uma vasta gama de formatos de entrada, sem necessidade de ajustes manuais para cada novo tipo de dado.
2. **Precisão e Conformidade:** A combinação de agentes de conversão e verificação assegura que os dados de saída estejam sempre em conformidade com o modelo JSON padronizado.
3. **Manutenção Simples:** Com a modularidade da solução, cada componente pode ser atualizado ou melhorado de forma independente, facilitando a manutenção e evolução do sistema.

## Integrantes da Equipe
1. Aldo Nunes - https://github.com/AldoNunes001
2. Daniel Correia - https://github.com/dancorreia-swe
3. Iago Maurício - https://github.com/iagomauricioo
