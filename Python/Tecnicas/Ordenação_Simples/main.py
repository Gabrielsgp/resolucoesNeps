# Solução para: Ordenação Simples
# Link: https://neps.academy/br/exercise/176

def main():
    # eu poderia usar um sort do phyton aqui mais ai cade 
    # a graça vou ordenar essa lista com um quicksort
    #primeiro vou declarar  o numero de elementos do array 
    # eu nao vou usar mais tenho que declarar 
    entrada1 = int(input())
    lista = [int(i) for i in input().split()]
    #entao vamos la quicksort
    # vou fazer de forma recursiva gasta mais memoria mas vai servir
    def quicksort(array):
        if len(array)<2: 
            return array
        else:
            #vamos definir o pivo vou por o primeiro item como pivo 
            #vai aumentar o temp do algoritimo mas ta comoo limite e 10 a4 ta de boa
            pivo = array[0]
            menores = [i for i in array[1:] if i <= pivo] # faz uma lista 
            maiores = [i for i in array[1:] if i > pivo]
            return quicksort(menores)+[pivo] + quicksort(maiores)
    
    print(" ".join([str(i) for i in quicksort(lista)]))
        
        
    
    
    

if __name__ == "__main__":
    main()
