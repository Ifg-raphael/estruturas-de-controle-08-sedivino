# Sua solução aqui
'''
# Exercício - Lógica de Programação com Python
## Lista 03 - Exercício 08
Tendo como dados de entrada a altura e o sexo de uma pessoa (“M” masculino e “F” feminino), construa um
algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
- para homens: (72.7*altura)-58
- para mulheres: (62.1*altura)-44.7

O programa deve assumir que a entrada e saída seja exatamente no formato dado nos exemplos a seguir. 
**Não adicione outras mensagens ou mude a capitalização das letras pois se fizer isso o teste não passará!**

---

**Exemplo 01:**

Entrada:
```
1.60 M
```
Saída:
```
58.32
```
 '''

altura, sexo = input().split()
altura = float(altura)

if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
elif sexo == "F":
    peso_ideal = (62.1 * altura) - 44.7

print(f"{peso_ideal:.2f}")

