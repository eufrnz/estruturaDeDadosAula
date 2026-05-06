def somaVetor(v, n):
   if(n == 0):
       return v[n]
   else: 
       return v[n] + somaVetor(v, n - 1)

def main():
    n = input()
    print("Entre com os numeros")
    v = []
    for i in range(n):
        numero = int(input(f"Numero (i + 1): "))
        v.append(numero)
    
    resultado = somaVetor(v, n - 1)
    print(f"Resultado = {resultado}")
    
if __name__ == "__main__":
    main()