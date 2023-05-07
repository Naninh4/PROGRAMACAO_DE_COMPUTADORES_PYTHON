base_folha,altura_folha = map(int,input().split())
base_foto1, altura_foto1=  map(int,input().split())
base_foto2, altura_foto2=  map(int,input().split())

if ((base_foto1 + base_foto2) <= base_folha) and ((altura_foto1 <= altura_folha) and (altura_foto2 <= altura_folha)):
    print("S")
elif((base_foto1 + altura_foto2) <= base_folha) and ((altura_foto1 <= altura_folha) and (base_foto2 <= altura_folha)):
    print("S")
elif((altura_foto1 + base_foto2) <= base_folha) and ((base_foto1 <= altura_folha) and (altura_foto2 <= altura_folha)):
    print("S")
elif((altura_foto1 + altura_foto2) <= base_folha) and ((base_foto1 <= altura_folha) and (base_foto2 <= altura_folha)):
    print("S")
elif ((base_foto1 + base_foto2) <= altura_folha) and ((altura_foto1 <= base_folha) and (altura_foto2 <= base_folha)):
    print("S")
elif((base_foto1 + altura_foto2) <= altura_folha) and ((altura_foto1 <= base_folha) and (base_foto2 <= base_folha)):
    print("S")
elif((altura_foto1 + base_foto2) <= altura_folha) and ((base_foto1 <= base_folha) and (altura_foto2 <= base_folha)):
    print("S")
elif((altura_foto1 + altura_foto2) <= altura_folha) and ((base_foto1 <= base_folha) and (base_foto2 <= base_folha)):
    print("S")
else:
    print("N")
