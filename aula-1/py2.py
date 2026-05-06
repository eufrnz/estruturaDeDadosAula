def exibe_invertido(mensagem, tamanho):
    if(tamanho >= 0):
        print(mensagem[tamanho], end="")
        exibe_invertido(mensagem, tamanho - 1)
        
def main():
    print("Forneça a mensagem")
    mensagem = input("Digite a mensagem: ")
    tamanho = len(mensagem) - 1
    print("Mensagem invertida: ")
    exibe_invertido(mensagem, tamanho)
    print()
    
if __name__ == "__main__":
    main()