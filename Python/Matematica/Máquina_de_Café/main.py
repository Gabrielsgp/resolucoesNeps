# Solução para: Máquina de Café
# Link: https://neps.academy/br/exercise/95

def main():
    # primeiro exercicio medio que parece dificil mais e que nem um problema de enem sei so saber
    #traduzir
    #vamos receber as pessoas nos andares primeiro 
    
    primeiroAndar = int(input())
    segundoAndar = int(input())
    terceiroAndar = int(input())
    
    #eu sabendo a quantidade de pessoas por andar posso calcular o tempo gasto baseado onde a maquina esta 
    # por isso vou fazer um dicionario para por os minutos gastos com maquina em cada andar 
    valores = {'maqAndar3':0,'maqAndar2':0,'maqAndar1':0}
    #eu calculei individualmente a quantidade de minutos gastos com a maquina em cada andar
    valores['maqAndar3'] = (segundoAndar*2)+(primeiroAndar*4)    #as contas mudao pois em certos
    valores['maqAndar2'] = (primeiroAndar*2)+(terceiroAndar*2)  # andares se gasta 4 mins ida e volta                                                                                                        
    valores['maqAndar1'] = (segundoAndar*2)+(terceiroAndar*4)    # em outros se gasta 2 mins 
    #so printei o menor valor do dicionario apos os calculos 
    print(min(valores.values()))

    # E MEIO VERBOSO E NAO FUNCIONARIA EM UM CONTEXTO MAIOR  EM UM PREDIO COM 20 ANDARES POR EXEMPLO MAIS EU SIGO A LINHA DO EXERCICIO E TENTO FAZER MAIS LEGIVEL POSSIVEL 
if __name__ == "__main__":
    main()