##this function returns the simulated discharge##

import os

cwd = os.getcwd()

def output_checker():
    files = os.listdir(cwd)
    for filename in files:
        if 'output' in filename and 'discharge' in filename and 'everytimestep' not in filename:
            return str(filename)

def results():
    hourly_discharge = output_checker()
    simulated = []
    f = open(hourly_discharge, 'r')
    next(f)
    for line in f:
        simulated.append(float(line.strip()))
    return simulated

#print results()
