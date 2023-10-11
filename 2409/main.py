
def transformation():
    list_ = [("кружка", 300), ("стакан", 400), ("кофе 500гр", 800)]
    res ={}
    for i in list_:
        res[i[0]] = i[1]

    return res
list_  = transformation()



purchase_amount = 0
for i in list_.values():
    purchase_amount += i
print(purchase_amount)