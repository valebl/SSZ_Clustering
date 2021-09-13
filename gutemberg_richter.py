import numpy as np

def gutemberg_richter(magnitude, year):

    Mmin = 4.5
    Mmax = max(magnitude)
    Delta_M = 0.2
    ThreshYear = [min(year), max(year)]

    Minterval0 = [x/100 for x in range(int(3.5*100), int(Mmax*100), int(Delta_M*100))]
    Minterval  = [x/100 for x in range(int(Mmin*100), int(Mmax*100), int(Delta_M*100))]

    index = [i for i in range(len(year)) if year[i] > ThreshYear[0]]
    magnitude = magnitude[index]

    Mmintoshow = min(magnitude)
    Mmaxtoshow = max(magnitude)

    N0 = np.zeros(len(Minterval0)-1)
    for i in range(len(Minterval0)-1):
        N0[i] = len([1 for j in range(len(magnitude)) if magnitude[j] >= Minterval0[i]])/(ThreshYear[1]-ThreshYear[0]+1)

    N = np.zeros(len(Minterval)-1)
    for i in range(len(Minterval)-1):
        N[i] = len([1 for j in range(len(magnitude)) if magnitude[j] >= Minterval[i]])/(ThreshYear[1]-ThreshYear[0]+1)

    N0[N0==0] = 0
    N[N==0] = 0

    # Calculate the b-value (maximum likelihood)
    Mlist = [m for m in magnitude if m > Mmin]
    if Mlist != []:
        MminCat = np.min([m for m in magnitude if m > Mmin])
        MmeanCat = np.mean([m for m in magnitude if m > Mmin])
    else:
        return 0

    # Calculate the b-value
    b = 1/(MmeanCat-(MminCat-Delta_M/2)) * np.log10(np.exp(1))

    # Calculate the a-value
    a = np.log10(N[0]) + b * MminCat

    GRfit = [a, b]

    return GRfit


