dish_name = "Aaloo paratha"
print("I love to eat " + dish_name)

order_quantity = 2
order_rate = 50.50

dhaba_items = ["Aaloo paratha", "Paneer paratha", "Gobi paratha", "Methi paratha"]
print("Dhaba items: " + str(dhaba_items))

dhaba_menu = {
    "Aaloo paratha": 50.50,
    "Methi paratha": 45.00  }
print(dhaba_menu)

print(type(order_quantity))
print(type(order_rate))

print(type(str(order_quantity)))


print("Order quantity: " + str(order_quantity))
print("Order rate: " + str(order_rate))


print("Order quantity: ", order_quantity)

print("-------Billing Section-------")
order_a_quantity = 2
order_a_rate = 50.50

total_a = order_a_quantity * order_a_rate
print("Total for order A: " + str(total_a))

order_b_rate = 60.00
total_b = order_b_qantity * order_b_rate
print("Total for order B: " + str(total_b))

total_bill = total_a + total_b
print("Total bill amount: " + str(total_bill))



cash_given = 500.00
change = cash_given - total_bill
print("Change to be returned: " + str(change))

budget = 1000.00
max_parathas = (budget // paratha_cost)
print("Maximum parathas that can be bought with the budget: " + str(max_parathas))
