import numpy as np

R = [[0, 1, 0, 1, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0]]


# debug
# R1 = [[1, 1, 0, 1, 0],
#     [1, 0, 1, 1, 0],
#     [1, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1],
#     [1, 1, 0, 0, 0]]

# R2 = [[1, 0, 1, 0],
#     [1, 1, 0, 0],
#     [1, 0, 1, 1],
#     [1, 0, 0, 1]]


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


# x* is largest in a Relation iff for any x∈X: x*Rx
def get_largest(R):
    shape = (np.array(R)).shape
    if(shape[0] != shape[1]):
        return "Relation is not a quadratic matrix"
    
    flag = 'NaN'
    for i in range(shape[0]):
        if(R[i] == [1 for j in range(shape[1])]):
            if(flag == 'NaN'): flag = []
            flag.append(i)
    return flag


# x₊ is smallest in a Relation iff for any x∈X: x₊Rx
def get_smallest(R):
    R = np.array(R)
    shape = R.shape
    if(shape[0] != shape[1]):
        return "Relation is not a quadratic matrix"
    
    flag = 'NaN'
    for j in range(shape[1]):
        if((np.ones((1, shape[0])) == R[:, j].reshape((1, shape[0]))).all()):
            if(flag == 'NaN'): flag = []
            flag.append(j)
    return flag


def get_strong_relation(R):
    R = np.array(R)
    Rs = np.zeros_like(R)
    for i in range(R.shape[0]):
        for j in range(R.shape[1]):
            if((R[i, j]!=0 or R[j, i]!=0) and (R[j, i] ==0)):
                Rs[i, j] = 1
    return Rs


def get_max(R):
    Rs = get_strong_relation(R)
    flag = 'NaN'
    for j in range(Rs.shape[1]):
        if((np.zeros((1, Rs.shape[0])) == Rs[:, j].reshape((1, Rs.shape[0]))).all()):
            if(flag == 'NaN'): flag = []
            flag.append(j)
    return flag


def get_min(R):
    Rs = get_strong_relation(R)
    flag = 'NaN'
    for i in range(Rs.shape[0]):
        if((np.zeros((1, Rs.shape[0])) == Rs[i, :].reshape((Rs.shape[0], 1))).all()):
            if(flag == 'NaN'): flag = []
            flag.append(i)
    return flag



def inverse(R):
    shape = (np.array(R)).shape
    for i in range(shape[0]):
        for j in range(i, shape[1]):
            res = R[i][j]
            R[i][j]=R[j][i]
            R[j][i]=res
    return R

def complement(R):
    shape = (np.array(R)).shape
    for i in range(shape[0]):
        for j in range(shape[1]):
            R[i][j]=1-R[i][j]
    return R



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

    print('Largest:', get_largest(R))
    print('Smallest:', get_smallest(R))
    print('Min:', get_min(R))
    print('Max:', get_max(R))

    #R2 for check
    # print('Min:', get_min(R2))
    # print('Max:', get_max(R2))


    print('Inversed R:', inverse(R))
    print('Complement R:', complement(R))

    return properties



print(check(R))

# print(get_strong_relation(R))
# print(get_strong_relation(R2))