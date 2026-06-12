# 🦟 Predição Epidemiológica de Dengue via Aprendizagem Federada

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep_Learning-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Flower](https://img.shields.io/badge/Flower-Federated_Learning-FFD43B?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)

> **Projeto submetido à categoria Ensino Superior do 32º Prêmio Jovem Cientista (2026).** > Implementação de um ecossistema preditivo para surtos de dengue no Distrito Federal (DF), garantindo total conformidade com a Lei Geral de Proteção de Dados (LGPD) através do paradigma *Privacy by Design*.

---

## 📌 Visão Geral do Projeto

O objetivo principal desta arquitetura é capacitar as Unidades Básicas de Saúde (UBS) do Distrito Federal a construírem um modelo de Inteligência Artificial preditivo global de forma colaborativa, **sem que nenhuma unidade precise compartilhar ou centralizar os dados sensíveis de seus pacientes**.

### ⚙️ Como funciona a arquitetura?
1. 🏛️ **O Servidor Central** (Secretaria de Saúde) envia um modelo LSTM inicial para as UBSs.
2. 🏥 **Cada UBS** (nó local) treina o modelo localmente utilizando seu próprio histórico de casos e variáveis climáticas.
3. 🔒 **Segurança:** Os nós enviam de volta ao servidor apenas as atualizações matemáticas (pesos). *Os dados brutos nunca saem da UBS.*
4. 🧠 **Agregação:** O Servidor combina as atualizações usando o algoritmo `FedAvg` (Federated Averaging), gerando um modelo global mais inteligente.

---

## 🛠️ Tecnologias Utilizadas

* **Orquestração Federada:** `Flower (flwr)` e `Ray`
* **Deep Learning:** `TensorFlow` / `Keras` (Arquitetura LSTM)
* **Processamento de Dados:** `Pandas` e `Scikit-learn`
* **Visualização Científica:** `Matplotlib`
* **Fonte de Dados:** API InfoDengue (Fiocruz/FGV)

---

## 📂 Estrutura do Repositório

O pipeline foi estruturado de forma estritamente modular:

```text
📦 projeto_dengue
 ┣ 📜 dados.py         # Consumo da API, limpeza e criação da Janela Deslizante.
 ┣ 📜 modelo.py        # Arquitetura da Rede Neural Recorrente (LSTM).
 ┣ 📜 cliente.py       # Lógica do nó local da UBS (Treinamento on-device).
 ┣ 📜 servidor.py      # Orquestrador centralizado (Estratégia FedAvg).
 ┗ 📜 gerar_grafico.py # Script para plotagem da convergência do erro.
```
---

## 🚀 **Como Executar a Simulação**

Para replicar a simulação no seu ambiente local, instale as dependências executando o comando abaixo no terminal:
pip install flwr tensorflow scikit-learn pandas requests numpy matplotlib "flwr[simulation]"

Com os arquivos na mesma pasta, inicie a simulação executando o orquestrador (que instanciará os nós virtuais automaticamente):
python servidor.py

---

## 📈 **Resultados e Convergência**

A simulação demonstrou uma rápida convergência matemática da rede global. O erro quadrático médio (Loss) decaiu significativamente ao longo de 5 rodadas de comunicação, provando a eficácia da aprendizagem descentralizada:

Rodada,Loss (MSE),Observação
1,0.1853,Fase inicial de calibração do modelo
2,0.1010,Queda acentuada do erro após primeira troca de pesos
3,0.0748,🏆 Ponto ótimo (Redução de ~60% no erro inicial)
4,0.1044,Ajuste global frente à heterogeneidade dos dados (Não-IID)
5,0.1086,Estabilização e generalização do modelo

Para gerar o gráfico científico desta tabela, execute:
python gerar_grafico.py
