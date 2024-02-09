import numpy as np

R = [[0, 1, 0, 1, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0]]


def isReflexive(R):
    for i in range(len(R)):
        if(R[i][i]!=1):
            return False
    return True

def isAntireflexive(R):
    for i in range(len(R)):
        if(R[i][i]!=0):
            return False
    return True

def isSymetric(R):
    for i in range(len(R)):
        for j in range(len(R[i])):
            if(R[i][j]!=R[j][i]):
                return False
    return True

def isAntysymetric(R):
    for i in range(len(R)):
        for j in range(len(R[i])):
            if(R[i][j]==R[j][i] and R[i][j]==1 and i!=j):
                return False
    return True

def isAsymetric(R):
    for i in range(len(R)):
        for j in range(len(R[i])):
            if(R[i][j]==R[j][i] and R[i][j]==1):
                if(i==j and R[i][j]!=0):
                    return False
    return True

def isin(R1, R2):
    if(len(R1)!=len(R2)):
        return

    for i in range(len(R1)):
        for j in range(len(R1[i])):
            if(R1[i][j]>R2[i][j]):
                return False
    return True

def isTransitive(R):
    R = np.array(R)
    R_s = R.dot(R)
    if(isin(R_s, R)):
        return True
    else:
        return False




def check(R):
    properties = []
    if(isReflexive(R)):
        properties.append('Reflexive')
    if(isAntireflexive(R)):
        properties.append('Antireflexive')
    if(isSymetric(R)):
        properties.append('Symetric')
    if(isAntysymetric(R)):
        properties.append('Antysymetric')
    if(isAsymetric(R)):
        properties.append('Asymectic')
    if(isTransitive(R)):
        properties.append('Transitive')

    return properties






print(check(R))