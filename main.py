def farenhait(c):
    conv= (c *9/5) +32
    return conv
def Celsius(f):
    conv = (f - 32) * 5/9
    return conv
def menu():
    while True:
       print("***** Conversor de temperatura *****\n")
       print("Opções\t")
       print("1 - De Fahrenheit para Celsius :")
       print("2 - De Celsius para Fahrenheit :")
       print("0 - Sair :")
       opcao = int(input("Digite uma das opções acima ?\n"))
       if opcao == 1:
           c = float(input("Digite a temperatura em °c ?\n"))
           conver = farenhait(c)
           print("A temperatura em Fahrenheit é {} F\n". format(conver))
       elif opcao == 2:
           c = float(input("Digite a temperatura em F ?\n"))
           conver = Celsius(c)
           print("A temperatura em Celsius é {} °C\n". format(conver))
       elif opcao == 0:
            print(" Obrigado! Até mais. ")
            break


menu()