class Flower:
    def __init__(self, name, price, lifespan):
        self.name = name
        self.price = price
        self.lifespan = lifespan


class Accessory:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Bouquet:
    def __init__(self):
        self.flowers = []
        self.accessories = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def add_accessory(self, accessory):
        self.accessories.append(accessory)

    def calculate_cost(self):
        return sum(flower.price for flower in self.flowers) + sum(accessory.price for accessory in self.accessories)

    def average_lifespan(self):
        if not self.flowers:
            return 0
        return sum(flower.lifespan for flower in self.flowers) / len(self.flowers)

    def sort_by_price(self):
        self.flowers.sort(key=lambda flower: flower.price)

    def is_flower_in_bouquet(self, flower_name):
        return any(flower.name == flower_name for flower in self.flowers)


rose = Flower("Роза", 8, 7)
tulip = Flower("Ромашка", 4, 5)
ribbon = Accessory("Пион", 15)

bouquet = Bouquet()
bouquet.add_flower(rose)
bouquet.add_flower(tulip)
bouquet.add_accessory(ribbon)

print(f"Общая стоимость букета: {bouquet.calculate_cost()} byn")
print(f"Средняя продолжительность жизни цветов: {bouquet.average_lifespan()} дней")

bouquet.sort_by_price()
for flower in bouquet.flowers:
    print(f"{flower.name}: {flower.price} byn")

print(f"Роза в букете? {bouquet.is_flower_in_bouquet('Роза')}")
print(f"Лилия в букете? {bouquet.is_flower_in_bouquet('Лилия')}")