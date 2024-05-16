frutas=["pepino","pepino","naranja","zanahoria","zanahoria","zanahoria","banano","banano","banano"]
contador=int
consulta=
for fruta in frutas:
    consulta=input("Ingrese el nombre de la fruta a consultar...:")
    if consulta==fruta:
        contador+=1
        print("La cantidad de ", consulta, "es de ",  contador)