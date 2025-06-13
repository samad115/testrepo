print("Dominos Pizza Hut")
print('Menu card')
print('1. pizza')
print('2. Breadsticks')
print('3. pasta')
print('4. Burger')
print('5. cake')
print('6. chips')
order =[]
ch="y"
while ch=="y":
    n=int(input('enter your choice:'))
    if n == 1:
        itemname = 'pizza'
        if n in order:
            order.append(n)
    elif n == 2:
        itemname = 'breadsticks'
        if n in order:
            order.remove(n)
        else:
            print('sorry item is not available')
    elif n == 3:
       itemname = 'pasta'
    elif n == 4:
       itemname = 'burger'
    elif n == 5:
       itemname = 'cake'
    elif n == 6:
       itemname = 'chips'
    else:
        print('Invalid choice')
        continue
    order.append(itemname)
    ch=input("do you want to continue(y/n): ")
print('your order is:',order)
a=(input("enter item name to modify:"))
if a in order:
    i=order.index(a)
    m=(input('enter item name to replace:'))
    order[i]=m
else:
    print('sorry item is not available')
print('your order is :',order)