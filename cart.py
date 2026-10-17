"""Small sample product catalog and in-memory cart rules."""

PRODUCTS = [
    {"id": "beans", "name": "Ground coffee", "category": "Pantry", "price": 9.50, "stock": 8, "tags": ["coffee", "breakfast"]},
    {"id": "tea", "name": "Green tea", "category": "Pantry", "price": 6.00, "stock": 12, "tags": ["tea", "breakfast"]},
    {"id": "oats", "name": "Rolled oats", "category": "Pantry", "price": 4.25, "stock": 20, "tags": ["breakfast", "wholegrain"]},
    {"id": "soap", "name": "Unscented hand soap", "category": "Household", "price": 5.50, "stock": 10, "tags": ["household", "unscented"]},
    {"id": "towel", "name": "Cotton kitchen towel", "category": "Household", "price": 12.00, "stock": 6, "tags": ["household", "cotton"]},
]


def add_to_cart(cart, product_id, quantity=1):
    if quantity < 1:
        raise ValueError("quantity must be positive")
    product = next((p for p in PRODUCTS if p["id"] == product_id), None)
    if product is None:
        raise KeyError(product_id)
    updated = dict(cart)
    new_quantity = updated.get(product_id, 0) + quantity
    if new_quantity > product["stock"]:
        raise ValueError("requested quantity exceeds sample stock")
    updated[product_id] = new_quantity
    return updated


def remove_from_cart(cart, product_id):
    updated = dict(cart)
    if product_id not in updated:
        return updated
    if updated[product_id] > 1:
        updated[product_id] -= 1
    else:
        updated.pop(product_id)
    return updated


def subtotal(cart):
    return sum(
        product["price"] * cart.get(product["id"], 0)
        for product in PRODUCTS
    )


def recommend(cart, limit=3):
    selected = {p["id"] for p in PRODUCTS if cart.get(p["id"], 0) > 0}
    tags = {tag for p in PRODUCTS if p["id"] in selected for tag in p["tags"]}
    ranked = [
        (len(tags.intersection(p["tags"])), index, p)
        for index, p in enumerate(PRODUCTS)
        if p["id"] not in selected and tags.intersection(p["tags"])
    ]
    ranked.sort(key=lambda item: (-item[0], item[1]))
    return [row[2] for row in ranked[:limit]]
