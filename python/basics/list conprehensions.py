#list comprehensions

prices=[10,20,30,40,50,60]
halved=[]
for price in prices:
    half_price=price/2
    halved.append(half_price)
print(halved)

prices=[10,220,30,40]
halved=[price/2 for price in prices]
print(halved)

meters=[100,2000,30000]
kilometers=[m/100 for m in meters]
print(kilometers)

miles=[100,20,39,40]
km=[value*1.609 for value in miles]
print(km)

ages=[15,16,34]
can_drive=[age>=18 for age in ages]
print(can_drive)
