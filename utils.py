import numpy as np
import matplotlib.pyplot as plt

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

def derive_zones(path_to_file)
    zones = []
    with open(path_to_file) as f:
        lines = f.read()
        for zone in lines.split(';'):
            zones.append(zone)
    for i in range(len(zones)):
        zones[i] = zones[i].split('\n')
        for j in range(len(zones[i])):
            zones[i][j] = zones[i][j].split(',')
        if [''] in zones[i]:
            zones[i].remove([''])
    for i in range(len(zones)):
        for j in range(len(zones[i])):
            if '' in zones[i][j]:
                zones[i][j].remove('')
            if zones[i][j] == []:
                del zones[i][j]
                continue
            for k in range(len(zones[i][j])):
                zones[i][j][k] = float(zones[i][j][k])
    return zones
                
def plot_italy(zones):
    j = 0
    for zone in zones:
        x_zone = [zone[i][0] for i in range(len(zone)) if i > 0]
        y_zone = [zone[i][1] for i in range(len(zone)) if i > 0]
        plt.plot(x_zone, y_zone, 'k', alpha=1, linewidth=0.3)
        j += 1

def haversine_np(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees) in km.

    All args must be of equal length.    

    """
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = np.sin(dlat/2.0)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2.0)**2

    c = 2 * np.arcsin(np.sqrt(a))
    km = 6367 * c
    return km


def distance_np(x1, y1, x2, y2):
    
    x2 = np.array(x2)
    y2 = np.array(y2)

    dx = x2 - x1
    dy = y2 - y1

    d = np.sqrt(dx**2 + dy**2)

    return d


