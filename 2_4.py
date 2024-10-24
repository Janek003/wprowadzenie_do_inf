all_nums = []
curr_num = 0

while curr_num%2==0:
    curr_num = int(input("enter num: "))
    all_nums.append(curr_num)

print(max(all_nums))
print(min(all_nums))

potega = min(all_nums)

for i in range(max(all_nums)):
    potega *= min(all_nums)

print(potega)