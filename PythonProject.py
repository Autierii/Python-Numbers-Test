import random

def ordenar_numeros(numeros, ordem):
    if ordem == 1:
        numeros.sort()
    elif ordem == 2:
        numeros.sort(reverse=True)
    elif ordem == 3:
        random.shuffle(numeros)
    return numeros

def main():
    numeros = []
    
    print("Digite os números desejados. Digite 'sair' para parar.")

    while True:
        num = input("Digite um número ou 'sair': ")
        if num.lower() == 'sair':
            break
        try:
            numeros.append(int(num))
        except ValueError:
            print("Opção inválida. Por favor, insira apenas números.")
            continue

    while True:
        ordem = input("Escolha a ordem (1 - Crescente, 2 - Decrescente, 3 - Aleatório): ")
        if ordem in ['1', '2', '3']:
            numeros_ordenados = ordenar_numeros(numeros.copy(), int(ordem))
            print("Números ordenados:", numeros_ordenados)
        else:
            print("Opção inválida. Por favor, escolha novamente.")
            continue

        continuar = input("Deseja continuar? (s/n): ")
        if continuar.lower() != 's':
            break

if __name__ == "__main__":
    main()
