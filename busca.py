from grafo import grafo

def carregar_grafo(nome_arquivo):
    grafo = {}
    try:
        local_vars = {}
        exec(open(nome_arquivo).read(), {}, local_vars)
        grafo = local_vars.get('grafo', {})
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
    return grafo

def executar_busca(grafo, algoritmo, inicio, objetivo):
    try:
        resultado = algoritmo(grafo, inicio, objetivo)
        return resultado
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")
        return None
