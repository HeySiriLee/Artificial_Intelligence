# File processing 
# open("File name", "mode", "encoding language")

# save 
# open("File name", "read", "encoding language")
saveExFile = open("exFile.txt", "w", encoding="utf=8" )

print("test1: Hello,", file = saveExFile)
print("test2: world!", file = saveExFile)

saveExFile.close()

# load 
<<<<<<< HEAD
# open("File name", "read", "encoding language")
=======
# 열꺼야("File name", "read", "encoding language")
>>>>>>> 60aba27 (교수님수업클론코딩듕)
loadExFile = open("exfile.txt", "r", encoding="utf=8")

while True:
    line = loadExFile.readline()
    
    if not line:
        break
    
    print(line, end="")

loadExFile.close()