import pickle

pFile = open("pFile.pickle", "rb")

memData = pickle.load(pFile)

print(memData)

pFile.close()