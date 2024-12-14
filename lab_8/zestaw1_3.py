a = []

while True:
    curr = int(input("cyfra: "))
    if curr % 10 == 0: break
    a.append(curr)

print(min(a))
print(sum(a) / len(a))