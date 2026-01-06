# Solução para: Insensibilidade
# Link: https://neps.academy/br/exercise/316

def main():
    # o exercicio pede a soma dos quadrados das distnacias entao so preciso calculalos
    # e usar o sum na lista deles para descobrir por isso a lista abaixo
    listaComOsquadrados = []
    #agora vou fazer uma funçao que faz os calculo do quadrado da distancia
    #como o exercicio me da um numero fixo a cada entrada ou seja uma lista
    #com 4 indices fica facil de resolver busquei mais clareza na funçao 
    # deve que dava pra fazer com menos codigo mais achei assim legivel
    def calcularInsensibilidade(lista):
        distancia1 = lista[0] - lista[2] 
        distancia2 = lista[1] - lista[3]
        listaComOsquadrados.append(distancia1*distancia1)
        listaComOsquadrados.append(distancia2*distancia2)
    #ok vou começar pegando o numero de entradas isso importante pois dita
    #quantas entradas vou ter e quantas vezes vou usar minha funçao ou
    #e numero de interaçoes no loop 
    numerodeEntradas = int(input())
    #agora vou pegar  cada uma das entradas e fazer as operaçoes nelas
    #primeiro eu pego a string 
    #usei uma listcompr para passar os indices para int
    #usei a funçao que ira a cada iteraçao do loop executar a funçao 
    #que ja adiciona n lista os quadrados 
    for i in range(numerodeEntradas):
        valores = input() #pegamos uma string 
        valores = [int(i) for i in valores.split()] #list comprension 
        calcularInsensibilidade(valores)
    #agora so printar a soma dos quadrados 
    print(sum(listaComOsquadrados))
    #NOT APOS EU ANALISAR O CODIGO  POR MAIS QUE FUNCIONE NAO ESCALA POIS 
    # O NUMERO DE OPERAÇOES NA FUNÇAO ESCALA COM TIPO DE ENTRADA OU SEJA DEIXA (O)n
    # PARA RESOLVER EU TERIA QUE  RETIRAR A PRIMEIRA LISTA DO CODIGO E FAZER COM O UM CONTADOR 
      
        
    

if __name__ == "__main__":
    main()
