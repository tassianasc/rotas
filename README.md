# 🚚 Sistema de Otimização de Rotas Logísticas

Este projeto é uma aplicação interativa desenvolvida em Python para simular e otimizar rotas de entrega logística. Ele utiliza **Teoria dos Grafos** para calcular o caminho de menor custo (tempo) entre um armazém e um ponto de entrega, permitindo também a simulação de incidentes (bloqueio de estradas) em tempo real.

Projeto desenvolvido para a disciplina de **Análise e Complexidade de Algoritmos**.

## ✨ Funcionalidades

* **Seleção Dinâmica:** Escolha qualquer cidade como Armazém (Origem) ou Cliente (Destino).
* **Cálculo de Caminho Mínimo:** Algoritmo personalizado para encontrar a rota mais rápida.
* **Simulação de Incidentes:** Interface para "interditar" estradas e forçar o recálculo da rota (Análise de Robustez).
* **Visualização Gráfica:** Mapa interativo que destaca a rota, mostra os custos e diferencia origem/destino por cores.

## 🛠 Tecnologias Utilizadas

* **Python 3.x**
* **Streamlit:** Para a interface web interativa.
* **NetworkX:** Para modelagem do grafo e algoritmos de caminho.
* **Matplotlib:** Para renderização visual do grafo.

---

## 🚀 Como Rodar o Projeto (Passo a Passo)

Siga as instruções abaixo para executar o projeto na sua máquina.

### 1. Pré-requisitos

Certifique-se de ter o **Python** instalado. Recomendamos também o uso de um editor de código como o **VS Code**.

### 2. Configuração do Ambiente

Abra o terminal na pasta do projeto e siga os passos para criar um ambiente virtual (isso evita conflitos com outras bibliotecas do seu computador).

#### No Windows:
```bash
# Cria o ambiente virtual
python -m venv venv

# Ativa o ambiente
.\venv\Scripts\activate

# No Mac/Linux:

# Cria o ambiente virtual
python3 -m venv venv

# Ativa o ambiente
source venv/bin/activate

```

### 3. Garanta que seu arquivo `requirements.txt` tenha este conteúdo:

Crie (ou verifique) um arquivo chamado **`requirements.txt`** na raiz do projeto e cole o seguinte conteúdo:

```text
networkx
matplotlib
streamlit
```

### 4. Instalação das Dependências

Com o ambiente virtual ativado, instale todas as bibliotecas necessárias de uma só vez utilizando o arquivo de requisitos:

```bash
pip install -r requirements.txt
```

### 5. Executando a Aplicação
Para iniciar o sistema, execute o comando abaixo no terminal:

```Bash
python run.py
```


O navegador abrirá automaticamente com o sistema rodando (geralmente no endereço http://localhost:8501).

# 🚚 Sistema de Otimização de Rotas Logísticas

Este projeto é uma aplicação interativa de Pesquisa Operacional desenvolvida em Python. O sistema simula uma malha logística utilizando Teoria dos Grafos para calcular rotas otimizadas e analisar riscos operacionais em tempo real.

O objetivo é auxiliar na tomada de decisão logística, respondendo a perguntas como: "Qual é o caminho mais rápido?" e "O que acontece se essa estrada for bloqueada?"

Projeto desenvolvido para a disciplina de **Análise e Complexidade de Algoritmos.**

## 🧠 Arquitetura e Lógica do Sistema
O projeto adota princípios de **Engenharia de Software** para garantir modularidade e escalabilidade, dividindo responsabilidades entre lógica de negócios e interface.

**1. Estrutura Modular (Separation of Concerns)**

* **```src/core´´´ (Backend Lógico):** Responsável pela modelagem matemática utilizando a biblioteca **NetworkX.**

	* **Estrutura:** Grafo Direcionado Ponderado (DiGraph).
	* **Entidades:** Cidades (Nós), Estradas (Arestas) e Tempo de Viagem (Pesos).

* **`src/ui´ (Frontend Interativo):** Interface desenvolvida em **Streamlit**, otimizada com gestão de estado (Session State) e Callbacks para garantir interatividade fluida sem recarregamentos desnecessários.

**2. Algoritmo de Otimização**

O cálculo de rotas utiliza uma abordagem de Caminho Mínimo. O sistema avalia todos os caminhos simples viáveis entre origem e destino, selecionando aquele que minimiza a função de custo total ($C_{total} = \sum P_{arestas}$).

**3. Análise de Robustez e Risco**

O sistema implementa uma comparação dinâmica em tempo real para análise de contingência:

* **1. Cenário Ideal:** Rota otimizada na rede íntegra.

* **2. Cenário Simulado:** Recálculo de rotas considerando a "interdição" de arestas selecionadas pelo usuário.

	* **Resultado:** O sistema quantifica o impacto operacional (atraso em minutos) ou alerta para a ruptura total da rede (falta de caminhos alternativos).

## ✨ Funcionalidades Principais

* **📍 Seleção Bidirecional:** Escolha dinâmica de Origem e Destino com botão de inversão rápida de rota.

* **🛣️ Cálculo de Caminho Mínimo:** Identificação automática da rota mais eficiente.

* **🚧 Simulação de Falhas:** Interface para bloqueio de estradas e recálculo de contingência.

* **📊 Relatório de Impacto:** Feedback visual imediato sobre atrasos ou inviabilidade de entrega.

* **🗺️ Visualização Interativa:** Plotagem gráfica da rede com destaque colorido para a rota ativa (Matplotlib).

## 📂 Estrutura do Projeto
```
├── run.py                   # Script de Entrada (Entry Point)
├── requirements.txt         # Lista de dependências
├── src/
│   ├── core/                # Camada de Modelo
│   │   └── logistic_network.py  # Lógica de Grafos e NetworkX
│   └── ui/                  # Camada de Visualização
│       └── web_app.py       # Interface Streamlit
´´´

