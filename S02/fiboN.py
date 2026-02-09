def fibon(n):
    fibo_list = []
    for i in range (0,n):
        n1= (len(fibo_list)-1)
        n2= (len(fibo_list)-2)
        if i == 0:
            fibo_list.append(0)
        elif i == 1:
            fibo_list.append(1)
        else:
            fibo_list.append(fibo_list[n1] + fibo_list[n2])
    return "The " + str(n) + "th Fibonacci term: " + str(fibo_list[len(fibo_list) - 1])

print("\n",fibon(5),"\n", fibon(10),"\n",fibon(15))
