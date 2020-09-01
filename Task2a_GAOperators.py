import random,copy
from math import exp
class CHROMOSOME:
    def __init__(self,length=8):
        self.genes=[None]*length
        for i in range(length):
            self.genes[i]=random.choice([0,1])
        self.EVALUATE()

    def EVALUATE(self):
        x_value=(4*self.genes[1]+2*self.genes[2]+1*self.genes[3])
        if self.genes[0]:
            x_value*=-1
        y_value = (4 * self.genes[-3] + 2 * self.genes[-2] + 1 * self.genes[-1])
        if self.genes[-4]:
            y_value *= -1

        value1=exp(-1*(pow(x_value, 2) + pow(y_value, 2)))
        self.fitness=value1
        # 
        # value1=pow((1-x_value),2)
        # value2=pow((y_value-pow(x_value,2)),2)
        # self.fitness=value1+100*value2

class SELECTION:
    def binary_tournament(pop,return_pop,T_size):
        new_population=[]
        for i in range(return_pop):
            Tour_teams=[]
            for j in range(T_size):
                Tour_teams.append(random.choice(pop))
            new_population.append(max(Tour_teams,key=lambda item:item.fitness))
        return(new_population)

class OPERATOR:
    def one_point_crossover(parent1,parent2):

        print('parent fitness',parent1.fitness,parent2.fitness)
        child1=copy.deepcopy(parent1)
        child2=copy.deepcopy(parent2)

        crossover_point=random.randint(0,len(parent2.genes))
        print('crossover point', crossover_point)
        child1.genes[crossover_point:]=parent2.genes[crossover_point:]
        child2.genes[crossover_point:]=parent1.genes[crossover_point:]
        print('The children are :',child1.genes,child2.genes)
        child1.EVALUATE()
        child2.EVALUATE()
        print('child fitness', child1.fitness, child2.fitness)

        return child1,child2

    def two_point_crossover(parent1, parent2):
        print('parent fitness', parent1.fitness, parent2.fitness)
        child1 = copy.deepcopy(parent1)
        child2 = copy.deepcopy(parent2)

        crossover_point1 = random.randint(0, len(parent2.genes))
        crossover_point2 = random.randint(0, len(parent2.genes))
        if (crossover_point1 >crossover_point2):
            crossover_point1,crossover_point2=crossover_point2,crossover_point1
        print('crossover point:', crossover_point1,crossover_point2)

        child1.genes[crossover_point1:crossover_point2] = parent2.genes[crossover_point1:crossover_point2]
        child2.genes[crossover_point1:crossover_point2] = parent1.genes[crossover_point1:crossover_point2]
        print('The children are :', child1.genes, child2.genes)
        child1.EVALUATE()
        child2.EVALUATE()
        print('parent fitness', child1.fitness, child2.fitness)

        return child1, child2

    def flip_mutation(ind):
        index=random.randint(0,len(ind.genes)-1)
        print('index is:',index)
        print('before',ind.genes)
        ind.genes[index]=int(not(ind.genes[index]))
        print('after', ind.genes)
        ind.EVALUATE()
        return ind
