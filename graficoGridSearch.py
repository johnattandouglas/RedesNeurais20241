import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados dos arquivos
df_early = pd.read_csv('resultadosEarly.csv')

# Filtrar os dados para incluir apenas as condições desejadas, excluindo os resultados com 50 neurônios
df_early_linear = df_early[(df_early['batch_size'] == 4) & 
                           (df_early['learning_rate'] == 0.001) & 
                           (df_early['activation'] == 'linear') &
                           (df_early['neurons'] != 50)]
df_early_tanh = df_early[(df_early['batch_size'] == 4) & 
                         (df_early['learning_rate'] == 0.001) & 
                         (df_early['activation'] == 'tanh') &
                         (df_early['neurons'] != 50)]
df_early_relu = df_early[(df_early['batch_size'] == 4) & 
                         (df_early['learning_rate'] == 0.001) & 
                         (df_early['activation'] == 'relu') &
                         (df_early['neurons'] != 50)]

# Encontrar o menor score para cada combinação de neurônios para linear
best_scores_early_linear = df_early_linear.groupby('neurons')['score'].min().reset_index()

# Encontrar o menor score para cada combinação de neurônios para tanh
best_scores_early_tanh = df_early_tanh.groupby('neurons')['score'].min().reset_index()

# Encontrar o menor score para cada combinação de neurônios para relu
best_scores_early_relu = df_early_relu.groupby('neurons')['score'].min().reset_index()

# Ordenar os dados por número de neurônios
best_scores_early_linear = best_scores_early_linear.sort_values(by='neurons')
best_scores_early_tanh = best_scores_early_tanh.sort_values(by='neurons')
best_scores_early_relu = best_scores_early_relu.sort_values(by='neurons')

# Plotar o gráfico comparativo dos scores
plt.figure(figsize=(5, 3.5))

if not best_scores_early_linear.empty:
    plt.plot(best_scores_early_linear['neurons'], best_scores_early_linear['score'], marker='o', linestyle='--', label='Linear Activation')
if not best_scores_early_tanh.empty:
    plt.plot(best_scores_early_tanh['neurons'], best_scores_early_tanh['score'], marker='o', linestyle='--', label='Tanh Activation')
if not best_scores_early_relu.empty:
    plt.plot(best_scores_early_relu['neurons'], best_scores_early_relu['score'], marker='o', linestyle='--', label='ReLU Activation')

plt.xlabel('Quantidade de Neurônios')
plt.ylabel('Score')
plt.legend()
plt.grid(True)
plt.xticks(best_scores_early_linear['neurons'])  # Use os neurônios comuns como ticks no eixo x
plt.tight_layout()
plt.savefig('grafico_com_early_stopping.png')
plt.show()