# Цветочница.
# Определить иерархию и создать несколько цветов. Собрать букет с использованием аксессуаров с определением его стоимости.
# Определить время его увядания по среднему времени жизни всех цветов в букете.
# Позволить сортировку цветов стоимости
# Узнать, есть ли цветок в букете.


def create_flower(name, price, lifespan):
    return {"name": name, "price": price, "lifespan": lifespan}


def create_accessory(name, price):
    return {"name": name, "price": price}


def create_bouquet():
    return {"flowers": [], "accessories": []}


def add_flower(bouquet, flower):
    bouquet["flowers"].append(flower)


def add_accessory(bouquet, accessory):
    bouquet["accessories"].append(accessory)


def calculate_cost(bouquet):
    flower_cost = sum(flower["price"] for flower in bouquet["flowers"])
    accessory_cost = sum(accessory["price"] for accessory in bouquet["accessories"])
    return flower_cost + accessory_cost


def average_lifespan(bouquet):
    flowers = bouquet["flowers"]
    if not flowers:
        return 0
    return sum(flower["lifespan"] for flower in flowers) / len(flowers)


def sort_by_price(bouquet):
    bouquet["flowers"].sort(key=lambda flower: flower["price"])


def is_flower_in_bouquet(bouquet, flower_name):
    flowers = bouquet["flowers"]
    return any(flower["name"] == flower_name for flower in flowers)


rose = create_flower("Роза", 8, 7)
tulip = create_flower("Ромашка", 4, 5)
ribbon = create_accessory("Пион", 15)

bouquet = create_bouquet()
add_flower(bouquet, rose)
add_flower(bouquet, tulip)
add_accessory(bouquet, ribbon)

print(f"Общая стоимость букета: {calculate_cost(bouquet)} byn")
print(f"Средняя продолжительность жизни цветов в букете: {average_lifespan(bouquet)} дней")

sort_by_price(bouquet)
for flower in bouquet["flowers"]:
    print(f"{flower['name']}: {flower['price']} byn")

print(f"Роза в букете? {is_flower_in_bouquet(bouquet, 'Rose')}")
print(f"Лилия в букете? {is_flower_in_bouquet(bouquet, 'Lily')}")
