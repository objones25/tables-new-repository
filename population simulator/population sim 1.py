import random
from dataclasses import dataclass

@dataclass
class Organism:
    reproRate: int
    deathRate: int
    foodRequire: int

OrganismPop = []

for i in range(0,500):
    OrganismPop.append(Organism(random.randint(0,1000), random.randint(0,800), random.randint(100,300)))
#print(OrganismPop)

def popYear(yrs):
    totalFoodGathered = 0
    totalFoodRequire = 0
    totalReproRate = 0
    totalDeathRate = 0

    for y in range(0,yrs+1):
        for Organisms in OrganismPop:
            #print(Organisms)
            foodGathered = random.randint(0,400)
            #print('foodGathered' + str(foodGathered))
            reproRole = random.randint(0,500)
            #print('reproRole' + str(reproRole))
            deathRole = random.randint(700,1000)
            #print('deathRole' + str(deathRole))

            if y == yrs:
                totalFoodRequire += Organisms.foodRequire
                totalFoodGathered += foodGathered
                totalReproRate += Organisms.reproRate
                totalDeathRate += Organisms.deathRate

            if Organisms.foodRequire > foodGathered:
                OrganismPop.remove(Organisms)
            elif deathRole < Organisms.deathRate:
                OrganismPop.remove(Organisms)
            elif (reproRole * Organisms.foodRequire) < (foodGathered * Organisms.reproRate):
                babyRepro = Organisms.reproRate + random.randint(-50,50)
                baby = Organism(babyRepro, random.randint(0,1000), Organisms.foodRequire)
                #print(baby)
                OrganismPop.append(baby)
                Organisms.deathRate += 75
            else:
                Organisms.deathRate += 50
    #print(OrganismPop)
    print(len(OrganismPop))
    print(totalFoodRequire / len(OrganismPop))
    print(totalFoodGathered / len(OrganismPop))
    print(totalReproRate / len(OrganismPop))
    print(totalDeathRate / len(OrganismPop))


popYear(8)
