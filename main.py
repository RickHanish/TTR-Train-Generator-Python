import random

with open("DestinationList.txt", 'r') as f:
    cityList = []
    connectorList = []
    for line in f:
        name = line[:len(line) - 1]
        line = f.readline()
        numConnectors = int(line)
        connectors = []
        i = 0
        while i < numConnectors:
            line = f.readline()
            newCity = line
            connectors.append(newCity[:len(newCity) - 1])
            i = i + 1
        cityList.append(name)
        connectorList.append(connectors)
        f.readline()
j = 0
while j < 4:
    i = random.randrange(len(cityList))
    # print(i)
    # print(len(cityList))
    print(cityList[i], "<>", connectorList[i][random.randrange(len(connectorList[i]))])
    j = j + 1
