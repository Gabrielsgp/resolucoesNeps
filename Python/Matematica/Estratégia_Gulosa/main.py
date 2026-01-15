def main():
    #vamos la eu ja resolvi um exercicio parecido 
    #so ir checando se os numeros grandes cabem
    #acho que o proprio nome do exericicio fala a estrategia e
    #estrtegia gulosa so pegar o maior numero nao funcionar com outras moedas 
    #vou ter somente uma entrada  o valor
    Valor =  int(input())
    #vou declarar uma sobra e simples quanto daquele numero cabe no 
    #valor entende
    sobra = 0
    quantidade = 0
    #vou usar uma lista mesmo deve ter outra estrutara que ia 
    #que ia ser mais rapida  
    lista = [1,5,10,25,50,100]
    #fiz hardcoded assim o codigo fica mais rapido vou deixar o loop mais abaixo 
    quantidade += Valor//100
    sobra = Valor%100

    quantidade += sobra//50
    sobra = sobra%50
        
    quantidade += sobra//25
    sobra = sobra%25

    quantidade += sobra//10
    sobra = sobra%10
    
    quantidade += sobra//5
    sobra = sobra%5

    quantidade += sobra//1
    sobra = sobra%1

    print(quantidade)
    


    #como seria com o  loop
    '''for moeda in moedas:
        # Quantas moedas desse valor cabem?
        qtd_desta_moeda = valor // moeda
        
        # Adiciona ao total
        quantidade_total += qtd_desta_moeda
        
        # Atualiza o valor para ser o resto (o que sobrou)
        valor = valor % moeda'''
if __name__ == "__main__":
    main()
