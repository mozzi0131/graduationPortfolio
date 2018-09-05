import urban_sound_classifier2
import pythondbtest
import insertingClassifiedData

def processingSnd(filename):
    result = urban_sound_classifier2.analyzingFile(filename)

    print(filename)

    if result==0:
        print("siren")
    elif result==1:
        print("fire alarm")
    elif result==2:
        print("boiling water")
    elif result == 3:
        print("dog")

    insertingClassifiedData.insertData(result)
