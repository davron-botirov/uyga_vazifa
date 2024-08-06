#Botirov Davronbek
from os import system
system("color 2")
system("cls")

data = """
1,c098529b-4f74-421e-8636-5da700c68b77,Plastic,$1295.11,true
2,1476954c-e2dd-4355-a944-3b1a94cd4bbf,Brass,$1273.17,false
3,647be64d-eb7b-43dc-a478-55c660840742,Wood,$819.94,false
4,e403a8dd-166a-4fc5-a6af-e6527c474a7e,Steel,$1346.68,false
5,6d186463-d800-42a9-80e1-0b2af3a035ce,Plexiglass,$821.53,false
6,95500f55-7fe3-4256-a0d5-433b8f3b9ebf,Wood,$1167.68,true
7,43cfc22d-7f7b-4068-a54d-a467266ae7dc,Wood,$1221.45,false
8,3a6b59e9-5539-41ca-bbd3-f045866196e8,Plexiglass,$849.08,true
9,f53ac49f-8b94-4a74-8906-7c8e3bdc8b2f,Glass,$1216.01,false
10,42d54d01-6427-401d-b84d-358cc6923fdd,Vinyl,$670.39,false
"""
lines = data.strip().split("\n")
products = []
for line in lines:
    parts = line.split(",")
    product = {
        "id": int(parts[0]),
        "product_code": parts[1],
        "material": parts[2],
        "price": float(parts[3].replace("$", "")),
        "is_available": parts[4].strip().lower() == "true"
    }
    products.append(product)
print("500 va 1000 dollar orasida bo'lgan va omborda mavjud bo'lgan produktlar:")
for product in products:
    if 500 <= product["price"] <= 1000 and product["is_available"]:
        print(f"1-misol: ID: {product['id']}, Material: {product['material']}")
print("\n")

# 2. Foydalanuvchi kiritgan material uchun omborda mavjud bo'lgan produktlar narxlarini o'sish tartibida chiqarish
user_material = input("2-misol: Material nomini kiriting: ").capitalize()
filtered_products = [p for p in products if p["material"] == user_material and p["is_available"]]
filtered_products.sort(key=lambda x: x["price"])
print(f"{user_material} materiali uchun omborda mavjud bo'lgan produktlar narxlari:")
for product in filtered_products:
    print(f"2-misol: ID: {product['id']}, Narx: ${product['price']}")
print("\n")

# 3. Omborda mavjud bo'lmagan va narxi 1000 dollardan arzon bo'lgan tovarlarning materiali
print("Omborda mavjud bo'lmagan va narxi 1000 dollardan arzon bo'lgan tovarlarning materiali:")
for product in products:
    if not product["is_available"] and product["price"] < 1000:
        print(f"3-misol: Material: {product['material']}")