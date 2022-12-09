def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


def combinations(n, m): # combination without repetition
    return factorial(n) / (factorial(m) * factorial(n - m))

def plcmntWrep(n, m): # placement with repetition
    return n**m

def simpleprob(a, b):
    return (a/b) * 100

def probof2(a, b):
    return a*b

def prob7task(countOfStud, prepTask, totalCountOfStud, allTasks):
    return (countOfStud / totalCountOfStud) * (prepTask / allTasks) * ((prepTask - 1) / (allTasks - 1)) * ((prepTask - 2) / (allTasks - 2))


def task1(black, brown, red, blue):
    sum = black + brown + red + blue
    return simpleprob(red + blue, sum)


def task2():
    return simpleprob(combinations(8, 2) + combinations(8, 1), combinations(10, 2))


def task3():
    return 1 - round(simpleprob(combinations(8, 3), combinations(10, 3))/100, 3)


def task4(p1, p2, p3, p4):
    return round((1 - p1 - p2 - p3 - p4) * 100, 2)


def task5(total, choose, take):
    return round((plcmntWrep(choose, take) / plcmntWrep(total, take)) * 100, 2)


def task6(prob1, prob2):
    return round((prob1 * prob2) * 100, 2)


def task7(CountBest, CountGood, CountMiddle, CountBad, PrepBest, PrepGood, PrepMiddle, PrepBad, TotalCountOfStud, NumbOfAllTasks,
          mark):
    bestProb = prob7task(CountBest, PrepBest, TotalCountOfStud, NumbOfAllTasks)
    goodProb = prob7task(CountGood, PrepGood, TotalCountOfStud, NumbOfAllTasks)
    middleProb = prob7task(CountMiddle, PrepMiddle, TotalCountOfStud, NumbOfAllTasks)
    badProb = prob7task(CountBad, PrepBad, TotalCountOfStud, NumbOfAllTasks)

    totalProb = bestProb + goodProb + middleProb + badProb

    match mark:
        case "Best":
            return round((bestProb / totalProb) * 100, 2)
        case "Good":
            return round((goodProb / totalProb) * 100, 2)
        case "Middle":
            return round((middleProb / totalProb) * 100, 2)
        case "Bad":
            return round((badProb / totalProb) * 100, 2)
        case _:
            return "Wrong mark"

def task8(first, second, third, probFrist, probSecond, probThird):
    return (probof2(first, probFrist) + probof2(second, probSecond) + probof2(third, probThird)) * 100


def task9(first, second, third, probFrist, probSecond, probThird):
    probOfPer = probof2(second, probSecond)
    probOfAll = probof2(first, probFrist) + probOfPer + probof2(third, probThird)
    return round((probOfPer / probOfAll) * 100, 2)


def task10(first, second, probFrist, probSecond):
    probOfHigh = probof2(first, probFrist)
    probOfMed = probof2(second, probSecond)
    probOfAll = probOfHigh + probOfMed
    return round((probOfHigh / probOfAll) * 100, 2)

print("\n\t\tMenu")
print("1. - Task 1")
print("2. - Task 2")
print("3. - Task 3")
print("4. - Task 4")
print("5. - Task 5")
print("6. - Task 6")
print("7. - Task 7")
print("8. - Task 8")
print("9. - Task 9")
print("10. - Task 10")
print("0. - Exit program")

while(True):
    print("\n\nChoose the number of task:")
    key = int(input())
    match key:
        case 1: print("\nTask 1 - probability: ", str(task1(40, 26, 22, 12)), "%")
        case 2: print("\nTask 2 - probability: ", str(task2()), "%")
        case 3: print("\nTask 3 - probability: ", str(round(task3(), 2)*100), "%")
        case 4: print("\nTask 4 - probability: ", str(task4(0.15, 0.25, 0.2, 0.1)), "%")
        case 5: print("\nTask 5 - probability: ", str(task5(120, 80, 2)), "%")
        case 6: print("\nTask 6 - probability: ", str(task6(0.9, 0.8)), "%")
        case 7: print("\nTask 7 - probability: ", "\nBest mark:", str(task7(3, 4, 2, 1, 20, 16, 10, 5, 10, 20, "Best")), "%","\nBad mark:",str(task7(3, 4, 2, 1, 20, 16, 10, 5, 10, 20, "Bad")), "%")
        case 8: print("\nTask 8 - probability: ", str(task8(0.4, 0.3, 0.3, 0.9, 0.95, 0.95)), "%")
        case 9: print("\nTask 9 - probability: ", str(task9(0.4, 0.3, 0.3, 0.8, 0.7, 0.85)), "%")
        case 10: print("\nTask 10 - probability: ", str(task10(0.3, 0.7, 0.9, 0.8)), "%")
        case 0: break






