from abc import ABC
from homework_02.exceptions import EngineNotStarted, NotEnoughFuel, LowFuelError


class Vehicle(ABC):

    def __init__(self, weight=10, fuel=10, fuel_consumption=2):
        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError("Fuel level is low!")

    def move(self, distance):
        if self.fuel/self.fuel_consumption >= distance:
            self.fuel -= self.fuel_consumption*distance
        else:
            raise NotEnoughFuel("Not enough fuel for given distance!")
