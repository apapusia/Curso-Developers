import random


pesos={
    'winning':1,
    'break_event':2,
    'lossing':10
}

def weighted_lottery(pesos):
    container_list=[]
    for (name,peso) in pesos.items():
        for _ in range(peso):
            container_list.append(name)
    return random.choices(container_list)
    
        

print(weighted_lottery(pesos))

