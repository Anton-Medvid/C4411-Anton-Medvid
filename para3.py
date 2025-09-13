import random
brand_of_cars = {
    "Megane":{'fuel':150, 'strength':150, 'consumption':2},
    "Lada":{'fuel':50, 'strength':40, 'consumption':10},
    "Tesla":{'fuel':95, 'strength':95, 'consumption':7},
    "Xiaomi":{'fuel':20, 'strength':20, 'consumption':100},
}
job_list = {
    "Java Developer": {'salary':50, 'gladness_less':10},
    "a Xiaomi factory employee": {'salary':100, 'gladness_less':2},
    "Farmer": {'salary':10, 'gladness_less':50},
}
class Human:
    def __init__(self, name='human', job=None,home=None,car=None):
        self.name = name
        self.car =car
        self.job =job
        self.home =home
        self.gladness = 50
        self.money = 100
        self.satiety = 50
    def get_car(self):
        self.car = Auto(brand_of_cars)
    def get_home(self):
        self.home = House()
    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
    def eat(self):
        if self.home.food <= 0:
            self.shopping('food')
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5
    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping('fuel')
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4
    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping('fuel')
                return
            else:
                if self.car.drive():
                    pass
                if manage == 'fuel':
                    print('i bought fuel')
                    self.money -= 100
                    self.car.fuel += 100
                elif manage == "food":
                    print('i bought food')
                    self.money -= 50
                    self.home.food += 50
                elif manage == "delicacies":
                    print('horray')
                    self.gladness += 10
                    self.satiety += 2
                    self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5
    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0
    def to_repair(self):
        self.car.strength += 100
        self.money -= 50
    def days_indexes(self, day):
        print(f'today the {day} of {self.name} life')
        print(f'money -{self.money}')
        print(f'Satiety - {self.satiety}')
        print('Home')
        print(f'Gladness - {self.gladness}')
        print(f'food - {self.home.food}')
        print(f'Mess - {self.home.mess}')
        print('Car')
        print(f'Fuel - {self.car.fuel}')
        print(f'Strength - {self.car.strength}')

    def is_alive(self):
        if self.gladness < 0:
            print('Depression')
            return False
        if self.satiety < 0:
            print('dead')
            return False
        if self.money < 500:
            print('bankrupt')
            return False
    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f'{self.car.brand}')
            if self.job is None:
                self.get_job()
                print(f'{self.job.job}')
            self.days_indexes(day)
            dice = random.randint (1 , 4)
            self.eat()
        elif self.gladness < 20:
            if self.home.mess < 15:
                self.clean_home()
            else:
                self.chill()
            elif self.money < 0
                self.work()
        elif self.car.strength < 15:


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]['fuel']
        self.consumption = brand_list[self.brand]['consumption']
        self.strength = brand_list[self.brand]['strength']

    def drive(self):
        if self.strength > 0 and self.fuel > self.consumption:
            self.strength -= 1
            self.fuel -= self.consumption
            return True
        else:
            print('The car not move')
            return False
class House:
    def __init__(self):
        self.mess = 0
        self.food = 0
class job:
    def __init__(self, job_list):
        self.job =  random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness_less = job_list[self.job]['gladness_less']








