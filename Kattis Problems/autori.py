#string

fullName=input()
size_name=len(fullName)
finalAns=""
first_char=fullName[0]

finalAns= finalAns + first_char

for i in range(size_name):
    if fullName[i] == '-':
        finalAns = finalAns + fullName[i+1]

print(finalAns)
