def pizza_order(size, *toppings, **customization):
    print(f"Pizza size: {size}")
    print("Toppings:", toppings)
    print("Custom options:", customization)

pizza_order("Medium", "Olives", "Mushrooms", extra_cheese=True, crust="thin")