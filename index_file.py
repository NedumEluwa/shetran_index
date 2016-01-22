###This program will open SHETRAN, run it and plot the discharge hydrograph###

#Import system modules
import output_checker
import subprocess
import matplotlib.pyplot as plt

shetran = subprocess.call('program/sv4.4.1.exe')

simulation = output_checker.results()

plt.plot(simulation)
plt.ylabel('simulated discharge (cumecs)')
plt.xlabel('hours')
plt.show()
