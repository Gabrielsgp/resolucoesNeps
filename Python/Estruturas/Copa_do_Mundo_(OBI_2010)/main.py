# Solução para: Copa do Mundo (OBI 2010)
# Link: https://neps.academy/br/exercise/276

def main():
    # ok esse exercicio tem muitas entradas 
    # vou fazer uma lista com as letras 
    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
    #agora vou fazer um loop para conferir os resultados e retira os perdedores 
    #como sei que sera 15 jogos for serve
    #vou usar  a lista como uma fila o time que ganha vai para o final sempre pego os dois primeiros 
    for i in range(15):
        jogo = [int(i) for i in input().split()]
        time1 = letras.pop(0) # o pop retorna o valor entao e so adicionar o maior entre os
        time2 = letras.pop(0) # dois primeiros no final da fila 

        if jogo[0] > jogo[1]:
            letras.append(time1)
        else:
             letras.append(time2)
        
    
    print(letras[0])
if __name__ == "__main__":
    main()
