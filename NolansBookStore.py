hardCover = 7.49
softCover = 2.99
magazine = 2.79

print("----- Self Checkout -----")

# Asks users for what they are purchasing
def purchase():
    hc = int(input("How many hard cover books are you purchasing? "))
    if hc > 5:
        print(f"Hard cover limit reached. Please put {hc - 5} back.")
        hc = 5
    else:
        pass
    sc = int(input("How many soft cover books are you purchasing? "))
    if sc > 5:
        print(f"Soft cover limit reached. Please put {sc - 5} back.")
        sc = 5
    else:
        pass
    mag = int(input("How many magazines are you purchasing? "))
    if mag > 5:
        print(f"Magazine limit reached. Please put {mag - 5} back.")
        mag = 5
    else:
        pass

# Shows user what they ordered and if they want to continue or not
    print(f"Hardcover books: {hc}")
    print(f"Softcover books: {sc}")
    print(f"Magazines: {mag}")

    order()

    # Calculates total

    total(hc, sc, mag)

def order():
    while True:
        ans = input('Does your oder look correct? (y/n) ').lower()
        if ans == 'y':
            break
        elif ans == 'n':
            purchase()
        else:
            print("Unsupported response, try again.")

def total(x, y, z):
    discount = 1

    while True:
        member = input("Are you a loyalty member? (y/n) ").lower()
        if member == 'y':
            discount = .05
            break
        elif member == 'n':
            discount = 0
            break
        else:
            print("Unsupported input, try again.")

    # Calculates SubTotal

    subTotal = (x * hardCover) + (y * softCover) + (z * magazine)

    # Calculates Discounts

    discounts = subTotal * discount

    # Calculates Sales Tax

    if discounts == 0:
        salesTax = subTotal * .07
    else:
        salesTax = (subTotal - discounts) * .07

    # Calculates Total

    purchaseTotal = (subTotal - discounts + salesTax)

    # Prints Reciept

    print("--------------- Receipt ----------------")
    print(f"Hardcover books:                      {x}")
    print(f"Softcover books:                      {y}")
    print(f"Magazines:                            {z}")
    print("----------------------------------------")
    print(f"SUBTOTAL:                         ${subTotal:.2f}")
    print(f"DISCOUNTS:                        ${discounts:.2f}")
    print(f"NC SALES TAX:                     ${salesTax:.2f}")
    print(f"TOTAL:                            ${purchaseTotal:.2f}")
    print("----------------------------------------")
    print("Thank you for shopping at Nolan's Used Book Store!")

purchase()
