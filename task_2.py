a = 100 #Kolichestvo stranic v knige
b = 50 #Chislo strok na stranitce
c = 25 #Kolichestvo simvolov
d = 4 #rasmer odnovo simvola
sum_ = float(a*b*c*d) #rasmer odnoy knigi
k = float(1.44)
V_ = k*1024**2
Obyom = int(V_//sum_)
print (f"Количество книг, помещающихся на дискету: {Obyom}")
