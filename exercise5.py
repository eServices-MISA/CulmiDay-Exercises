'''
While Loops
'''
count = 0
with open("data.txt", "__________") as file:
    for __________ in file:
        if line.strip() __________ "":
            count += 1
print("Non-empty lines:", count)