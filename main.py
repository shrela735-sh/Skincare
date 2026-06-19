from read import read_products
from write import write_products, generate_sale_invoice
from operation import purchase_product, sell_products

def display_products(products):
    print("\n=======================================WeCare SkinCare=======================================")
    print("\n                              Address: Chunikhel, Kathmandu")
    print("\n                                  Phone: +977-9800000000")
    print("-" * 100)
    print("\n------------------------------------------Available Products------------------------------------------")
    print("ID    Product Name           Brand        Qty        Sell Price      Country              ")
    print("-" * 100)

    for index, product in enumerate(products, start=1):
        sell_price = product['cost_price'] * 2
        print("%-6d%-22s%-20s%-10dRs. %-12.2f%-15s" % (
            index,
            product['name'],
            product['brand'],
            product['quantity'],
            sell_price,
            product['country']
        ))
    print("-" * 100)

def main():
    products = read_products()
    display_products(products)

    while True:
        print("\nThere are some options you need to choose from to continue the operations:")
        print("-" * 90)
        print("1. Sell")
        print("2. Purchase Products")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            customer_name = input("Enter customer name: ")
            cart = []
            while True:
                try:
                    product_id = input("Enter product ID (or 'done'): ")
                    if product_id.lower() == 'done':
                        break
                    product_id = int(product_id)
                    if product_id < 1 or product_id > len(products):
                        print("Invalid product ID.")
                        continue
                    quantity = int(input("Quantity: "))
                    product = products[product_id - 1]

                    free_qty = quantity // 3
                    print("\nYou will receive " + str(free_qty) + " free product(s) for purchasing " +
                          str(quantity) + " product(s) of " + product['name'] + ".")

                    cart.append({
                        'name': product['name'],
                        'brand': product['brand'],
                        'quantity': quantity
                    })
                except ValueError:
                    print("Please enter valid input.")

            try:
                sold_items, total = sell_products(products, cart)
                generate_sale_invoice(sold_items, total, customer_name)
                display_products(products)  # show updated stock
            except ValueError as e:
                print(str(e))

        elif choice == '2':
            product_name = input("Product name: ")
            brand = input("Brand: ")
            quantity = int(input("Quantity: "))
            cost_price = int(input("Cost price: "))
            country = input("Country: ")
            products = purchase_product(products, product_name, brand, quantity, cost_price, country)
            generate_sale_invoice([{
                'name': product_name,
                'brand': brand,
                'quantity': quantity,
                'price': cost_price
            }], quantity * cost_price, "PURCHASE")
            display_products(products)

        elif choice == '3':
            write_products(products)
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
