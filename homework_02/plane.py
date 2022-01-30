from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload
"""
создайте класс `Plane`, наследник `Vehicle`
"""


class Plane(Vehicle):

    def __init__(self, max_cargo=30):
        super().__init__()
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, cargo):
        if cargo+self.cargo < self.max_cargo:
            self.cargo += cargo
        else:
            raise CargoOverload("Too much cargo to load!")

    def remove_all_cargo(self):
        removed_cargo = self.cargo
        self.cargo = 0
        return removed_cargo
