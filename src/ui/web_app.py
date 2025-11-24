import streamlit as st
import sys
import os

# --- HACK DE PATH (SÊNIOR FIX) ---
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    from src.core.logistic_network import RedeLogistica
except ModuleNotFoundError as e:
    st.error(f"Erro Crítico de Importação: {e}")
    st.stop()
# -----------------------------------------------

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Sistema de Logística", layout="wide")

st.title("🚚 Otimização de Rotas Logísticas")
st.markdown("Selecione o armazém, o cliente e simule incidentes para testar a robustez da rede.")

# --- 1. ESTADO DA APLICAÇÃO (MEMÓRIA) ---
if 'rede' not in st.session_state:
    rede = RedeLogistica()
    # Dados iniciais
    dados_rotas = [
        ('Vassouras', 'Maricá', 205),
        ('Vassouras', 'Itaboraí', 181),
        ('Vassouras', 'Saquarema', 231),
        ('Maricá', 'Vassouras', 200),
        ('Maricá', 'Itaboraí', 32),
        ('Maricá', 'Saquarema', 50),
        ('Saquarema', 'Vassouras', 221),
        ('Saquarema', 'Maricá', 51),
        ('Saquarema', 'Itaboraí', 57),
        ('Itaboraí', 'Vassouras', 173),
        ('Itaboraí', 'Maricá', 34),
        ('Itaboraí', 'Saquarema', 61),
    ]
    rede.adicionar_rotas(dados_rotas)
    st.session_state.rede = rede
    st.session_state.rotas_originais = dados_rotas

# Acessa a rede da memória (apenas para ler os nós na sidebar)
rede_base_leitura = st.session_state.rede
cidades = list(rede_base_leitura.grafo.nodes())

# --- 2. BARRA LATERAL (CONTROLES) ---
with st.sidebar:
    st.header("📍 Configuração da Rota")
    
    # 1. INICIALIZAÇÃO DE ESTADO
    # Garante que o Streamlit saiba quem são origem/destino antes de renderizar os widgets
    if 'cidade_origem' not in st.session_state:
        st.session_state.cidade_origem = cidades[0]
    if 'cidade_destino' not in st.session_state:
        st.session_state.cidade_destino = cidades[1] if len(cidades) > 1 else cidades[0]

    # 2. FUNÇÃO DE CALLBACK (Lógica de Inversão)
    # Executada instantaneamente ao clicar no botão, antes da página recarregar
    def inverter_cidades():
        st.session_state.cidade_origem, st.session_state.cidade_destino = \
            st.session_state.cidade_destino, st.session_state.cidade_origem

    # 3. SELECTBOX ORIGEM
    origem = st.selectbox(
        "Armazém (Origem)", 
        options=cidades, 
        key='cidade_origem' 
    )

    # 4. SELECTBOX DESTINO
    destino = st.selectbox(
        "Cliente (Destino)", 
        options=cidades, 
        key='cidade_destino'
    )

    # 5. BOTÃO DISCRETO (Abaixo do destino)
    # Criamos duas colunas: uma vazia (60%) e uma para o botão (40%) para jogá-lo para a direita
    col_espaco, col_botao = st.columns([0.6, 0.4]) 
    
    with col_botao:
        st.button("🔄", on_click=inverter_cidades, use_container_width=True)

    st.divider()
    
    st.header("🚧 Gestão de Incidentes")
    st.write("Simule falhas na rede removendo estradas:")
    
    # Pega as arestas da rede base para mostrar as opções
    todas_arestas = list(rede_base_leitura.grafo.edges())
    lista_formatada = [f"{u} -> {v}" for u, v in todas_arestas]
    
    rotas_removidas = st.multiselect(
        "Estradas Interditadas:",
        options=lista_formatada,
        placeholder="Nenhum incidente..."
    )

    if st.button("♻ Recalcular"):
        # Limpa a rede modificada da memória para forçar a recriação no início do script
        del st.session_state.rede
        st.rerun()

