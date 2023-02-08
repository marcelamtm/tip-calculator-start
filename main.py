#Projeto: Day 2 - 100 Days of Code, By Angela.
#Minha versão:
print("Bem-vindo à calculadora de gorjetas.")
conta = float(input("Qual é a conta total? $"))
gorjeta = int(input("Que porcentagem você gostaria de dar? 10, 12 ou 15? "))
divisão = int(input("Quantas pessoas para dividir a conta? "))

porcentagem = int(gorjeta) / 100
v_total = conta * porcentagem
v_total = conta + v_total #ou round(v_total, 2)
v_total /= divisão

print("Cada pessoa deve pagar: $" + str(round(v_total, 2)))
# ou print(f"Cada pessoa deve pagar: ${v_total}")

#Substituindo o v_total por round(v_total, 2), na linha 10, deve-se printar como no comentário da linha 14. Caso contrário, dará erro.

#Versão de Angela:
#print("Welcome to the tip calculator!")
#bill = float(input("What nas the total bill? $"))
#tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
#people = int(input("How many people to split the bill? "))

#tip_as_percent = tip / 100
#total_tip_amount = bill * tip_as_percent
#total_bill = bill + total_tip_amount
#bill_per_person = total_bill / people
#final_amount = round(bill_per_person, 2)
#print(f"Each person should pay ${final_amount}")