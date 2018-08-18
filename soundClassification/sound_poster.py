import LSH_TEST
import pythondbtest

result = LSH_TEST.analyzingFile('testing_dogbark.wav')

if result==0:
    print("siren")
elif result==1:
    print("fire alarm")
elif result==2:
    print("boiling water")
elif result == 3:
    print("dog")
