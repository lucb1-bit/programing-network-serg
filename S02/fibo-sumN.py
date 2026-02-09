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
    return fibo_list

def fibosum(n):
    res = 0
    for i in fibon(n):
        res += i
    return "Sum of the first " + str(n) + " terms of the Fibonacci series: " + str(res)


print("\n",fibosum(5),"\n", fibosum(10),"\n",fibosum(15))