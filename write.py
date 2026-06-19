import datetime

def write_products(products, file_path="products.txt"):
    with open(file_path, 'w') as file:
        for product in products:
            line = product['name'] + ", " + \
                   product['brand'] + ", " + \
                   str(product['quantity']) + ", " + \
                   str(product['cost_price']) + ", " + \
                   product['country'] + "\n"
            file.write(line)

def generate_sale_invoice(items, total, customer_name):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = "SALE_" + customer_name + "_" + timestamp + ".txt"
    
    with open(filename, 'w') as file:
        file.write("=== SALES INVOICE ===\n")
        file.write("Date: " + str(datetime.datetime.now()) + "\n")
        file.write("Customer: " + customer_name + "\n")
        file.write("-" * 40 + "\n")
        
        for item in items:
            free_items = item['quantity'] // 3
            file.write("Product: " + item['name'] + "\n")
            file.write("Brand: " + item['brand'] + "\n")
            file.write("Quantity Paid: " + str(item['quantity']) + "\n")
            file.write("Free Items: " + str(free_items) + "\n")
            file.write("Unit Price: " + str(item['price']) + "\n")
            file.write("Subtotal: " + str(item['quantity'] * item['price']) + "\n")
            file.write("-" * 40 + "\n")
        
        file.write("TOTAL AMOUNT: " + str(total) + "\n")
        file.write("=" * 40 + "\n")


def generate_sale_invoice(items, total, customer_name):
    free_total = 0
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = "SALE_" + customer_name + "_" + timestamp + ".txt"

    with open(filename, 'w') as file:
        file.write("WeCare Skincare Store Invoice\n\n")
        file.write("Customer: " + customer_name + "\n\n")
        file.write("Product Details:\n")
        file.write("Product Name              Qty        Free Item            Total\n")
        file.write("----------------------------------------------------------------------\n")
        
        for item in items:
            free_items = item['quantity'] // 3
            line = "%-25s%-10d%-20dRs. %.2f\n" % (
                item['name'], item['quantity'], free_items, item['quantity'] * item['price']
            )
            file.write(line)
            free_total += free_items
        
        file.write("----------------------------------------------------------------------\n")
        file.write("Total Amount: Rs. %.2f\n" % total)
        file.write("Free Items: %d\n" % free_total)
        file.write("Thank you for shopping with us. We hope you had a great time!\n")

    print("Invoice generated as'%s' ," % filename)

