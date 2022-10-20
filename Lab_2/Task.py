import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve
Data = [0]
File = open("result.txt", "w+")


def connectTxT(data):    #імпорт файлу та внесення його значень у змінну, створення файлу для запису
    NameOfFile = input("Input txt file: ")
    data = np.genfromtxt(NameOfFile, dtype='int')
    data = np.delete(data,0)
    print("Unsorted data: ", data)
    File.write("Unsorted data: " + str(data))
    data = sorted(data)
    print("\nSorted data: ", data)
    File.write("\nSorted data: " + str(data) + "\n\n")
    return data


def getFirstDigit(num):     #визначення першої цифри з числа
    digit = ""
    for i in range(len(str(num))-1):
        digit += str(num)[i]
    return digit


def Pfunc(x, SortedData):   #обчислення персантилів
    index = x * (len(SortedData) + 1) - 1
    Percentile = SortedData[int(index)] + (index % int(index)) * (SortedData[int(index) + 1] - SortedData[int(index)])
    return Percentile


def StandartDeviation(data, midleX):    #стандартне відхилення
    totalSum = 0
    for i in range(len(data)):
        totalSum += (data[i] - midleX)**2
    return np.sqrt(totalSum/(len(data)-1))

def AverageDeviation(data, midleX):     #cереднє відхилення
    totalSum = 0
    for i in range(len(data)):
        totalSum += abs(data[i] - midleX)
    return totalSum/(len(data))


def boxdiagram(data):    #коробкова діаграма
    plt.figure(figsize=(10, 7))
    plt.boxplot(data)
    plt.grid()
    plt.show()


def lineal(data, midleX):   #обчислення оцінок за допомогою лінійних рівнянь
    result = []
    a = np.array([
        [100*1, 1, ],
        [1*midleX, 1, ]
    ])
    b = np.array([100, 95])
    x = solve(a, b)
    print("a = " + str(x[0]) + "\nb = " + str(x[1]))
    File.write("a = " + str(x[0]) + "\nb = " + str(x[1]))
    for i in range(len(data)):
        result.append(x[0]*data[i]+x[1])
    print("Result marks: " + str(result) + "\n\n")
    File.write("\nResult marks: " + str(result) + "\n\n")


Data = connectTxT(Data)
minimal = min(Data)
maximal = max(Data)
Q1 = Pfunc(1 / 4, Data)
Q3 = Pfunc(3 / 4, Data)
P90 = Pfunc(0.9, Data)
sum = 0
for i in range(len(Data)):
    sum += Data[i]
midleX = sum / len(Data)
print("\n\nMediana = ", midleX)
print("\nLower(first) quartile = " + str(Q1))
File.write("Lower(first) quartile = " + str(Q1))
print("Upper(third) quartile = " + str(Q3))
File.write("\nUpper(third) quartile = " + str(Q3))
print("\n90-th percentile = " + str(P90))
File.write("\n\n90-th percentile = " + str(P90))
print("\nStandart Deviation = " + str(StandartDeviation(Data, midleX)))
File.write("\n\nStandart Deviation = " + str(StandartDeviation(Data, midleX)))
print("Average Deviation = " + str(AverageDeviation(Data, midleX)) + "\n")
File.write("\nAverage Deviation = " + str(AverageDeviation(Data, midleX)) + "\n\n")
lineal(Data, midleX)

print("Stem-Leaf Diagram")
File.write("\nStem-Leaf Diagram")
def CreateTable(data):      # діаграма "стовбур-листя"
    strnumbers = ""
    leaves = []
    key = 0
    for i in range(len(data)):
        strnumbers += str(data[i] % 10) + " "
        FDigit = int(getFirstDigit(data[i]))
        j = i
        if (i == len(data)-1):
            leaves.append(strnumbers)
            print(getFirstDigit(data[i]) + " \t| \t" + strnumbers)
            File.write("\n" + getFirstDigit(data[i]) + " \t| \t" + strnumbers)
            break
        elif (getFirstDigit(data[i]) != getFirstDigit(data[i+1])):
            leaves.append(strnumbers)
            print(getFirstDigit(data[i]) + " \t| \t" + strnumbers)
            File.write("\n" + getFirstDigit(data[i]) + " \t| \t" + strnumbers)
            strnumbers = ""
            FDigit += 1
            while (FDigit != int(getFirstDigit(data[i+1]))):
                print(str(FDigit) + " \t| \t" + strnumbers)
                File.write("\n" + str(FDigit) + " \t| \t" + strnumbers)
                FDigit += 1
        while (j != len(data) and key == 0):
            if (int(getFirstDigit(data[i])) == int(getFirstDigit(data[j]))-1):
                key = data[i]
                break
            else:
                j += 1
    print("\nKey: " + str(key))
    File.write("\n\nKey: " + str(key))


CreateTable(Data)
boxdiagram(Data)