housePos = int(input())

stepsRange = [1, 2, 3, 4, 5]
steps = 0
degree = 0
while housePos != 0:
    ostatok = housePos % 10
    if ostatok == 0:
        steps += 0
    else:
        if degree == 0:
            if ostatok in stepsRange:
                steps += 1
            else:
                i = 0
                while True:
                    ostatok -= stepsRange[i]
                    if ostatok not in stepsRange:
                        ostatok += stepsRange[i]
                        i += 1
                    else:
                        break
                steps += 2
        else:
            steps += (ostatok * 10 ** degree) // stepsRange[4]
    degree += 1
    housePos //= 10
print(steps)
