list = []
elementy_3plus = []
is_sym = True

while True:
    given = int(input('val: '))
    if given == 0: break
    
    list.append(given)

for item in list:
    if list.count(item) > 2 and not item in elementy_3plus:
        print(item)
        elementy_3plus.append(item)