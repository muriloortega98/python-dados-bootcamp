#nome, salario, e % bonus
#retorna o valor do bonus
# 1000 + salario * bonus

VALOR_BONUS = 1000

nome = input("Qual seu nome? ")
salario = float (input("Qual seu salario? "))
perc_bonus = float (input("Qual seu percentual do bonus? "))

#calcula o bonus
bonus_base = (salario * perc_bonus) 
bonus_final = VALOR_BONUS + bonus_base

#retorna o resultado para o usuario
print(f"Ola {nome}. Seu bonus será de {bonus_final:,.2f} reais")


