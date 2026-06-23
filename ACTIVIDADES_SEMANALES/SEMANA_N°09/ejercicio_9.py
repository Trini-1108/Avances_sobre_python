# Una panadería vende el pan a 0.35 céntimos cada uno. El pan que no es del
# día tiene un descuento del 60%. Escribe un programa que permita ingresar los
# panes que no son del día. Después tu programa debe mostrar el precio habitual
# del pan, el descuento que se le hace por no ser fresco y el costo final total

#entrada:
while True:
    print("="*80)
    print("===BIENVENIDO AL PROGRAMA DE DESCUENTO DEL PAN===")
    print("="*80)
    precio= 0.35
    desc=0.60
    cantidad= int(input("INGRESA LA CANTIDAD DE PANES QUE NO SON DEL MISMO DÍA: \n Sue repuesta =>  "))
    print("="*80)

    precioh=cantidad * precio
    descut=precioh * desc
    preciofinal=precioh - descut

    print(f"\n Precio habitual: {round(precioh, 2)}")
    print(f" \n Descuento (60%): {round(descut,2)}")
    print(f"\n Precio final : {round(preciofinal,2)}")
    print("="*80)

    rpta= input("¿Deseas hacer otro pedido? (si/no): \n Su repuesta => ").lower()
    if rpta.lower() != "si":
        print("="*80)
        print("¡Gracias por usar el programa!")
        print("="*80)
        break
print("Elaborado por Esteban Trinidad")
print("="*80)
