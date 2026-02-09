fibo_list = []
for i in range (0,11):
    n1= (len(fibo_list)-1)
    n2= (len(fibo_list)-2)
    if i == 0:
        fibo_list.append(0)
    elif i == 1:
        fibo_list.append(1)
    else:
        fibo_list.append(fibo_list[n1] + fibo_list[n2] )
print (fibo_list)

