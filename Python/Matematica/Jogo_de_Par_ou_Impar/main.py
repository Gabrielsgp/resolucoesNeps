# Solução para: Jogo de Par ou Impar
# Link: https://neps.academy/br/exercise/51

def main():
    #primeiro vou setar os inputs acho que fazer um for so pra 3 
    #inputs nao rende vou colocar 3 inputs crus 
    lados_escolhidos = int(input())
    #antes de receber o outros inputs vou declarar o jogadores como
    #como e par e impar booleano resolve vai começar os dois com false
    Alice = False
    Bob = False
    #agora preciso arumar que e par e quem e impar 
    if lados_escolhidos == 0:
        Alice = True
        Bob = False
    else:
        Alice = False
        Bob = True
    # se 0 entao alice pego par se der 1 bob pegou par
    
    #agora receber os numeros 
    maoAlice= int(input())
    maobob = int(input())
    
    #agora o resultado se e par ou impar
    resultado = (maoAlice + maobob)%2
    #agora e so fazer ums condicionais para saber quem ganhou 
    if resultado == 0 and Alice == True:
        print(0)
    elif resultado == 0 and Bob == True:
        print(1)
    elif resultado == 1 and Alice == False:
        print(0)
    elif resultado == 1 and Bob == False:
        print(1)
    


# ---------------------------------------------------------
# SOLUÇÃO OTIMIZADA (V2)
# Notas: Usa comparação direta de paridade.
# ---------------------------------------------------------
def solucao_otimizada():
    p = int(input())
    d1 = int(input())
    d2 = int(input())
    
    # Se a escolha (P) for igual ao resto da soma, a resposta é 0 (Alice)
    # Caso contrário, é 1 (Bob).
    if p == (d1 + d2) % 2:
        print(0)
    else:
        print(1)

# ---------------------------------------------------------
# EXECUÇÃO
# ---------------------------------------------------------
if __name__ == "__main__":
    # solucao_inicial()  # Comentado para não rodar
    solucao_otimizada()  # Rodando a melhor versão
