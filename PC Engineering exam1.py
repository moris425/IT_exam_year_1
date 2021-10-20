x = input("rakam?")
if 0 <= int(x) <= 25:
    delta = input("işlem?")
    if str(delta) == str("/") or str(delta) == str("*"):
        multiple = 3  # ilk sonucun çarpanı
        afterOperation = 2  # deltaadan sonraki işlem
        power = 2  # ilk sonucun üssü
        factorial = 4  # faktoriel
        i = 2  # 30luk loop
        operation = 2  # + - belirlenmesinde kullanıldı
        variableFactorial = 4  # faktoriel işleminde
        bottomPower = 2  # alttakilerin üssü
        bottomNumber = 2
        xx = int(x)

        while int(i) < 32:
            print("Result after {}. term".format(int(i) - 1))
            while int(power) > 1:
                firstThing = int(xx) * int(x)
                xx = firstThing
                power = int(power) - 1
            else:
                firstThing = int(firstThing) * int(multiple)

            while int(factorial) == int(variableFactorial):
                variableFactorial = int(factorial) - 1
                oldResult = int(variableFactorial) * int(factorial)
            else:
                while int(variableFactorial) > 1:
                    variableFactorial = int(variableFactorial) - 1
                    result = int(oldResult) * int(variableFactorial)
                    oldResult = int(result)
                else:
                    newResult = int(result)
                    factorial = int(factorial) + 2
                    variableFactorial = factorial

            if int(newResult) > int(firstThing):
                bracket = int(firstThing)
            else:
                bracket = int(newResult)

            if str(delta) == str("/"):
                top = int(bracket) / int(afterOperation)
            else:
                top = int(bracket) * int(afterOperation)

            a = 0
            b = int(i) - 1
            looper = 0
            variableNumber = bottomNumber
            while int(a) < int(i):  # a = 0 in first run
                yy = int(bottomNumber)  # yy = 2 in first run
                if a == 0:
                    while int(b) > 0:  # b = 2 means it need to one loop
                        variablePlus = int(yy) * variableNumber  # 2*2 in first run
                        yy = variablePlus
                        b = b - 1
                    plus = variablePlus  # plus needs to be 64 in second loops first part
                    bottomNumber = bottomNumber + 2
                    variableNumber = bottomNumber
                else:
                    yy = int(variableNumber)
                    while int(b) > 0:
                        variablePlus = int(yy) * variableNumber
                        yy = variablePlus
                        b = b - 1
                    plus = plus + variablePlus
                    variableNumber = variableNumber + 2
                b = int(i) - 1
                a = a + 1
            bottom = plus

            testOperation = int(operation) / 2
            if str(testOperation)[-1:] == str("0"):
                realOperation = str("positive")
            else:
                realOperation = str("negative")

            if int(i) == 2:
                process = float(top) / float(bottom)
                processResult = float(process)
                print(processResult)
            else:
                process = float(top) / float(bottom)
                if realOperation == str("negative"):
                    process = float(process) - float(float(process) * 2)
                processResult = float(processResult) + float(process)
                print(float(processResult))








            i = int(i) + 1
            multiple = multiple + 4
            power = power + 3
            afterOperation = afterOperation + 5
            operation = operation + 1
    else:
        print("You can only write / or *")
    print("Result after all process: {}".format(processResult))
else:
    print("You need to write a number which it needs to be between 0 and 25")

