# formulacao.py

import pandas as pd
from scipy.optimize import linprog
from dados import ingredientes, exigencias_nutricionais, restricoes

# Convertendo dados de ingredientes para um DataFrame
df_ingredientes = pd.DataFrame(ingredientes).T

# Coletando apenas os valores nutricionais principais
nutrientes = ['PB', 'PD', 'EB', 'ED', 'FB', 'EE', 'MM', 'LYS', 'MET', 'CIS', 'TRP', 'TRE', 'Ca', 'P_dis']
nutrition_matrix = df_ingredientes[nutrientes].values.T

# Configurando os limites das exigências nutricionais como restrições
nutrition_constraints = [-exigencias_nutricionais[nutriente] for nutriente in nutrientes]

# Configurando limites para cada ingrediente com base em `restricoes`
bounds = []
for ingrediente in df_ingredientes.index:
    if ingrediente in restricoes:
        limite = restricoes[ingrediente]
        if isinstance(limite, tuple):
            bounds.append((limite[0], limite[1]))
        else:
            bounds.append((limite, limite))
    else:
        bounds.append((0, 100))  # Sem limite específico

# Função objetivo (minimizar a soma total dos ingredientes)
objective = [1] * len(df_ingredientes)

# Executando a otimização
resultado = linprog(
    c=objective,
    A_ub=-nutrition_matrix,
    b_ub=nutrition_constraints,
    bounds=bounds,
    method='highs'
)

# Exibindo resultado
if resultado.success:
    proporcoes = pd.DataFrame({
        'Ingrediente': df_ingredientes.index,
        'Inclusão (%)': resultado.x * 100
    })
    print("Proporções dos ingredientes para atender às exigências nutricionais:")
    print(proporcoes)
else:
    print("Não foi possível encontrar uma solução que atenda a todas as restrições.")
