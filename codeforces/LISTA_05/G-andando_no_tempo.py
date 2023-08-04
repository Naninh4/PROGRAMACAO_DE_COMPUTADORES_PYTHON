cred1, cred2, cred3 = map(int, input().split())

if cred1 == cred2 or cred3 == cred1 or cred2 == cred3:
    print("S")
elif cred1 + cred2 == cred3 or cred1 + cred3 == cred2 or cred2 + cred3 == cred1:
    print("S")
else:
    print("N")