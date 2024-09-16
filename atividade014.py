# Crie um programa que receba três notas de um aluno e calcule a média. Informe se o aluno foi aprovado, reprovado ou se está de recuperação. Use as seguintes regras:
# Média ≥ 7: Aprovado
# 5 ≤ Média < 7: Recuperação
# Média < 5: Reprovado
val=float(input("insira a primeira nota:"))
val2=float(input("insira a segunda nota:"))
val3=float(input("insira a terceira nota:"))

p=(val+val2+val3)/3
if (p>=7):
    print("aprovado")
elif(p<=5) and (p<7):
    print("recuperação")
elif (p<5):
    print("reprovado")