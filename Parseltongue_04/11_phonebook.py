dic1={}
dic2={}
with open("name.txt") as file:
    for line in file:
        (firstname, lastname) = line.strip().split(",")
        if firstname not in dic1:
            dic1[firstname] = [lastname]
        else:
            dic1[firstname] += [lastname]
print(dic1)

for key, value in dic1.items():
    print(key, value)
    print(f"{key} ({len(value)}): {value}")
