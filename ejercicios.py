"""La panadería de Don Pancho vende pan a $300 cada uno.

Reglas:

    Si compra más de 20 panes → 10% descuento
    Si compra más de 50 panes → 20% descuento
    Si ingresa una cantidad negativa, mostrar "Cantidad inválida"

Calcular y mostrar el total."""

preciopan=10
cantidad=int(input("cuantos panes quiere?"))

if not cantidad > 0:
    print("cantidad invalida")
else:
    total = cantidad * preciopan
    descuento10=(total*0.8)
    descuento20=(total*0.9)
    if cantidad >0 and cantidad <20:
        print(f"debes pagar. {total}")

    
    elif cantidad > 50:
        print(f"debes pagar. descuento 20%:{descuento20}")
    elif cantidad > 20:
        print(f"debes pagar. descuento 10%:{descuento10}")

    


