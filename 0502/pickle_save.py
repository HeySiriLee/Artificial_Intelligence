import pickle 

saveFile = open("pFile.pickle", "wb")

saveData = {
    "name": "Siri",
    "age": 5,
    "lang": "Python"
}

pickle.dump(saveData, saveFile)
saveFile.close()