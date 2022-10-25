import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve
InputData = [0]
File = open("result.txt", "w+")


def ImportTxtFile(data):    #імпорт файлу та внесення його значень у змінну, створення файлу для запису
    NameOfFile = input("Input txt file: ")
    data = np.genfromtxt(NameOfFile, dtype='int')
    data = np.delete(data,0)
    print("Unsorted data: ", data)
    File.write("Unsorted data: " + str(data))
    data = sorted(data)
    print("\nSorted data: ", data)
    File.write("\nSorted data: " + str(data) + "\n\n")
    return data

def CalculationOfPercentile(x, SortedData):   #обчислення персантилів
    index = x * (len(SortedData) + 1) - 1
    Percentile = SortedData[int(index)] + (index % int(index)) * (SortedData[int(index) + 1] - SortedData[int(index)])
    return Percentile

def CalculateAverageDeviation(data, midleX):     #cереднє відхилення
    totalSum = 0
    for i in range(len(data)):
        totalSum += abs(data[i] - midleX)
    return totalSum/(len(data))

def CalculateStandartDeviation(data, midleX):    #стандартне відхилення
    totalSum = 0
    for i in range(len(data)):
        totalSum += (data[i] - midleX)**2
    return np.sqrt(totalSum/(len(data)-1))

def CalculationOfGrades(data, midleX):   #обчислення оцінок за допомогою лінійних рівнянь
    ResultArray = []
    GradeA = np.array([[100*1, 1, ], [1*midleX, 1, ]])
    GradeB = np.array([100, 95])
    GradeX = solve(GradeA, GradeB)
    GradeA = round(GradeX[0], 2)
    GradeB = round(GradeX[1], 2)
    print("GradeA = " + str(GradeA) + "\nGradeB = " + str(GradeB))
    File.write("GradeA = " + str(GradeA) + "\nGradeB = " + str(GradeB))
    for i in range(len(data)):
        ResultArray.append(GradeA*data[i]+GradeB)
    print("Result grades: " + str(ResultArray) + "\n\n")
    File.write("\nResult grades: " + str(ResultArray) + "\n\n")

def CalculateFirstDigit(num):     #визначення першої цифри з числа
    digit = ""
    for i in range(len(str(num))-1):
        digit += str(num)[i]
    return digit

def CreateSteamLeafDiagram(Data):      # діаграма "стовбур-листя"
    strnumbers = ""
    leaves = []
    key = 0
    for i in range(len(Data)):
        strnumbers += str(Data[i] % 10) + " "
        FDigit = int(CalculateFirstDigit(Data[i]))
        j = i
        if (i == len(Data)-1):
            leaves.append(strnumbers)
            print(CalculateFirstDigit(Data[i]) + " \t| \t" + strnumbers)
            File.write("\n" + CalculateFirstDigit(Data[i]) + " \t| \t" + strnumbers)
            break
        elif (CalculateFirstDigit(Data[i]) != CalculateFirstDigit(Data[i + 1])):
            leaves.append(strnumbers)
            print(CalculateFirstDigit(Data[i]) + " \t| \t" + strnumbers)
            File.write("\n" + CalculateFirstDigit(Data[i]) + " \t| \t" + strnumbers)
            strnumbers = ""
            FDigit += 1
            while (FDigit != int(CalculateFirstDigit(Data[i + 1]))):
                print(str(FDigit) + " \t| \t" + strnumbers)
                File.write("\n" + str(FDigit) + " \t| \t" + strnumbers)
                FDigit += 1
        while (j != len(Data) and key == 0):
            if (int(CalculateFirstDigit(Data[i])) == int(CalculateFirstDigit(Data[j]))-1):
                key = Data[i]
                break
            else:
                j += 1
    print("\nKey: " + str(key))
    File.write("\n\nKey: " + str(key))

def GenerateBoxDiagram(Data):    #коробкова діаграма
    plt.figure(figsize=(10, 7))
    plt.boxplot(Data, vert = 0)
    plt.grid()
    plt.show()


InputData = ImportTxtFile(InputData)
MinElement = min(InputData)
MaxElement = max(InputData)
FirstQuartile = CalculationOfPercentile(0.25, InputData)
ThirdQuartile = CalculationOfPercentile(0.75, InputData)
Percentile90 = CalculationOfPercentile(0.9, InputData)
SumOfElements = 0
for i in range(len(InputData)):
    SumOfElements += InputData[i]
midleX = SumOfElements / len(InputData)
print("\nLower(first) quartile = " + str(FirstQuartile))
File.write("Lower(first) quartile = " + str(FirstQuartile))
print("Upper(third) quartile = " + str(ThirdQuartile))
File.write("\nUpper(third) quartile = " + str(ThirdQuartile))
print("\n90-th percentile = " + str(Percentile90))
File.write("\n\n90-th percentile = " + str(Percentile90))
print("\nStandart Deviation = " + str(CalculateStandartDeviation(InputData, midleX)))
File.write("\n\nStandart Deviation = " + str(CalculateStandartDeviation(InputData, midleX)))
print("Average Deviation = " + str(CalculateAverageDeviation(InputData, midleX)) + "\n")
File.write("\nAverage Deviation = " + str(CalculateAverageDeviation(InputData, midleX)) + "\n\n")
CalculationOfGrades(InputData, midleX)
print("Stem-Leaf Diagram")
File.write("\nStem-Leaf Diagram")
CreateSteamLeafDiagram(InputData)
GenerateBoxDiagram(InputData)