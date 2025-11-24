import networkx as nx
import matplotlib.pyplot as plt

class RedeLogistica:
    def __init__(self):
        self.grafo = nx.DiGraph()
        self.pos_layout = None 

    def adicionar_rotas(self, lista_de_rotas):
        self.grafo.add_weighted_edges_from(lista_de_rotas)
        # Layout circular para ficar bonito na tela
        self.pos_layout = nx.shell_layout(self.grafo)

    def remover_rota(self, origem, destino):
        if self.grafo.has_edge(origem, destino):
            self.grafo.remove_edge(origem, destino)
            print(f"⚠ ALERTA: Estrada entre {origem} e {destino} foi INTERDITADA.")
        else:
            print(f"Erro: A estrada {origem}-{destino} não existe.")

    def calcular_caminho_minimo(self, origem, destino):
        try:
            # Para grafos pequenos, isso funciona bem.
            todos_caminhos = list(nx.all_simple_paths(self.grafo, origem, destino))
        except nx.NodeNotFound:
            return None, float('inf')

        if not todos_caminhos:
            return None, float('inf')

        melhor_caminho = None
        melhor_custo = float('inf')

        for caminho in todos_caminhos:
            custo_atual = 0
            for u, v in zip(caminho, caminho[1:]):
                custo_atual += self.grafo[u][v]['weight']

            if custo_atual < melhor_custo:
                melhor_custo = custo_atual
                melhor_caminho = caminho

        return melhor_caminho, melhor_custo

    def visualizar(self, origem, destino, caminho_destaque=None, titulo="Mapa Logístico"):
        fig, ax = plt.subplots(figsize=(10, 8))
        
        cores_nos = []
        for node in self.grafo.nodes():
            if node == origem:
                cores_nos.append('lightgreen')
            elif node == destino:
                cores_nos.append('lightcoral')
            else:
                cores_nos.append('lightblue')

        nx.draw(self.grafo, self.pos_layout, ax=ax, with_labels=True, 
                node_color=cores_nos, node_size=3000, font_size=10, 
                edge_color='gray', width=1, arrowsize=20,
                connectionstyle='arc3, rad = 0.1')

        edge_labels = nx.get_edge_attributes(self.grafo, 'weight')
        nx.draw_networkx_edge_labels(self.grafo, self.pos_layout, ax=ax,
                                     edge_labels=edge_labels, font_color='red', label_pos=0.3)

        if caminho_destaque:
            arestas_caminho = list(zip(caminho_destaque, caminho_destaque[1:]))
            nx.draw_networkx_edges(self.grafo, self.pos_layout, ax=ax, edgelist=arestas_caminho, 
                                   edge_color='blue', width=4,
                                   connectionstyle='arc3, rad = 0.1')

        ax.set_title(titulo)
        return fig