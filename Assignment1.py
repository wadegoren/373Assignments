import numpy as np
import matplotlib.pyplot as plt
# Define parameters
serviceRate = 0.75
arrivalRates = [0.2,0.4,0.5,0.60,0.65,0.7,0.72,0.74,0.745]
runTime = int(1000000)
finalArray = []
#Simulate the queue arrival rate and calculate the expected delay
for arrivalRate in arrivalRates:
  queue = []
  time = 0
  numArrived = 1
  for i in range(runTime):
   if arrivalRate > np.random.random():
    queue.append(np.random.geometric(serviceRate))
   if 0 < len(queue):
    time = time + len(queue) - 1
    queue[0] -= 1
    if queue[0] == 0:
     queue.pop(0)
     numArrived += 1
   expectedDelay = time/numArrived
 finalArray.append(expectedDelay)
#Plot the expeected queueing delay with respect to the arrival rate
plt.plot(arrivalRates, finalArray)
plt.title("Expected Queueing Delay vs. Arrival Rate")
plt.xlabel("Arrival Rate (Lambda)")
plt.ylabel("Expected Queueing Delay")
plt.show()
