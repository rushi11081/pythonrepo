file = open('test')
# print(file.read())
# print(file.read(2))
#print(file.readline())
#print(file.readline())
print(file.readline())

line = file.readline()
while line != "":
    print(line)
    line = file.readline()


for line in file.readlines():
    print(line)

file.close()
