import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados dos arquivos
df_early = pd.read_csv('resultadosEarly.csv')
df = pd.read_csv('resultados.csv')

# # Filtrar os dados para considerar apenas o tamanho de lote de 4, taxa de aprendizado de 0.001 e função tanh
# df_early_filtered = df_early[(df_early['batch_size'] == 4) & 
#                              (df_early['learning_rate'] == 0.001) & 
#                              (df_early['activation'] == 'tanh')]
# df_filtered = df[(df['batch_size'] == 4) & 
#                  (df['learning_rate'] == 0.001) & 
#                  (df['activation'] == 'tanh')]

# # Encontrar o melhor score para cada combinação de neurônios
# best_scores_early = df_early_filtered.groupby('neurons')['score'].max().reset_index()
# best_scores = df_filtered.groupby('neurons')['score'].max().reset_index()

# # Ordenar os dados por número de neurônios
# best_scores_early = best_scores_early.sort_values(by='neurons')
# best_scores = best_scores.sort_values(by='neurons')

# # Plotar o gráfico comparativo dos scores
# plt.figure(figsize=(4, 3))
# plt.plot(best_scores_early['neurons'], best_scores_early['score'], marker='o', label='Com Early Stopping')
# plt.plot(best_scores['neurons'], best_scores['score'], marker='o', label='Sem Early Stopping')
# plt.xlabel('Quantidade de Neurônios')
# plt.ylabel('Score')
# plt.legend()
# plt.grid(True)
# plt.xticks(best_scores_early['neurons'])  # Define os valores de xticks para corresponder aos neurônios
# plt.tight_layout()  # Ajusta o layout para evitar que as legendas e rótulos se sobreponham
# plt.savefig('grafico_grid.png')  # Salva a figura em um arquivo
# plt.show()


# Filtrar os dados para considerar apenas o tamanho de lote de 4, taxa de aprendizado de 0.001 e função tanh
df_early_tanh = df_early[(df_early['batch_size'] == 4) & 
                         (df_early['learning_rate'] == 0.001) & 
                         (df_early['activation'] == 'tanh')]
df_tanh = df[(df['batch_size'] == 4) & 
             (df['learning_rate'] == 0.001) & 
             (df['activation'] == 'tanh')]

# Filtrar os dados para considerar apenas o tamanho de lote de 4, taxa de aprendizado de 0.001 e função linear
df_early_linear = df_early[(df_early['batch_size'] == 4) & 
                           (df_early['learning_rate'] == 0.001) & 
                           (df_early['activation'] == 'linear')]
df_linear = df[(df['batch_size'] == 4) & 
               (df['learning_rate'] == 0.001) & 
               (df['activation'] == 'linear')]

# Encontrar o melhor score para cada combinação de neurônios para tanh
best_scores_early_tanh = df_early_tanh.groupby('neurons')['score'].max().reset_index()
best_scores_tanh = df_tanh.groupby('neurons')['score'].max().reset_index()

# Encontrar o melhor score para cada combinação de neurônios para linear
best_scores_early_linear = df_early_linear.groupby('neurons')['score'].max().reset_index()
best_scores_linear = df_linear.groupby('neurons')['score'].max().reset_index()

# Ordenar os dados por número de neurônios para tanh
best_scores_early_tanh = best_scores_early_tanh.sort_values(by='neurons')
best_scores_tanh = best_scores_tanh.sort_values(by='neurons')

# Ordenar os dados por número de neurônios para linear
best_scores_early_linear = best_scores_early_linear.sort_values(by='neurons')
best_scores_linear = best_scores_linear.sort_values(by='neurons')

# Plotar o gráfico comparativo dos scores
plt.figure(figsize=(10, 6))
plt.plot(best_scores_early_tanh['neurons'], best_scores_early_tanh['score'], marker='o', label='Com Early Stopping (tanh)')
plt.plot(best_scores_tanh['neurons'], best_scores_tanh['score'], marker='o', label='Sem Early Stopping (tanh)')
plt.plot(best_scores_early_linear['neurons'], best_scores_early_linear['score'], marker='o', label='Com Early Stopping (linear)')
plt.plot(best_scores_linear['neurons'], best_scores_linear['score'], marker='o', label='Sem Early Stopping (linear)')
plt.xlabel('Quantidade de Neurônios')
plt.ylabel('Score')
plt.title('Comparação dos Scores com e sem Early Stopping (Tamanho do Lote: 4, Taxa de Aprendizado: 0.001)')
plt.legend()
plt.grid(True)
plt.xticks(best_scores_early_tanh['neurons'])  # Define os valores de xticks para corresponder aos neurônios
plt.tight_layout()  # Ajusta o layout para evitar que as legendas e rótulos se sobreponham
plt.savefig('grafico_grid2.png')  # Salva a figura em um arquivo
plt.show()