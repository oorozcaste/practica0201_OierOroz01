produktua = input("dime un producto: ")
precio = float(input("dime su precio: "))
unitateak = int(input("dime el numero de unidades: "))

costetotal = precio*unitateak

frasenueva =("el nombre del producto es {},el precio de es de producto es {:6.2f} son {} unidades y el gasto es de {:8.4f} euros ").format(produktua,precio,unitateak,costetotal)
print(frasenueva)