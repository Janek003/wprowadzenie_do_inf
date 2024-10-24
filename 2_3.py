num = int(input("enter a num: "))
sum = num
product = num

while sum < 255 and product < 50000:
    #print(f"sum is: {sum}\nproduct is: {product}")
    num = int(input("enter another num: "))
    sum += num
    product = product * num

print(f'conditions reached: \nsum: {sum}\nproduct: {product}')