print("Avaliação de Risco de Diabetes Tipo 2")


# Coletando sintomas
sintomas = 0
while True:
    sede = input(" Você tem sede excessiva? (s/n): ").strip().lower()
    if sede in ['s', 'n']:
        if sede == 's':
            sintomas += 1
        break
    else:
        print("Responda com 's' para sim ou 'n' para não.")


while True:
    fome = input("Você tem fome excessiva? (s/n): ").strip().lower()
    if fome in ['s', 'n']:
        if fome == 's':
            sintomas += 1
        break
    else:
        print("Responda com 's' para sim ou 'n' para não.")


while True:
    urinar = input("Você urinar frequentemente? (s/n): ").strip().lower()
    if urinar in ['s', 'n']:
        if urinar == 's':
            sintomas += 1
        break
    else:
        print("Responda com 's' para sim ou 'n' para não.")


while True:
    perda_peso = input("Você tem perda de peso inexplicável? (s/n): ").strip().lower()
    if perda_peso in ['s', 'n']:
        if perda_peso == 's':
            sintomas += 1
        break
    else:
        print("Responda com 's' para sim ou 'n' para não.")


# Coletando fatores de risco
fatores_risco = 0
while True:
    historico = input("Histórico familiar de diabetes? (s/n): ").strip().lower()
    if historico in ['s', 'n']:
        if historico == 's':
            fatores_risco += 1
        break
    else:
        print("Responda com 's' para sim ou 'n' para não.")


while True:
    sedentario = input("Você tem estilo de vida sedentário? (s/n): ").strip().lower()
    if sedentario in ['s', 'n']:
        if sedentario == 's':
            fatores_risco += 1
        break
    else:
        print("Responda com 's' para sim ou 'n' para não.")


while True:
    sobrepeso = input("Sobrepeso ou obesidade? (s/n): ").strip().lower()
    if sobrepeso in ['s', 'n']:
        if sobrepeso == 's':
            fatores_risco += 1
        break
    else:
        print("Responda com 's' para sim ou 'n' para não.")


# Coletando glicemia
while True:
    try:
        glicemia = float(input("Glicemia em jejum (mg/dL): ").strip())
        break
    except ValueError:
        print("Digite um número válido.")


# Avaliação de risco
if glicemia > 126 or (fatores_risco >= 2 and sintomas >= 2):
    print("Alto risco de Diabetes Tipo 2")
elif (fatores_risco >= 1 and sintomas >= 1) or glicemia >= 100:
    print("Moderado risco de Diabetes Tipo 2")
else:
    print("Baixo risco de Diabetes Tipo 2")