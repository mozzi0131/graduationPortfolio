import soundClassification
import insertingClassifiedData
import checkValidInput


def processingSnd(filename,userID):
    print("processingSnd")
    result = soundClassification.analyzingFile(filename)

    print(filename)

    if result==0:
        print("siren")
        title = "사이렌 소리"
    elif result==1:
        print("fire alarm")
        title = "화재경보기 소리"
    elif result==2:
        print("boiling water")
        title = "물 끓는 소리"
    elif result == 3:
        print("dog")
        title = "개 짖는 소리"

    returnVal = checkValidInput.checkValidData(result,userID)

    if returnVal == True:
        print("now we can input data")
        insertingClassifiedData.insertData(result,userID)

    else:
        print(returnVal)
        print("we cannot input data because you not allowed")
