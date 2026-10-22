import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração global de estilo
sns.set_theme(style="whitegrid")

# ==============================================================================
# 1. Gráfico de Barras (dados_barras.csv)
# ==============================================================================
def gerar_grafico_barras():
    print("Gerando Gráfico de Barras...")
    df = pd.read_csv('dados_barras.csv')
    
    plt.figure(figsize=(9, 5))
    sns.barplot(data=df, x='categoria', y='vendas_medias', hue='regiao')
    plt.title('Vendas Médias por Categoria e Região')
    plt.xlabel('Categoria')
    plt.ylabel('Vendas Médias (R$)')
    plt.tight_layout()
    plt.show()

# ==============================================================================
# 2. Diagrama de Caixa / Boxplot (dados_boxplot.csv)
# ==============================================================================
def gerar_grafico_boxplot():
    print("Gerando Boxplot...")
    df = pd.read_csv('dados_boxplot.csv')
    
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df, x='departamento', y='salario', palette='Set2')
    plt.title('Distribuição Salarial por Departamento')
    plt.xlabel('Departamento')
    plt.ylabel('Salário (R$)')
    plt.tight_layout()
    plt.show()

# ==============================================================================
# 3. Gráfico de Dispersão / Scatter Plot (dados_dispersao.csv)
# ==============================================================================
def gerar_grafico_dispersao():
    print("Gerando Gráfico de Dispersão...")
    df = pd.read_csv('dados_dispersao.csv')
    
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x='altura_cm', y='peso_kg', hue='sexo', style='sexo', s=70)
    plt.title('Relação entre Altura e Peso por Sexo')
    plt.xlabel('Altura (cm)')
    plt.ylabel('Peso (kg)')
    plt.tight_layout()
    plt.show()

# ==============================================================================
# 4. Gráfico de Distribuição / Histograma (dados_distribuicao.csv)
# ==============================================================================
def gerar_grafico_distribuicao():
    print("Gerando Gráfico de Distribuição...")
    df = pd.read_csv('dados_distribuicao.csv')
    
    plt.figure(figsize=(8, 5))
    sns.histplot(df['idade'], kde=True, bins=15, color='teal')
    plt.title('Distribuição de Idade dos Clientes')
    plt.xlabel('Idade')
    plt.ylabel('Frequência / Contagem')
    plt.tight_layout()
    plt.show()

# ==============================================================================
# 5. Gráfico de Frequência (dados_frequencia.csv)
# ==============================================================================
def gerar_grafico_frequencia():
    print("Gerando Gráfico de Frequência...")
    df = pd.read_csv('dados_frequencia.csv')
    
    df_counts = df['tipo_atendimento'].value_counts().reset_index()
    df_counts.columns = ['tipo_atendimento', 'frequencia']
    
    plt.figure(figsize=(8, 5))
    sns.barplot(data=df_counts, x='tipo_atendimento', y='frequencia', palette='viridis')
    plt.title('Frequência de Tipos de Atendimento')
    plt.xlabel('Tipo de Atendimento')
    plt.ylabel('Quantidade de Chamados')
    plt.tight_layout()
    plt.show()

# ==============================================================================
# 6. Mapa de Calor / Heatmap (dados_heatmap.csv)
# ==============================================================================
def gerar_grafico_heatmap():
    print("Gerando Heatmap...")
    df = pd.read_csv('dados_heatmap.csv')
    
    dias_ordem = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
    pivot_heatmap = df.pivot(index='dia_semana', columns='horario', values='movimento_clientes')
    pivot_heatmap = pivot_heatmap.reindex([d for d in dias_ordem if d in pivot_heatmap.index])
    
    plt.figure(figsize=(9, 6))
    sns.heatmap(pivot_heatmap, annot=True, fmt="d", cmap="YlGnBu", cbar_kws={'label': 'Movimento de Clientes'})
    plt.title('Mapa de Calor do Movimento de Clientes por Dia e Horário')
    plt.xlabel('Horário')
    plt.ylabel('Dia da Semana')
    plt.tight_layout()
    plt.show()

# ==============================================================================
# 7. Gráfico de Linhas (dados_linhas.csv)
# ==============================================================================
def gerar_grafico_linhas():
    print("Gerando Gráfico de Linhas...")
    df = pd.read_csv('dados_linhas.csv')
    df['data'] = pd.to_datetime(df['data'])
    
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=df, x='data', y='vendas', hue='loja', marker='o')
    plt.title('Evolução das Vendas ao Longo do Tempo por Loja')
    plt.xlabel('Data')
    plt.ylabel('Vendas')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# ==============================================================================
# 8. Gráfico de Pizza (dados_pizza.csv)
# ==============================================================================
def gerar_grafico_pizza():
    print("Gerando Gráfico de Pizza...")
    df = pd.read_csv('dados_pizza.csv')
    
    plt.figure(figsize=(7, 7))
    plt.pie(
        df['faturamento'], 
        labels=df['canal_venda'], 
        autopct='%1.1f%%', 
        startangle=140, 
        colors=sns.color_palette('pastel')
    )
    plt.title('Distribuição do Faturamento por Canal de Venda')
    plt.tight_layout()
    plt.show()

# ==============================================================================
# 9. Gráfico de Regressão Linear (dados_regressao.csv)
# ==============================================================================
def gerar_grafico_regressao():
    print("Gerando Gráfico de Regressão...")
    df = pd.read_csv('dados_regressao.csv')
    
    plt.figure(figsize=(8, 5))
    sns.regplot(
        data=df, 
        x='renda_mensal', 
        y='gasto_mensal', 
        scatter_kws={'alpha': 0.7}, 
        line_kws={'color': 'red'}
    )
    plt.title('Regressão: Relação entre Renda Mensal e Gasto Mensal')
    plt.xlabel('Renda Mensal (R$)')
    plt.ylabel('Gasto Mensal (R$)')
    plt.tight_layout()
    plt.show()

# ==============================================================================
# Execução Principal
# ==============================================================================
if __name__ == '__main__':
    gerar_grafico_barras()
    gerar_grafico_boxplot()
    gerar_grafico_dispersao()
    gerar_grafico_distribuicao()
    gerar_grafico_frequencia()
    gerar_grafico_heatmap()
    gerar_grafico_linhas()
    gerar_grafico_pizza()
    gerar_grafico_regressao()