# --- 3. CÁLCULOS DE CENÁRIO (Base vs Simulado) ---

# A) Cenário BASE (Sem incidentes, rede perfeita)
rede_ideal = RedeLogistica()
rede_ideal.adicionar_rotas(st.session_state.rotas_originais)
rota_ideal, custo_ideal = rede_ideal.calcular_caminho_minimo(origem, destino)

# B) Cenário SIMULADO (Com os bloqueios do usuário)
rede_simulada = RedeLogistica()
rede_simulada.adicionar_rotas(st.session_state.rotas_originais)

if rotas_removidas:
    for item in rotas_removidas:
        u, v = item.split(" -> ")
        rede_simulada.remover_rota(u, v)

rota_real, custo_real = rede_simulada.calcular_caminho_minimo(origem, destino)

# --- 4. ÁREA PRINCIPAL (RESULTADOS) ---
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📊 Relatório de Entrega")
    
    if origem == destino:
        st.warning("A Origem e o Destino são a mesma cidade!")
    else:
        # Exibe o status da rota atual (Simulada)
        if rota_real:
            st.success(f"✔ Rota Viável Encontrada")
            st.metric(label="Tempo Estimado (Atual)", value=f"{custo_real} min")
            
            st.markdown("### 🛣 Trajeto Atual:")
            for i in range(len(rota_real) - 1):
                u, v = rota_real[i], rota_real[i+1]
                peso = rede_simulada.grafo[u][v]['weight']
                st.write(f"{i+1}. **{u}** ➝ **{v}** ({peso} min)")
        else:
            st.error("❌ ENTREGA IMPOSSÍVEL")
            st.metric(label="Status", value="Cancelado")

        st.divider()

        # --- ANÁLISE DE ROBUSTEZ (A Lógica da Parte 4) ---
        st.subheader("🛡️ Análise de Robustez")
        
        impacto_msg = ""
        
        # Caso 1: Nenhuma falha simulada ou a falha não afetou a rota original
        if custo_real == custo_ideal:
            st.info("✅ **Sem Impacto:** A rede opera em condições normais ou a rota principal não foi afetada pelos bloqueios.")
        
        # Caso 2: Houve falha, mas existe rota alternativa (Custo aumentou)
        elif custo_real < float('inf'):
            atraso = custo_real - custo_ideal
            st.warning(f"⚠️ **Impacto Moderado:** Avaria na rede detectada.")
            st.write(f"**Análise:** Uma rota crítica falhou, mas o sistema encontrou contingência.")
            st.markdown(f"""
            > **Caso a falha ocorra, qual é o impacto na entrega de mercadorias?** > R: Haverá um atraso de **{atraso} minutos** na entrega.
            >
            > **Há alternativas viáveis?** > R: Sim, o desvio pela rota **{' ➝ '.join(rota_real)}** garante a entrega.
            """)
            
        # Caso 3: Falha Crítica (Não existe caminho)
        else:
            st.error(f"🚨 **IMPACTO CRÍTICO:** Ruptura total da cadeia logística.")
            st.markdown(f"""
            > **Caso a falha ocorra, qual é o impacto na entrega de mercadorias?** > R: A entrega foi **CANCELADA**. Não é possível chegar ao destino.
            >
            > **Há alternativas viáveis?** > R: Não. As estradas bloqueadas eram **gargalos únicos (Pontes)** para este destino.
            """)

with col2:
    st.subheader("🗺 Visualização da Rede")
    
    if origem != destino:
        # Mostra o gráfico do cenário simulado
        # Se não houver rota (None), o gráfico ainda mostra a rede, mas sem destaque
        figura = rede_simulada.visualizar(origem, destino, caminho_destaque=rota_real)
        st.pyplot(figura)
    else:
        st.info("Selecione cidades diferentes para gerar o mapa.")