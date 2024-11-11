class Car:
    def __init__(self, model, year, engine_size, price, mileage, wheels = 4):
        self.model = model
        self.year = year
        self.engine_size = engine_size
        self.price = price
        self.mileage = mileage
        self.wheels = wheels

    def descrition(self):
        descrition = (f"Модель - {self.model}, год выпуска - {self.year}, объём двигателя - {self.engine_size}, "
                      f"цена - {self.price}, пробег - {self.mileage}, количество колёс - {self.wheels}")
        return descrition


