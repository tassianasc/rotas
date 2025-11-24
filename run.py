import os
import sys

def main():
    """
    Script auxiliar para rodar a aplicação Streamlit apontando para o arquivo correto.
    """
    # Caminho absoluto para o arquivo da interface
    app_path = os.path.join('src', 'ui', 'web_app.py')
    
    print(f"🚀 Iniciando Sistema de Logística...")
    print(f"📂 Carregando aplicação de: {app_path}")
    
    # Executa o comando do streamlit via shell
    os.system(f"streamlit run {app_path}")

if __name__ == "__main__":
    main()