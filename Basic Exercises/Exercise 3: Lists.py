temperatures = [15.5, 17.2, 14.8, 16.0, 18.3, 20.1, 19.5]
max = sorted(temperatures)
min = sorted(temperatures,reverse=True)

def avg(temp):
    total = 0
    for t in temp:
        total +=t
    return round(total/len(temp),1)
def up_17(temp):
    counter = 0
    for t in temp:
        if t < 17:
            counter +=1
    return counter

print("The temperature on Wednesday (index 2): ",temperatures[2])
print("The maximum temperature:",max[-1])
print("The minimum temperature:",max[0])
print("The average temperature:" ,avg(temperatures))
print("The number of days above 17 degrees",up_17(temperatures))
print("The list sorted from lowest to highest",min)