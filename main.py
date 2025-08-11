# =============================================
# Controle Fuzzy de Potência de Aquecedor
# Autor: [Seu Nome]
# Descrição: Exemplo para aplicação em artigo
# Bibliotecas: numpy, matplotlib, scikit-fuzzy
# =============================================

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# -------------------------------
# 1. Definição das variáveis fuzzy
# -------------------------------
temperatura = ctrl.Antecedent(np.arange(0, 41, 1), 'temperatura')  # 0°C a 40°C
umidade = ctrl.Antecedent(np.arange(0, 101, 1), 'umidade')         # 0% a 100%
potencia = ctrl.Consequent(np.arange(0, 101, 1), 'potencia')       # 0% a 100%

# -------------------------------
# 2. Funções de pertinência
# -------------------------------
temperatura['baixa'] = fuzz.trimf(temperatura.universe, [0, 0, 20])
temperatura['media'] = fuzz.trimf(temperatura.universe, [15, 25, 35])
temperatura['alta'] = fuzz.trimf(temperatura.universe, [30, 40, 40])

umidade['baixa'] = fuzz.trimf(umidade.universe, [0, 0, 50])
umidade['media'] = fuzz.trimf(umidade.universe, [30, 50, 70])
umidade['alta'] = fuzz.trimf(umidade.universe, [60, 100, 100])

potencia['baixa'] = fuzz.trimf(potencia.universe, [0, 0, 50])
potencia['media'] = fuzz.trimf(potencia.universe, [30, 50, 70])
potencia['alta'] = fuzz.trimf(potencia.universe, [60, 100, 100])

# -------------------------------
# 3. Definição das regras fuzzy
# -------------------------------
regra1 = ctrl.Rule(temperatura['baixa'] & umidade['alta'], potencia['alta'])
regra2 = ctrl.Rule(temperatura['baixa'] & umidade['media'], potencia['alta'])
regra3 = ctrl.Rule(temperatura['baixa'] & umidade['baixa'], potencia['media'])
regra4 = ctrl.Rule(temperatura['media'] & umidade['alta'], potencia['media'])
regra5 = ctrl.Rule(temperatura['media'] & umidade['media'], potencia['media'])
regra6 = ctrl.Rule(temperatura['media'] & umidade['baixa'], potencia['baixa'])
regra7 = ctrl.Rule(temperatura['alta'], potencia['baixa'])

# -------------------------------
# 4. Construção do sistema fuzzy
# -------------------------------
sistema_ctrl = ctrl.ControlSystem([regra1, regra2, regra3, regra4, regra5, regra6, regra7])
sistema = ctrl.ControlSystemSimulation(sistema_ctrl)

# -------------------------------
# 5. Simulação de um caso
# -------------------------------
entrada_temperatura = 18
entrada_umidade = 65

sistema.input['temperatura'] = entrada_temperatura
sistema.input['umidade'] = entrada_umidade
sistema.compute()

print(f"Temperatura: {entrada_temperatura}°C")
print(f"Umidade: {entrada_umidade}%")
print(f"Potência recomendada: {sistema.output['potencia']:.2f}%")

# -------------------------------
# 6. Visualização das funções
# -------------------------------
fig, axs = plt.subplots(nrows=3, figsize=(8, 10))
temperatura.view(ax=axs[0])
umidade.view(ax=axs[1])
potencia.view(ax=axs[2])
plt.tight_layout()
plt.show()

# -------------------------------
# 7. Visualização do resultado da inferência
# -------------------------------
potencia.view(sistema)
plt.show()
