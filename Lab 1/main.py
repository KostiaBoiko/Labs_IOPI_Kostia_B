import numpy as np
import matplotlib.pyplot as plt

FileName = input("Enter name of .txt file: ")
Data = np.genfromtxt(FileName, dtype='str')
empty_list = []
NofData = 0
datasort = sorted(Data)
for ele in datasort:
    if(ele not in empty_list):
        NofData += 1
        empty_list.append(ele)
#print(NofData)

NameOfFilms = [0 for i in range(NofData)]
freq = [1 for i in range(NofData)]
indNofF = 0
indfreq = -1
for i in range(len(datasort)):
    for j in range(NofData):
        if (datasort[i] == NameOfFilms[j]):
            freq[indfreq] += 1
            break
        if (j == NofData - 1):
            NameOfFilms[indNofF] = datasort[i]
            indNofF += 1
            indfreq += 1
#print(NameOfFilms)
#print(freq)
count = [(NameOfFilms[i], freq[i]) for i in range(NofData)]


totalcount = 0
f = open("result.txt", "w+")
f.write("\n Name & Views | Count | Total count")
f.write("\n -------------+-------+------------")
print("Name & Views| Count | Total Count ")
print("------------+-------+-------------")
for i in range(len(count)):
    totalcount += count[i][1]
    f.write("\n\t " + str(count[i][0]) + " \t|   " + str(count[i][1]) + "   |\t" + str(totalcount))
    print("\t  " + str(count[i][0]) + " \t|   " + str(count[i][1])+"   |\t" + str(totalcount))
f.write("\n")


for i in range(int(len(freq))):
    if (freq[i] == max(freq)):
        maxnumber = ('Number = ' + str(NameOfFilms[i]) + ' Freq = ' + str(freq[i]))
        Moda = 'Mode of entry data: ' + maxnumber
        print(Moda)


Mediana = 'Mediana of entry data = ' + str(datasort[int(len(Data) / 2)])
print(Mediana)

sumX = 0
for i in range(int(len(freq))):
    sumX += int(NameOfFilms[i]) * freq[i]
sumX = sumX/int(len(Data))
AverageSum = "Average value: " + str(round(sumX, 3))
print(AverageSum)

varX = 0
for i in range(int(len(Data))):
    varX += (int(Data[i]) - sumX) ** 2
varX = varX/(int(len(Data)) - 1)
disp = "Dispersion: " + str(round(varX, 3))
print(disp)
varX = np.sqrt(varX)
averagequad = "Mean square deviation: " + str(round(varX, 3))
print(averagequad)


f.write(Moda + "\n" + Mediana + "\n" + AverageSum + "\n" + disp + "\n" + averagequad)
f.close()


f, ax = plt.subplots()
plt.hist(sorted(Data), bins=int(10), facecolor='purple', align='mid', alpha=0.5)
plt.ylabel("Views")
plt.xlabel("Names of Films")
plt.title("Table Films")
plt.show()
