import json
import pandas
import numpy

x = pandas.read_excel('MappingDocumentExercise.xlsx')

# print(type(x))

p = x.head(0)
attributes = p.columns.values
list_attributes = numpy.ndarray.tolist(attributes)
list_attributes=list_attributes[0].split(',')
print(list_attributes)

data_list = numpy.ndarray.tolist(x.values)
print(data_list)
print(type(data_list))

result = []

for item in data_list:
    # print(item)
    item = item[0]
    kk = item.split(',')
    obj = {}

    if kk[0] != "":
        obj[list_attributes[0]] = kk[0]
    if kk[1] != "":
        obj[list_attributes[1]] = kk[1]
    if kk[2] != "":
        obj[list_attributes[2]] = kk[2]
    # print(obj)
    result.append(obj)

print(result)
jsonString = json.dumps(result)

print(jsonString)

jsonFile = open("welcome.json", "w")
jsonFile.write(jsonString)
jsonFile.close()