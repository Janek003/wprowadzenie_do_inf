import random
tab = [[random.randint(0,30) for _ in range(random.randint(5,10))] for _ in range(random.randint(3,7))]

for row in tab:
  for element in row:
    print(element, end=" ")
  print()

print()

for row in tab:
  if row[0] < row[1]:
    najmniejsza = row[0]
    druga_najmniejsza = row[1]
  else:
    najmniejsza = row[1]
    druga_najmniejsza = row[0]

  for i in range(2, len(row)):
    if row[i] < najmniejsza:
      druga_najmniejsza = najmniejsza
      najmniejsza = row[i]
      
    elif row[i] < druga_najmniejsza:
      druga_najmniejsza = row[i]
  suma = najmniejsza + druga_najmniejsza
  print(suma)