

print('kankuliyator yoki kvadrat tenglamalardan bittasini tanlang')
assa = input('tendlama yoki hisob ')
if assa == "hisob" :
    print('sonlar ustida amallar bajaruvchi dastur')
    print('dasturni boshidan boshlan uchun xx deb yozing')

    while True:
        a = int(input('a='))
        b = int(input('b='))
        q=input('+/-/*/div/**:')
        if q=='+':
            c=a+b
        elif q=='-':
            c=a-b
        elif q=='*':
            c=a*b
        elif q=='div':
            c==a/b
        elif q=='**':
            c=a**b
        else:
            c='xx'
            continue
        print('javobi=',c)
else:
    from math import*
    a = int(input('son kirit a ='))
    b = int(input('son kirit b ='))
    c = int(input('son kirit c ='))
    D = (b**2)-4*a*c
    if D > 0:
        x1=(-b+sqrt(D))/2*a
        x2=(-b-sqrt(D))/2*a
        print(x1, x2)
    elif D == 0:
        x = -b/2*a
        print(x)
    else:
        print('yechim yuq')

