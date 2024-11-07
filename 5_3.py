list = []
is_sym = True

while True:
    given = int(input('val: '))
    if given == 0: break
    
    list.append(given)

for i in range(len(list)//2):
    if not list[i] == list[-(i+1)]:
        print(list[i], list[-(i+1)])
        is_sym = False

if is_sym: print('Lista symetryczna')
else: print('Lista niesymetryczna')
