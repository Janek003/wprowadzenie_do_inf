def main():
    n = int(input("n>2, parzysta, n: "))
    if n < 2 or n % 2: return

    a = [int(input("cyfra: ")) for _ in range(n)]
    ind = len(a)//2

    print((a[ind]+a[ind-1])/2)

if __name__ == __name__:
    main()