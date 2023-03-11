#Juan Esteban Clavijo Garcia - Codigo: 202225709

cantidadA=int(input("Digite la cantidad de adultos:"))
cantidadN=int(input("Digite la cantidad de niños:"))
TP=(cantidadA*12000)+(cantidadN*8000)
M=TP*0.25
PE=TP*0.55
GN=TP*0.20
print("")
print("Total a pagar:",TP)
print("Total mantenimiento:",M)
print("Total pago a empleados:",PE)
print("Ganancia neta:",GN)
