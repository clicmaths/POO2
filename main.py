import random

#fonction pour définir les stats
def des():
    de1 = random.randint(1,6)
    de2 = random.randint(1,6)
    de3 = random.randint(1,6)
    de4 = random.randint(1,6)
    list = [de1, de2, de3, de4]
    list.sort()
    list.pop(0)
    return list[0] + list[1] + list[2]

#classe npc
class npc:

#fonction pour les stats de npc
    def __init__(self):
        self.force = des()
        self.agilite = des()
        self.constitution = des()
        self.intelligence = des()
        self.sagesse = des()
        self.charisme = des()
        self.classe_armure = random.randint(1,12)
        self.nom = 'Yi Long'
        self.race = 'kobold'
        self.espece = 'monstre'
        self.point_de_vie = random.randint(1,20)
        self.profession = 'voleur'

#fonction qui montre les stats
    def afficher_stats(self):
        print('force: ', self.force)
        print('agilité: ', self.agilite)
        print('constutution: ', self.constitution)
        print('intelligence: ', self.intelligence)
        print('sagesse: ', self.sagesse)
        print('charisme: ', self.charisme)
        print("classe d'armure: " , self.classe_armure)
        print('nom: ', self.nom)
        print('race: ', self.race)
        print('espèce: ', self.espece)
        print('point de vie: ', self.point_de_vie)
        print('profession: ', self.profession )

#classe kobold qui est un npc
class kobold(npc):
    #méthode d'attaquer
    def attaquer(self, cible):
        self.cible = cible
        attaque = random.randint(1, 20)
        if attaque == 20:
            dommage = random.randint(1, 8)
            cible.point_de_vie = - dommage

        elif 20 > attaque > 1:
            if attaque >= cible.classe_armure:
                dommage = random.randint(1, 6)
                cible.point_de_vie = - dommage

            else:
                print("attaque n'a pas fonctionné")

        elif attaque == 1:
            print("attaque ratée")

#subir de dommage
    def subir_dommage(self):
        self.point_de_vie -= (random.randint(1,6) - self.classe_armure)

#classe héros (exemple de npc)
class heros(npc):

#fonction d'attaquer
    def attaquer(self, cible):
        self.cible = cible
        attaque = random.randint(1, 20)
        if attaque == 20:
            dommage = random.randint(1,8)
            cible.point_de_vie =- dommage

        elif 20 > attaque > 1:
            if attaque >= cible.classe_armure:
                dommage = random.randint(1,6)
                cible.point_de_vie =- dommage

            else:
                print("attaque n'a pas fonctionné")

        elif attaque == 1:
            print("attaque ratée")

#subir de dommage
    def subir_dommage(self):
        self.point_de_vie -= (random.randint(1, 6) - self.classe_armure)



