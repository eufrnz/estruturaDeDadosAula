def divide(a,b):
    if(a < b): 
        return 0
    else:
        return 1 + divide(a - b, b)
    
def main():
    print("Forneça valores para a e b:")
    
    a= int(input("Divide o valor de a (dividendo): "))
    b= int(input("Divide o valor de b (divisor): "))
    resultado = divide(a,b)
    print(f"Resultado = {resultado}")
   
    
if __name__ == "__main__":
    main()