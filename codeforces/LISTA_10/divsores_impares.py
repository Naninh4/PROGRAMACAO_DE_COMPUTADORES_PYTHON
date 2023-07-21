def div(num, divisor=1):
    if(num==divisor):
        return 1
    else:
        if (num % divisor ==0):
            if divisor % 2 == 1:
                return 1 + div(num, divisor+1)
            else:
                return div(num, divisor+1)
        else:
            return div(num, divisor+1)
        
num = int(input())
print(div(num))
