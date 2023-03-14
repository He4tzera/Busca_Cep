from Api import consulta

while True:
    print("Seja bem vindo ao Busca Cep:)")
    print("Insira o cep:")
    cep = input()
    consulta(cep)
    #O usuario informa se deseja consultar outro cep ou não
    print("Deseja consultar outro cep ?")
    print("Y/N")
    resposta_usu = input().lower()
    #if para caso o usuario não queira consultar outro cep
    if resposta_usu == "n":
        print("Obrigado por usar nosso sistema:")
        break


