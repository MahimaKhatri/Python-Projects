w=int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper()=="L":
    c = w * 0.45;
    print(f"You are {c} kilos")
else:
    c = w / 0.45
    print(f"You are {c} pounds")

