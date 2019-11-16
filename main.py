"""Calculadora em Python
Tem um pequeno menu de ajuda quando solicitado e a opção de sair
José Feiteira
"""
import re


# Função Principal da aplicação
def main():
    #Expressão regular apenas aceita numeros inteiros e as 4 operações básicas
    reg_expression = re.compile("^\\s*(\\d+\\s*[+|-|/]\\s*)*\\d+$")
    print ("Se necessitar de ajuda, digite 'Ajuda'; Se quiser sair digite 'Sair'")
    print("Insira a conta que quer realizar:")
    while True:
        user_input = input("->").strip().lower()
        if user_input == "ajuda":
            ajuda()
        elif user_input == "sair":
            break
        elif reg_expression.match(user_input):
             print(user_input.lstrip().rstrip() + " = " + str(eval(user_input)))
        else:
            print(user_input + " = " + str(eval(user_input)))
            print("Expressão Inválida!")

def ajuda():
    print("Operações que pode realizar:")
    print("Somar -> +")
    print("Subtrair -> -")
    print("Multiplicar -> *")
    print("Dividir -> /")

"""Este if indica que só vai correr o main se for módulo principal"""
if __name__ == '__main__':
    main()
