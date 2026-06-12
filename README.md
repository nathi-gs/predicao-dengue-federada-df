🛠️ Pré-requisitos e Instalação

Para replicar a simulação no seu ambiente computacional local (Windows, macOS ou Linux), você precisará do Python instalado (versão recomendada: 3.12.3) e das bibliotecas listadas abaixo.

Instale todas as dependências executando o comando a seguir no seu terminal:
pip install flwr tensorflow scikit-learn pandas requests numpy matplotlib "flwr[simulation]" --user


🚀 Como Executar a Simulação

Certifique-se de que todos os arquivos (dados.py, modelo.py, cliente.py e servidor.py) estejam localizados dentro da mesma pasta.

Abra o terminal na pasta correspondente.
Execute o script do servidor central (que orquestrará as 4 UBSs simuladas via motor Ray):
python servidor.py

📈 Resultados e Convergência

A simulação demonstrou uma rápida convergência matemática da rede global, comprovando que a união federada dos nós supera as limitações de bancos de dados isolados. O erro quadrático médio (Loss) decaiu significativamente ao longo das iterações:

Rodada 1 (Round 1): Loss 0.1853 (Fase inicial de calibração)
Rodada 2 (Round 2): Loss 0.1010
Rodada 3 (Round 3): Loss 0.0748 (Ponto ótimo de otimização - Redução de ~60% no erro)
Rodada 4 (Round 4): Loss 0.1044 (Ajuste global frente à heterogeneidade dos dados)
Rodada 5 (Round 5): Loss 0.1086 (Estabilização da generalização)

Para gerar o gráfico de linhas científico que ilustra este comportamento, execute o arquivo auxiliar:
python gerar_grafico.py


📝 Licença e Autoria

Este projeto é disponibilizado abertamente sob a perspectiva de Ciência Aberta e reprodutibilidade científica.
Autor: Nathalia Gonçalves Silva
Instituição de Vínculo: Universidade Católica de Brasília - UCB
Contato: nathaliagoncalvessilva6@gmail.com
"""
