#Capital Inicial 
#c = 0
#Taxa de juros
#i = 0
#Tempo
#t = 0
#Montante
#m = 0

def calcular_juros(juro):
    while True:
        c = input("\nQual o capital inicial? ")
        if not c.isdigit():
            print("Apenas números são permitidos. Tente novamente.")
            continue
        c = float(c)
        break

    while True:
        i = input("\nQual a taxa de juros? ")
        if not i.isdigit():
            print("Apenas números são permitidos. Tente novamente.")
            continue
        i = float(i)/100
        break

    while True:
        t = input("\nAo decorrer de quantos anos? ")
        if not t.isdigit():
            print("Apenas números são permitidos. Tente novamente.")
            continue
        t = float(t)
        break

    if juro == 1:
        m = c*(1+i*t)
    else:
        m = c*(1+i)**t

    palavraAno = "ano" if t == 1 else "anos"
    print(f"O valor acumulado no período de {t} {palavraAno}, equivale a: {m:.2f} reais.")

def main():
    print("Calculadora de Juros:")
    print("1. Juros Simples")
    print("2. Juros Composto")
    print("3. Sair")

    while True:
        juros = input("Escolha uma opção: ")

        if not juros.isdigit():
            print("Apenas números são permitidos. Tente novamente.")
            continue

        juros = int(juros)

        if juros < 1 or juros > 3:
            print("Apenas números entre 1 e 3 são permitidos. Tente novamente.")
            continue

        match juros:
            case 1:
                calcular_juros(1)
            case 2:
                calcular_juros(2)
            case 3:
                print("Saindo...")
                break



main()
