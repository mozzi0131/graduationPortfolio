import LSH_TEST
import pythondbtest

result = LSH_TEST.analyzingFile('testing_siren.wav')

pythondbtest.insertData(result)

