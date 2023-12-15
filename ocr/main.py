import easyocr

reader = easyocr.Reader(['en'])

results = reader.readtext('good1.jpg')

print(results)