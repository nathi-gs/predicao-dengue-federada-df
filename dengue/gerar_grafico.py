import matplotlib.pyplot as plt

# Os dados reais extraídos do log de treinamento
rodadas = [1, 2, 3, 4, 5]
perda_loss = [0.1853, 0.1010, 0.0748, 0.1044, 0.1086]

plt.figure(figsize=(8, 5))
plt.plot(rodadas, perda_loss, marker='o', linestyle='-', color='#1e3a8a', linewidth=2, markersize=8)

plt.title('Convergência do Modelo Federado (FedAvg)', fontsize=14, fontweight='bold')
plt.xlabel('Rodadas de Treinamento Federado (Rounds)', fontsize=12)
plt.ylabel('Erro de Predição (Loss - MSE)', fontsize=12)
plt.xticks(rodadas)
plt.grid(True, linestyle='--', alpha=0.6)

# Adicionando anotações
plt.annotate('Início: 0.185', xy=(1, 0.1853), xytext=(1.2, 0.175),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5))
plt.annotate('Mínimo: 0.074', xy=(3, 0.0748), xytext=(3, 0.090),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5))

# Salvando a imagem na pasta
plt.savefig('grafico_convergencia.png', dpi=300, bbox_inches='tight')
print("[+] Gráfico salvo com sucesso como 'grafico_convergencia.png'")