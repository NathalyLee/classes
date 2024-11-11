from Autos.cars import Car
from Autos.trucks import Big

bmw = Car("BMW X5", "2023", "3,0 л", "12 989 000 руб.",
            "12 200 км")
truck = Big("Грузовик Foton S120", "2023", "3,8 л", "6 500 000 руб.",
            "50 000 км")

print (bmw.descrition())
print (truck.description())