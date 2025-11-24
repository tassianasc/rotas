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