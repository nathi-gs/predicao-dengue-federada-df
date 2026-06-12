import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import flwr as fl
from dados import carregar_dados_infodengue
from cliente import UbsCliente

def orquestrar_hospitais(cid: str):
    """
    Simula a inicialização de cada hospital, entregando uma fatia
    distinta de dados para cada um, emulando regiões diferentes.
    """
    nomes_ubs = ["UBS Norte (Planaltina)", "UBS Sul (Gama)", "Hospital Central", "UBS Oeste (Taguatinga)"]
    nome_atual = nomes_ubs[int(cid)]
    
    # Chama a função do arquivo dados.py
    X_completo, y_completo = carregar_dados_infodengue()
    
    # Divide os dados em 4 fatias
    fatia = len(X_completo) // 4
    inicio = int(cid) * fatia
    fim = inicio + fatia
    
    X_hospital = X_completo[inicio:fim]
    y_hospital = y_completo[inicio:fim]
    
    divisao = int(0.8 * len(X_hospital))
    
    # Chama a classe do arquivo cliente.py
    cliente = UbsCliente(
        nome_ubs=nome_atual,
        X_treino=X_hospital[:divisao], y_treino=y_hospital[:divisao],
        X_teste=X_hospital[divisao:], y_teste=y_hospital[divisao:]
    )
    return cliente.to_client()

if __name__ == "__main__":
    print("\n" + "="*60)
    print("INICIANDO SISTEMA FEDERADO DE PREVENÇÃO DE DENGUE DO DISTRITO FEDERAL")
    print("="*60)
    
    estrategia_servidor = fl.server.strategy.FedAvg(
        fraction_fit=1.0, 
        min_available_clients=4 
    )

    fl.simulation.start_simulation(
        client_fn=orquestrar_hospitais,
        num_clients=4,
        config=fl.server.ServerConfig(num_rounds=5),
        strategy=estrategia_servidor,
    )