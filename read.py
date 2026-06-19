def read_products(file_path="products.txt"):
    products = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()  # remove newline and whitespace
                parts = line.split(', ')
                if len(parts) < 5:
                    continue  # skip malformed lines
                product = {
                    'name': parts[0],
                    'brand': parts[1],
                    'quantity': int(parts[2]),
                    'cost_price': int(parts[3]),
                    'country': parts[4]
                }
                products.append(product)
    except FileNotFoundError:
        print("Error: Products file not found.")
    return products
