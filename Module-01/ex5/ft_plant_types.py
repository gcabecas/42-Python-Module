class Plant:
    def __init__(self, name, height_cm, age_days):
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days


class Flower(Plant):
    def __init__(self, name, height_cm, age_days, color):
        super().__init__(name, height_cm, age_days)
        self.color = color

    def bloom(self):
        print(self.name, "is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name, height_cm, age_days, trunk_diameter):
        super().__init__(name, height_cm, age_days)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        shade_area = self.trunk_diameter * 1.5
        print(self.name, "provides", shade_area,
              "square meters of shade")


class Vegetable(Plant):
    def __init__(self, name, height_cm, age_days,
                 harvest_season, nutritional_value):
        super().__init__(name, height_cm, age_days)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show_nutrition(self):
        print(self.name, "is rich in", self.nutritional_value)


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    rose = Flower("Rose", 25, 30, "red")
    print(rose.name, "(Flower):", rose.height_cm, "cm,",
          rose.age_days, "days,", rose.color, "color")
    rose.bloom()

    tulip = Flower("Tulip", 20, 25, "yellow")
    print(tulip.name, "(Flower):", tulip.height_cm, "cm,",
          tulip.age_days, "days,", tulip.color, "color")
    tulip.bloom()

    oak = Tree("Oak", 500, 1825, 50)
    print(oak.name, "(Tree):", oak.height_cm, "cm,",
          oak.age_days, "days,", oak.trunk_diameter, "cm diameter")
    oak.produce_shade()

    pine = Tree("Pine", 600, 2190, 40)
    print(pine.name, "(Tree):", pine.height_cm, "cm,",
          pine.age_days, "days,", pine.trunk_diameter, "cm diameter")
    pine.produce_shade()

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    print(tomato.name, "(Vegetable):", tomato.height_cm, "cm,",
          tomato.age_days, "days,", tomato.harvest_season, "harvest")
    tomato.show_nutrition()

    carrot = Vegetable("Carrot", 30, 75, "fall", "vitamin A")
    print(carrot.name, "(Vegetable):", carrot.height_cm, "cm,",
          carrot.age_days, "days,", carrot.harvest_season, "harvest")
    carrot.show_nutrition()
