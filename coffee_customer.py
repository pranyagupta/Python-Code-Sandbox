import coffee_shop

# Output the information we know from the module
print("Welcome to", coffee_shop.shop_name)
print("Available sizes:", coffee_shop.coffee_sizes)
print("Available roasts:", coffee_shop.coffee_roasts)



while True:
    coffee = input("which coffee do you want and in which cup size??? : ")
    coffee_and_size = coffee.split(", ")
    if (coffee_and_size[0] in coffee_shop.coffee_roasts) and coffee_and_size[1] in coffee_shop.coffee_sizes:
        print("of course here you go with your", coffee, "coffee.")
        i = input("Thanks for choosing us. kindly give your remarks : ")
        print("thank you for your remarks.")
        break
    else :
        print("sorry! this kind of roast is not available in our shop")
        print("you can choose from [hot chocolate', 'light', 'medium', 'dark', 'espresso'] ")
