# Solução para: Ordenação Simples
# Link: https://neps.academy/br/exercise/400

def main():
    # ordenaçao simples eu poderia usar um sort do proprio phython
    #mais cade a graça nisso um algoritimo de ordenaçao simples tbm 
    #resolveria porem vou fazer um quicksort

    #vou declarar lista desordenada primeiro
    listaDesordenada = []
    #ok como o exericicio me diz que serao sempre dez numeros 
    for i in range(10):
        num = int(input())
        listaDesordenada.append(num)
    #vou fazer de forma recursiva achoo mais legivel
    #nao me aprofundar muito no quicksort vou resumir nos dividimos
    #o array em arrays menores mais faceis de ordenar isso chama DC
    
    def quicksort(lista):
        if len(lista)<2:  #checando o tamanho do array caso recursivo
            return lista  #caso recursivo 
        else:
            pivo = lista[0] #provavel ter um pivo mais rapido vou no 0 mesmo
            menores = [i for i in lista[1:]if i <= pivo] # o array com todos numeros menores que o pivo
            maiores = [i for i in lista[1:]if i > pivo] # aray com o numeros maiores com pivo 
            return quicksort(menores) + [pivo] + quicksort(maiores) 
            #encima ja e a chamada recursiva ou seja ele vai rodar a funçao no array
            #ate ele ficar com um ou dois  e entrar no caso recursivo
    listaOrdenada = quicksort(listaDesordenada)
    #inveti a lista para ordem decrescente
    listaDecresente = listaOrdenada[::-1]
    #agora vou passar para string achei assim mais legivel
    listaString = ' '.join(map(str,listaOrdenada))
    listaStringDecre = ' '.join(map(str,listaDecresente))
    #agora e so printar 
    print(listaString)
    print(listaStringDecre)
    
if __name__ == "__main__":
    main()
