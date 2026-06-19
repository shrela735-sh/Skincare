def purchase_product(products, product_name, brand, quantity, cost_price, country):
    for product in products:
        if product['name'] == product_name and product['brand'] == brand:
            product['quantity'] += quantity
            product['cost_price'] = cost_price
            break
    else:
        products.append({
            'name': product_name,
            'brand': brand,
            'quantity': quantity,
            'cost_price': cost_price,
            'country': country
        })
    return products

def sell_products(products, cart):
    total = 0
    sold_items = []
    for item in cart:
        for product in products:
            if product['name'] == item['name'] and product['brand'] == item['brand']:
                required = item['quantity'] + (item['quantity'] // 3)
                if product['quantity'] < required:
                    raise ValueError("Insufficient stock for " + product['name'])
                product['quantity'] -= required
                selling_price = product['cost_price'] * 2
                total += item['quantity'] * selling_price
                sold_items.append({
                    'name': product['name'],
                    'brand': product['brand'],
                    'quantity': item['quantity'],
                    'price': selling_price
                })
    return sold_items, total
