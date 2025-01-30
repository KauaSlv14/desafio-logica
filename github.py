nome=input("digite o nome do herói: ")
xp=int(input("Digite o nivel do heroi")) 
if xp <1000: 
  nivel=  ("ferro")
elif xp>=1001 and xp <=2000:
  nivel= ("Bronze") 
elif xp >=2001 and xp <=5000:
   nivel=("Prata") 
elif xp >=50001 and xp <=7000: 
  nivel=("Ouro") 
elif xp >= 7001 and xp <=8000:
   nivel=("platina") 
elif xp>= 8001 and xp <=9000: 
  nivel =("Ascendente") 
elif xp >=9001 and xp >=1000:
    print ("imortal") 
else:
    nivel =print("Radiante")
print("O heroi de nome", nome,"esta mo nível de ", nivel) 