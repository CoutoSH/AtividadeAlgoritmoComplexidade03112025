"""
Algoritmo de Complexidade Constante - O(1)
==========================================

Este algoritmo demonstra operações que sempre levam o mesmo tempo
independentemente do tamanho da entrada. A complexidade é O(1).

Exemplo: acessar um elemento em uma lista por índice ou buscar um valor
em um dicionário pela chave.
"""

def acesso_direto(lista, indice):
    """
    Retorna o elemento de uma lista pelo índice.

    Args:
        lista (list): Lista de elementos.
        indice (int): Índice do elemento desejado.

    Returns:
        O elemento na posição especificada.

    Complexidade:
        O(1) - Constante:
        - O tempo de execução não depende do tamanho da lista.
        - Acesso direto por meio do índice.
    """
    # Acesso direto ao elemento - O(1)
    return lista[indice]


def busca_valor_dicionario(dicionario, chave):
    """
    Retorna o valor de um dicionário pela chave.

    Args:
        dicionario (dict): Dicionário com pares chave-valor.
        chave: Chave a ser pesquisada.

    Returns:
        O valor associado à chave ou None se ela não existir.

    Complexidade:
        O(1) - Amortizado para operações em dicionário.
    """
    # Acesso direto ao valor pela chave - O(1) amortizado
    return dicionario.get(chave)


if __name__ == "__main__":
    # Exemplo 1: Acesso direto a lista
    minha_lista = [10, 20, 30, 40, 50]
    elemento = acesso_direto(minha_lista, 2)  # Acessa o índice 2 (valor 30)
    print(f"Elemento na posição 2: {elemento}")

    # Exemplo 2: Acesso a dicionário
    meu_dict = {"a": 1, "b": 2, "c": 3}
    valor = busca_valor_dicionario(meu_dict, "b")
    print(f"Valor da chave 'b': {valor}")

    # Demonstração de que o tempo é constante
    import time

    print("\nTestando tempos de acesso para diferentes tamanhos de lista:")
    for tamanho in [100, 10_000, 1_000_000]:
        grande_lista = list(range(tamanho))

        inicio = time.perf_counter()
        acesso_direto(grande_lista, tamanho // 2)  # Acessa o elemento do meio
        fim = time.perf_counter()

        print(f"Tamanho {tamanho:>8}: {fim - inicio:.10f} segundos")

    print("\nIndependentemente do tamanho da lista, o tempo de acesso é constante!")
    print("Isso ocorre porque o acesso por índice é uma operação O(1).")
