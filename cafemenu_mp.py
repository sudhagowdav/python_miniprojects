#defining menu
menu ={
    'classsic hot coffee':150,
    'Americano':220,
    'cappaccino':283,
    'cold coffee':320,
    'caramel':370,
    'black tea':295,
    'green tea':295
}
print(menu)

print("welcome to cafe")
print("classsic hot coffee: Rs 150\nAmericano: Rs 220\ncappaccino: Rs 283\ncold coffee: Rs 320\ncaramel: Rs 370\nblack tea: Rs 295\ngreen tea: Rs295")
order_total = 0

item_1 = input("enter the item you want to order = ")
if item_1 in menu :
    order_total += menu[item_1]
    print(f"your item {item_1} has beign added to order")
else :
    print(f"ordered item {item_1} is not available")

another_order = input("do you want to order another item ? (yes/no)")
if another_order == "yes":
    item_2 = input("enter the item you want to order = ")
    if item_2 in menu :
        order_total += menu[item_2]
        print(f"your item {item_2} has beign added to order")
    else :
        print(f"ordered item {item_2} is not available")

print(f"the total amount to pay is {order_total}")