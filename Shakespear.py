# Shakespear.py
# by George Yu
# A genetic word generator that tries to get a specific string.

from string import ascii_lowercase as alphabet
from random import random, randint, choice
import tkinter
import threading

alphabet += ' '
correct = 'to be or not to be'
length = len(correct)
popSize = 30

root = tkinter.Tk()
root.title('Shakespear')
fitDisplay = tkinter.StringVar(root)
popDisplay = tkinter.StringVar(root)
tkinter.Label(root, font=('Monaco', 20), height=6, width=length+12, textvariable=fitDisplay).pack()
tkinter.Label(root, font=('Monaco', 12), textvariable=popDisplay).pack(side='left',fill='x')

class start(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        newDNA = [None for i in range(popSize)]
        popNum = 1
        while True:
            popDisplay.set(' Population: %d'%popNum)
            popNum += 1
            population = []
            for dna in newDNA:
                population.append(generate(dna))
            newDNA = reproduce(population)
            if newDNA == True:
                break

def calcFitness(individual):
    fitnessVal = 1
    for i,j in zip(correct, individual):
        if i == j:
            fitnessVal *= 2
    return fitnessVal

def generate(dna):
    if dna:
        return dna
    else:
        return ''.join(choice(alphabet) for i in range(length))

def crossover(father, mother):
    split = randint(1, len(father))
    new = list(father[:split] + mother[split:])
    for i in range(len(new)):
        if random() < 0.1:
            new[i] = choice(alphabet)
    return ''.join(new)

def reproduce(population):
    fitnesses = [calcFitness(i) for i in population]
    maxFit = population[fitnesses.index(max(fitnesses))]
    fitDisplay.set(maxFit)
    if maxFit == correct:
        return True
    matingPool = []
    for fitness, indiv in zip(fitnesses, population):
        matingPool += [indiv for i in range(fitness)]
    newDNA = []
    for i in range(popSize):
        newDNA.append(crossover(choice(matingPool), choice(matingPool))) 
    return newDNA

thread = start()
thread.start()
root.mainloop()
