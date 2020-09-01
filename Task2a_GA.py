import Task2a_GAOperators,random
pop=[_ for _ in range(10)]
#random solution generations
print('\nPOPULATION:')
for i in range(0,10):
    pop[i]=Task2a_GAOperators.CHROMOSOME(8)
    print(pop[i].genes,pop[i].fitness)

print('******************************************************************************')

for g in range(0,1): #generation loop
    offspring_pop=[]
    print('GENERATION:\n')

    for i in range(0,len(pop),2):
        parents=Task2a_GAOperators.SELECTION.binary_tournament(pop,2,2) #10 individual mn se 2 ko utha rh hun
        # print(parents[0].fitness,parents[1].fitness)
        for ind in parents:
            print(ind.genes,ind.fitness)
        print('\n')
        #off1,off2=GA_operators.operator.one_point_crossover(parents[0],parents[1])
        off1,off2=Task2a_GAOperators.OPERATOR.two_point_crossover(parents[0],parents[1])
        if random.random()<0.2:
            print('\nMUTATING')
            off1=Task2a_GAOperators.OPERATOR.flip_mutation(off1)
            print('after mutation fitness of offspring1:',off1.fitness)

        if random.random()<0.2:
            print('\nMUTATING')
            off2=Task2a_GAOperators.OPERATOR.flip_mutation(off2)
            print('after mutation fitness of offspring1:',off2.fitness)
        offspring_pop.append(off1)
        offspring_pop.append(off2)

    print('******************************************************************************')
    pop=Task2a_GAOperators.SELECTION.binary_tournament(pop+offspring_pop,len(pop),10) #survival selection

print('\nOPTIMAL SOLUTION:',sorted(pop,key=lambda x:x.fitness,reverse=True)[0].fitness)
    # for ind in pop:
    #     print(ind.genes, ind.fitness)
# if random.random()<0.2:
#     print('mutating')
#     off1=GA_operators.operator.flip_mutation(off1)
# print(off1.genes,off1.fitness)
# print(off2.genes,off2.fitness)