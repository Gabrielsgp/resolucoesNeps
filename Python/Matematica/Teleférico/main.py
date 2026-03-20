# Solução para: Teleférico
# Link: https://neps.academy/br/exercise/15

def main():
    # beleza o exercicio tenta esconder mais e os monitor que vale
    # duas entrada facil 
    capacidadeDaCabine = int(input())
    tamanhoDaTurma = int(input())
    numeroDeViagems = 0
    # vou sempre mandar o numero maximo -1 que e o instrutor 
    while tamanhoDaTurma > 0:
        tamanhoDaTurma -= (capacidadeDaCabine-1)
        #aumento a quantidade viagems a cada interação do loop
        numeroDeViagems+=1
        
    print(numeroDeViagems)
    #exercicio bem facinho podia por muito facil nele
if __name__ == "__main__":
    main()
