sales={
    'g':20,
    'f':32,
    't':12,
    'o':16
}

#copiar el dictionary, y cambiar sus valores por '$'
new_sales=sales.copy()
for x in new_sales:
    new_sales[x]=new_sales[x] *'$'
#convertir el dictionary en list    
sales_list=(list(new_sales.items()))
#pasar a string cada ele. y concatenar
for item in sales_list:
    print(str(item[0])+' '+str(item[1]))

