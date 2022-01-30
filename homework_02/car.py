from homework_02.base import Vehicle
"""
создайте класс `Car`, наследник `Vehicle`
"""


class Car(Vehicle):

    def __init__(self, *args):
        super().__init__(*args)
        self.engine = None

    def set_engine(self, engine):
        self.engine = engine

