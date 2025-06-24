def sumandavg(n):
    if not n:
        return 0,0
    
    total = sum(n)
    avg = total/len(n)
    return total, avg

numbers= input("enter numbers: ")
n= list(map(float, numbers.split()))
total,avg = sumandavg(n)

print(f"Sum= {total}")
print(f"Avg={avg}")
