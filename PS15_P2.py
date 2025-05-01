# Base Car class
class Car:
    def __init__(self, make, model, sticker_price):
        self.make = make
        self.model = model
        self.sticker_price = sticker_price

    def discount_price(self):
        return 0.90 * self.sticker_price  # 90% of sticker price


# Derived Sport class
class Sport(Car):
    def __init__(self, make, model, sticker_price):
        super().__init__(make, model, sticker_price)
        self.sport_wheels = 'N'
        self.sport_engine = 'N'
        self.sport_interior = 'N'

    def add_sport_wheels(self, option):
        self.sport_wheels = option.upper()

    def add_sport_engine(self, option):
        self.sport_engine = option.upper()

    def add_sport_interior(self, option):
        self.sport_interior = option.upper()

    def price_with_options(self):
        base_price = self.discount_price()
        total_price = base_price

        if self.sport_wheels == 'Y':
            total_price += 5000.00
        if self.sport_engine == 'Y':
            total_price += 3000.00
        if self.sport_interior == 'Y':
            total_price += 7000.00

        return total_price

    def display_summary(self):
        print(f"Car: {self.make} {self.model}")
        print(f"Sticker Price: ${self.sticker_price:.2f}")
        print(f"Discount Price: ${self.discount_price():.2f}")
        print(f"Price with Options: ${self.price_with_options():.2f}")


# Test Program
car1 = Sport("Ford", "Mustang", 60000)

# Add options
car1.add_sport_wheels('Y')
car1.add_sport_engine('Y')
car1.add_sport_interior('N')  # Let's say we skip this one

# Display results
car1.display_summary()
