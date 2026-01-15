# Solução para: Pares ou com Último Algarismo Igual a 5
# Link: https://neps.academy/br/exercise/177

def main():
    # eu estou meio fraco em dicionarios entao vou pegar um exercicios 
    #mais faceis pra treinar dicionarios 

    #esse exercicio e mamao vou declarar o dicionario
    dicio = {}

    #for para preencher o dicionario 
    for i in range(3):
        valor = int(input())
        dicio[i] = valor
    #usei filter com lambda simples aqui ele vai filtrar o numero
    #que for par ou termina com 5 transformei em string para conferir
    #se termina com 5 
    
    valores = list(filter(lambda x: x%2 == 0 or x%10 == 5 ,dicio.values()))
    print(len(valores))
    

    
    
            
if __name__ == "__main__":
    main()
