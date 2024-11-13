# dados.py

# Informações dos ingredientes (em % de inclusão e composição nutricional)
ingredientes = {
    'Farelo de soja': {
        'MS': 89.6, 'PB': 46.16, 'PD': 45.24, 'EB': 4174.15, 'ED': 3396.92,
        'FB': 5.58, 'EE': 1.45, 'MM': 6.53, 'LYS': 2.73, 'MET': 0.66,
        'CIS': 0.65, 'TRP': 0.65, 'TRE': 1.84, 'Ca': 0.24, 'P_dis': 0.18
    },
    'Concentrado proteico de soja': {
        'MS': 90.0, 'PB': 60.0, 'PD': 58.02, 'EB': 4471.0, 'ED': 3737.76,
        'FB': 5.0, 'EE': 0.4, 'MM': 5.0, 'LYS': 2.47, 'MET': 0.85,
        'CIS': 0.81, 'TRP': 0.81, 'TRE': 2.47, 'Ca': 0.4, 'P_dis': 0.28
    },
    'Milho': {
        'MS': 87.6, 'PB': 7.81, 'PD': 7.09, 'EB': 3868.84, 'ED': 3329.91,
        'FB': 2.53, 'EE': 3.76, 'MM': 1.11, 'LYS': 0.25, 'MET': 0.16,
        'CIS': 0.19, 'TRP': 0.07, 'TRE': 0.3, 'Ca': 0.06, 'P_dis': 0.06
    },
    'Farelo de trigo': {
        'MS': 88.73, 'PB': 15.27, 'PD': 13.4, 'EB': 3888.89, 'ED': 2870.0,
        'FB': 8.29, 'EE': 3.84, 'MM': 4.72, 'LYS': 0.66, 'MET': 0.23,
        'CIS': 0.29, 'TRP': 0.27, 'TRE': 0.48, 'Ca': 0.14, 'P_dis': 0.26
    },
    'Óleo de soja': {
        'MS': 100.0, 'PB': 0.0, 'PD': 0.0, 'EB': 9443.83, 'ED': 8485.28,
        'FB': 0.0, 'EE': 100.0, 'MM': 0.0, 'LYS': 0.0, 'MET': 0.0,
        'CIS': 0.0, 'TRP': 0.0, 'TRE': 0.0, 'Ca': 0.0, 'P_dis': 0.0
    },
    'BHT': {
        'MS': 100.0, 'PB': 0.0, 'PD': 0.0, 'EB': 0.0, 'ED': 0.0,
        'FB': 0.0, 'EE': 0.0, 'MM': 0.0, 'LYS': 0.0, 'MET': 0.0,
        'CIS': 0.0, 'TRP': 0.0, 'TRE': 0.0, 'Ca': 0.0, 'P_dis': 0.0
    },
    'Calcário Calcítico': {
        'MS': 98.0, 'PB': 0.0, 'PD': 0.0, 'EB': 0.0, 'ED': 0.0,
        'FB': 0.0, 'EE': 0.0, 'MM': 38.4, 'LYS': 0.0, 'MET': 0.0,
        'CIS': 0.0, 'TRP': 0.0, 'TRE': 0.0, 'Ca': 38.4, 'P_dis': 0.0
    },
    'Fosfato Bicálcico': {
        'MS': 98.8, 'PB': 0.0, 'PD': 0.0, 'EB': 0.0, 'ED': 0.0,
        'FB': 0.0, 'EE': 0.0, 'MM': 24.5, 'LYS': 0.0, 'MET': 0.0,
        'CIS': 0.0, 'TRP': 0.0, 'TRE': 0.0, 'Ca': 24.5, 'P_dis': 18.5
    },
    'DL-Metionina': {
        'MS': 100.0, 'PB': 0.0, 'PD': 0.0, 'EB': 5442.0, 'ED': 0.0,
        'FB': 0.0, 'EE': 0.0, 'MM': 0.0, 'LYS': 0.0, 'MET': 99.9,
        'CIS': 0.0, 'TRP': 0.0, 'TRE': 0.0, 'Ca': 0.0, 'P_dis': 0.0
    },
    'L-Lisina': {
        'MS': 100.0, 'PB': 95.11, 'PD': 91.1, 'EB': 4770.0, 'ED': 0.0,
        'FB': 0.0, 'EE': 0.0, 'MM': 0.0, 'LYS': 99.9, 'MET': 0.0,
        'CIS': 0.0, 'TRP': 0.0, 'TRE': 0.0, 'Ca': 0.0, 'P_dis': 0.0
    },
    'Premix': {
        'MS': 100.0, 'PB': 0.0, 'PD': 0.0, 'EB': 0.0, 'ED': 0.0,
        'FB': 0.0, 'EE': 0.0, 'MM': 0.0, 'LYS': 0.0, 'MET': 0.0,
        'CIS': 0.0, 'TRP': 0.0, 'TRE': 0.0, 'Ca': 0.0, 'P_dis': 1.2
    }
}

# Exigências nutricionais do tambaqui (segundo Buzollo)
exigencias_nutricionais = {
    'MS': 90.5, 'PB': 32.0, 'PD': 29.0, 'EB': 4200.0, 'ED': 3300.0,
    'FB': 4.57, 'EE': 4.9, 'MM': 4.15, 'LYS': 1.6, 'MET': 0.7,
    'CIS': 0.3, 'TRP': 0.3, 'TRE': 1.1, 'Ca': 0.8, 'P_dis': 0.4
}

# Limites e proporções específicas para alguns ingredientes
restricoes = {
    'Premix': 0.5, # 0.5% Premix
    'BHT': 0.03, # 0.03% BHT
    'Caulim': None, # Caulim é apenas inerte
    'Farelo de arroz': 0.0, # Não usar farelo de arroz
    'Farelo de trigo': (0, 8.5), # Máximo de 8.5% de farelo de trigo
    'Concentrado proteico de soja': (0, 18), # Máximo de 18%
    'Farelo de soja': (0, 33) # Máximo de 33%
}
