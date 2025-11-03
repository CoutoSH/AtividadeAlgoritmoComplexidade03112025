"""
Algoritmo de Complexidade Linear - O(n)
=======================================

Este algoritmo demonstra operações cujo tempo de execução cresce
linearmente com o tamanho da entrada. A complexidade é O(n).

Exemplo: busca linear em uma lista.
"""

def busca_linear(lista, valor):
    """
    Busca um valor em uma lista usando o método de busca linear.
    
    Args:
        lista (list): Lista de elementos.
        valor: Valor a ser pesquisado.
    
    Returns:
        int: Índice do valor na lista ou -1 se não encontrado.
    
    Complexidade:
        O(n) - Linear
        - No pior caso, todos os elementos precisam ser verificados.
        - O tempo de execução é proporcional ao tamanho da lista.
    """
    for i, elemento in enumerate(lista):
        if elemento == valor:
            return i  # Retorna o índice onde o valor foi encontrado
    return -1  # Valor não encontrado


def soma_elementos(lista):
    """
    Calcula a soma de todos os elementos de uma lista.
    
    Args:
        lista (list): Lista de números.
    
    Returns:
        float: Soma de todos os elementos.
    
    Complexidade:
        O(n) - Linear
        - Cada elemento da lista é visitado exatamente uma vez.
        - O tempo de execução é proporcional ao tamanho da lista.
    """
    soma = 0
    for elemento in lista:
        soma += elemento
    return soma


def encontrar_maximo(lista):
    """
    Encontra o elemento máximo em uma lista.
    
    Args:
        lista (list): Lista de números.
    
    Returns:
        O elemento máximo da lista ou None se estiver vazia.
    
    Complexidade:
        O(n) - Linear
        - Cada elemento da lista é comparado uma vez.
        - O tempo de execução é proporcional ao tamanho da lista.
    """
    if not lista:
        return None
    
    maximo = lista[0]
    for elemento in lista[1:]:
        if elemento > maximo:
            maximo = elemento
    return maximo


if __name__ == "__main__":
    # Exemplo 1: Busca linear
    minha_lista = [64, 34, 25, 12, 22, 11, 90]
    valor_buscado = 22
    indice = busca_linear(minha_lista, valor_buscado)
    
    if indice != -1:
        print(f"Valor {valor_buscado} encontrado no índice {indice}.")
    else:
        print(f"Valor {valor_buscado} não encontrado.")
    
    # Exemplo 2: Soma de elementos
    soma = soma_elementos(minha_lista)
    print(f"Soma dos elementos: {soma}")
    
    # Exemplo 3: Encontrar máximo
    maximo = encontrar_maximo(minha_lista)
    print(f"Elemento máximo: {maximo}")
    
    # Demonstração de crescimento linear
    import time
    
    print("\nDemonstração de crescimento linear:")
    for tamanho in [1_000, 2_000, 4_000, 8_000]:
        lista_teste = list(range(tamanho))
        
        inicio = time.perf_counter()
        soma_elementos(lista_teste)  # Executa a função O(n)
        fim = time.perf_counter()
        
        tempo_gasto = fim - inicio
        print(f"Tamanho: {tamanho:6d} | Tempo: {tempo_gasto:.6f}s | Tempo médio por elemento: {tempo_gasto / tamanho:.10f}s")
    
    print("\nObserve que, ao dobrar o tamanho da entrada, o tempo de execução tende a dobrar também.")
    print("Isso caracteriza uma complexidade linear O(n).")
