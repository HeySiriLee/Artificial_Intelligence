import easyocr

reader = easyocr.Reader(['en', 'ko'])

result = reader.readtext('./test_data/car02_02.jpg')

for message in result:
    print(message[1])