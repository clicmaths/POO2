import random

def des():
    de1 = random.randint(1,6)
    de2 = random.randint(1,6)
    de3 = random.randint(1,6)
    de4 = random.randint(1,6)
    list = [de1, de2, de3, de4]
    list.sort()
    list.pop(0)
    return list[0] + list[1] + list[2]
class npc:
    def __init__(self):
        self.force = des()
        self.agilite = des()
        self.constitution = des()
        self.intelligence = des()
        self.sagesse = des()
        self.charisme = des()
        self.classe_dèarmure = random.randint(1,12)
        self.nom = 'Yi Long'
        self.race = 'humain'
        self.espece = 'animal'
        self.point_de_vie = random.randint(1,20)
        self.profession = 'voleur'
        



