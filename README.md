# Regressão Logística para Previsão de Crash

Projeto de aprendizado de máquina que usa métricas de hardware para prever se ocorrerá um crash (`status_crash`). O modelo utilizado é uma regressão logística com padronização das variáveis numéricas.

## Tecnologias

- Python 3
- Pandas
- NumPy
- Scikit-learn

## Estrutura do projeto

```text
.
├── data/
│   └── base_hardware.csv
├── src/
│   └── main.py
├── requirements.txt
└── README.md
```

## Dados

O arquivo `data/base_hardware.csv` contém as variáveis usadas pelo modelo:

| Coluna | Descrição |
| --- | --- |
| `uso_cpu_percent` | Percentual de uso da CPU |
| `uso_ram_percent` | Percentual de uso da memória RAM |
| `uso_gpu_percent` | Percentual de uso da GPU |
| `uso_disco_percent` | Percentual de uso do disco |
| `temperatura_c` | Temperatura do sistema em graus Celsius |
| `status_crash` | Variável-alvo: `0` para ausência de crash e `1` para crash |

## Como executar

### 1. Criar e ativar o ambiente virtual

No Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Caso a política de execução do PowerShell bloqueie a ativação, execute antes:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

### 2. Instalar as dependências

```powershell
python -m pip install -r requirements.txt
```

### 3. Executar o modelo

A partir da raiz do projeto:

```powershell
python src/main.py
```

O programa exibe:

- A acurácia do modelo;
- A matriz de confusão;
- O relatório de classificação, com precisão, recall e F1-score.

## Metodologia

1. Carregamento da base de hardware com Pandas.
2. Separação das variáveis preditoras e da variável-alvo `status_crash`.
3. Divisão dos dados em treino e teste, usando 30% para teste e `random_state=42`.
4. Padronização das variáveis com `StandardScaler`.
5. Treinamento de uma `LogisticRegression`.
6. Avaliação das previsões com métricas de classificação.

## Observações

- Execute o comando a partir da raiz do projeto para que o caminho `data/base_hardware.csv` seja encontrado corretamente.
- O conjunto de dados e os resultados são destinados a fins educacionais e experimentais.
