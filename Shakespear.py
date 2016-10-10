# Shakespear.py
# by George Yu
# A genetic word generator that tries to get a specific string.

from string import ascii_lowercase as allChars
from random import random, randint, choice
from threading import Thread
from sys import exit
import tkinter as tk

allChars += ' !.,?\'' # I didn't use string.punctuation because there is a lot of unusual characters, you may use it if you like
correct = 'to be or not to be'
length = len(correct)
popSize = 30
mutationRate = 6

root = tk.Tk()
root.title('Shakespear')
fitDisplay = tk.StringVar(root)
popDisplay = tk.StringVar(root)
tk.Label(root, font=('Monaco', 20), height=6, width=length+12, textvariable=fitDisplay).pack()
tk.Label(root, font=('Monaco', 11), textvariable=popDisplay).pack(side='left',fill='x')

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
        return ''.join(choice(allChars) for i in range(length))

def crossover(father, mother):
    split = randint(1, len(father))
    new = list(father[:split] + mother[split:])
    for i in range(len(new)):
        if random()*100 < mutationRate:
            new[i] = choice(allChars)
    return ''.join(new)

def reproduce(population):
    fitnesses = [calcFitness(i) for i in population]
    maxFit = population[fitnesses.index(max(fitnesses))]
##    print(maxFit)
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

def main():
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
            return

try:
    Thread(target=main).start()
    root.mainloop()
except:
    exit()
