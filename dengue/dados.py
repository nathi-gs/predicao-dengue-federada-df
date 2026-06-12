import numpy as np
import pandas as pd
import requests
import io
from sklearn.preprocessing import MinMaxScaler

def carregar_dados_infodengue():
    print("[*] Baixando dados do DF...")
    url = "https://info.dengue.mat.br/api/alerta"
    parametros = {
        "geocode": "5300108", # DF
        "disease": "dengue",
        "format": "csv",
        "ew_start": 1, "ey_start": 2020,
        "ew_end": 52, "ey_end": 2023
    }
    
    try:
        resposta = requests.get(url, params=parametros, timeout=10)
        if resposta.status_code == 200:
            df = pd.read_csv(io.StringIO(resposta.text))
            df = df[['tempmin', 'tempmax', 'casos']].fillna(0)
            print("[+] Dados baixados com sucesso!")
        else:
            raise Exception("Falha na API")
    except:
        print("[-] Erro de conexão. Gerando dados de contingência...")
        df = pd.DataFrame({
            'tempmin': np.random.uniform(15, 22, 200),
            'tempmax': np.random.uniform(25, 33, 200),
            'casos': np.random.randint(0, 500, 200)
        })

    # Normalização
    scaler = MinMaxScaler()
    dados_norm = scaler.fit_transform(df)
    
    X, y = [], []
    semanas_historico = 4
    for i in range(len(dados_norm) - semanas_historico):
        X.append(dados_norm[i:(i + semanas_historico), :])
        y.append(dados_norm[i + semanas_historico, 2])
        
    return np.array(X), np.array(y)