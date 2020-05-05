# Ajuste de Curva Polinomial
input: x
variavel alvo: t

f(x) = sin(2xPI)

Overfitting: quando a curva do modelo acerta todos os dados de treino, porem possui uma ma representacao da funcao f(x)



## Atividade Pratica
Funcao para separar os dados em treino e teste
```python
def get_datasets(data):
    train = {'x': [], 'y': []}
    test  = {'x': [], 'y': []}

    for i in range(len(data)):
        if i%2 == 0:
            train['x'].append(i)
            train['y'].append(data[i])
        else:
            test['x'].append(i)
            test['y'].append(data[i])
    train['y'].reverse()
    test['y'].reverse()
    return train, test
```
maior erro = 8?

Opcao para Hold-Out: Kennard-Stone
    pega as amostras mais representativas


