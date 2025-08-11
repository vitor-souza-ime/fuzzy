# Controle Fuzzy de Potência de Aquecedor

Este projeto implementa um sistema de controle fuzzy baseado na arquitetura clássica de **Mamdani** (Mamdani e Assilian, 1975) para regular a potência de um aquecedor em função da temperatura e umidade do ambiente.

O sistema utiliza **regras linguísticas do tipo SE-ENTÃO** e método de defuzzificação pelo **Centro de Gravidade** para converter variáveis difusas (*fuzzy*) em uma saída nítida (*crisp*).

## 📂 Estrutura do Projeto
```

.
├── main.py      # Código principal do sistema fuzzy
└── README.md    # Documentação do projeto

```

## 🚀 Funcionalidades
- Modelagem fuzzy das variáveis **temperatura**, **umidade** e **potência**.
- Definição de **funções de pertinência triangulares** para cada variável.
- Conjunto de **7 regras fuzzy** para determinar a potência ideal do aquecedor.
- Visualização gráfica das funções de pertinência e do resultado da inferência.

## 📊 Exemplo de Uso
Entrada:
- Temperatura: `18°C`
- Umidade: `65%`

Saída:
```

Temperatura: 18°C
Umidade: 65%
Potência recomendada: 62.50%

````

O resultado inclui gráficos das funções de pertinência e o valor **crisp** calculado.

## 📦 Requisitos
O código foi testado com:
- Python 3.8+
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)
- [scikit-fuzzy](https://pythonhosted.org/scikit-fuzzy/)

## 🔧 Instalação
Clone o repositório:
```bash
git clone https://github.com/vitor-souza-ime/fuzzy.git
cd fuzzy
````

Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

> Caso não exista o `requirements.txt`, instale manualmente:

```bash
pip install numpy matplotlib scikit-fuzzy
```

## ▶️ Execução

No terminal, execute:

```bash
python main.py
```

No Google Colab:

```python
!pip install scikit-fuzzy
!python main.py
```

## 📚 Referências

* Mamdani, E. H., & Assilian, S. (1975). *An experiment in linguistic synthesis with a fuzzy logic controller*. International Journal of Man-Machine Studies, 7(1), 1–13.
* [Documentação do scikit-fuzzy](https://pythonhosted.org/scikit-fuzzy/)


