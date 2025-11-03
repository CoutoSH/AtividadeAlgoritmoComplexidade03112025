"""
Algoritmo de Complexidade Quadrática - O(n^2)
=============================================

Este algoritmo demonstra operações cujo tempo de execução cresce
quadraticamente com o tamanho da entrada. A complexidade é O(n^2).

Exemplos: algoritmo de ordenação Bubble Sort, verificação de duplicados
e busca de pares cuja soma é igual a um valor alvo.
"""

def bubble_sort(lista):
    """
    Função que ordena uma lista usando o algoritmo Bubble Sort.
    
    Args:
        lista (list): Lista de elementos a serem ordenados.
    
    Returns:
        list: Lista ordenada em ordem crescente.
    
    Complexidade: O(n^2) - Quadrática
        - Usa dois loops aninhados.
        - No pior caso, cada elemento é comparado com quase todos os outros.
        - Número total de comparações: n * (n - 1) / 2 ≈ n^2 / 2.
    """
    n = len(lista)
    # Faz cópia da lista para não modificar a original
    lista_ordenada = lista[:]
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_ordenada[j] > lista_ordenada[j + 1]:
                # Troca os elementos
                lista_ordenada[j], lista_ordenada[j + 1] = (
                    lista_ordenada[j + 1],
                    lista_ordenada[j],
                )
    
    return lista_ordenada


def busca_duplicados(lista):
    """
    Função que verifica se há elementos duplicados em uma lista.
    
    Args:
        lista (list): Lista de elementos.
    
    Returns:
        bool: True se houver duplicados, False caso contrário.
    
    Complexidade: O(n^2) - Quadrática (no pior caso)
        - Usa dois loops aninhados.
        - Cada elemento é comparado com todos os que vêm depois dele.
    """
    n = len(lista)
    for i in range(n):
        for j in range(i + 1, n):
            if lista[i] == lista[j]:
                return True
    return False


def encontrar_pares_soma(lista, alvo):
    """
    Função que encontra todos os pares de elementos cuja soma é igual a um valor alvo.
    
    Args:
        lista (list): Lista de números.
        alvo (int | float): Valor alvo para a soma.
    
    Returns:
        list[tuple]: Lista de tuplas contendo os pares que somam o valor alvo.
    
    Complexidade: O(n^2) - Quadrática
        - Usa dois loops aninhados para comparar todos os pares possíveis.
    """
    pares = []
    n = len(lista)
    
    for i in range(n):
        for j in range(i + 1, n):
            if lista[i] + lista[j] == alvo:
                pares.append((lista[i], lista[j]))
    
    return pares


# Exemplo de uso
if __name__ == "__main__":
    # Exemplo 1: Bubble Sort
    lista_desordenada = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", lista_desordenada)
    lista_ordenada = bubble_sort(lista_desordenada)
    print("Lista ordenada:", lista_ordenada)
    
    # Exemplo 2: Busca de duplicados
    lista_com_duplicados = [1, 2, 3, 4, 2, 5]
    lista_sem_duplicados = [1, 2, 3, 4, 5]
    
    print(f"\nLista {lista_com_duplicados} tem duplicados? {busca_duplicados(lista_com_duplicados)}")
    print(f"Lista {lista_sem_duplicados} tem duplicados? {busca_duplicados(lista_sem_duplicados)}")
    
    # Exemplo 3: Encontrar pares com soma específica
    lista = [1, 2, 3, 4, 5, 6]
    alvo = 7
    pares = encontrar_pares_soma(lista, alvo)
    print(f"\nPares em {lista} que somam {alvo}: {pares}")
    
    # Demonstração de crescimento quadrático
    import time
    
    print("\nDemonstração de crescimento quadrático:")
    print("Comparando tempo de execução para diferentes tamanhos de entrada:")
    
    for tamanho in [100, 200, 400]:
        # Cria uma lista com tamanho n (lista reversa para pior caso)
        lista_teste = list(range(tamanho, 0, -1))
        
        inicio = time.time()
        bubble_sort(lista_teste)
        fim = time.time()
        
        tempo_gasto = fim - inicio
        print(
            f"Tamanho: {tamanho:3d} | "
            f"Tempo: {tempo_gasto:.6f}s | "
            f"Tempo/n²: {tempo_gasto / (tamanho ** 2):.10f}"
        )
    
    print("\nObserve que ao dobrar o tamanho da entrada, "
          "o tempo de execução tende a aumentar aproximadamente 4 vezes (2² = 4).")
    print("Isso caracteriza uma complexidade quadrática O(n^2).")
    print("\nA razão tempo/n² tende a se manter aproximadamente constante, "
          "confirmando a natureza quadrática do algoritmo.")
