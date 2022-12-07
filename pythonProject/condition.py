greeting = "good morning"

if greeting == "good morning":
    print("match")
else:
    print("not match")

print("hi")

# for loop

obj = [1, 2, 3, 4, 5]

for i in obj:
    print(i * 2)

add = 0
for j in range(1, 6):
    add = add + j
    print(add)

print("***************")
for k in range(1, 10, 2):
    print(k)

print("***************")
for m in range(10):
    print(m)

try:
    with open('test', 'r') as reader:
        print(reader.read())
except Exception as e:
    print(e)
