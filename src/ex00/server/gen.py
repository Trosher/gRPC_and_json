from random import uniform, randint, choice
from names import get_first_name, get_last_name

def genDataShip():
    dict_valid_param = [[[80,250],[4,10],True,True],
                        [[300,600],[10,15],True,False],
                        [[500,1000],[15,30],True,True],
                        [[800,2000],[50,80],True,False],
                        [[1000,4000],[120,250],False,True],
                        [[5000,20000],[300,500],True,True]]
    clas:int = randint(0, 5)
    name:str = get_first_name()
    armed:bool = randint(0, 1) if dict_valid_param[clas][2] else 0
    alignment:int = randint(0, 1) if dict_valid_param[clas][3] else 0
    length:float = uniform(dict_valid_param[clas][0][0], dict_valid_param[clas][0][1])
    crewSize:int = randint(dict_valid_param[clas][1][0], dict_valid_param[clas][1][1])
    officers = []
    rank = ['Lieutenant', 'Captain', 'Major', 'Colonel', 'General', 'Commander']
    for _ in range(0 if name == "Enemy" else 1, 10):
        officer:dict = {'first_name': get_first_name(), 
                        'last_name' : get_last_name(),
                        'rank' : choice(rank)}
        officers.append(officer)
    return {'alignment' : alignment, 'name' : name, 'class' : clas,
            'length' : length, 'crew_size' : crewSize, 'armed' : armed,
            'officers' : officers}