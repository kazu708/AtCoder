from decimal import Decimal
A , B = map(float,input().split(' '))


print(100 - (Decimal(B)/Decimal(A))*100)