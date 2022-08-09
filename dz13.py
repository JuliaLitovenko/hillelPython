class Human:

    def __init__(self, name:str, lastname:str, birth_date:str, sex:str, energy:int):
        self.name = name
        self.lastename = lastname
        self.birth_date = birth_date
        self.sex = sex
        self.energy = energy

    def eat(self):
        self.energy = self.energy + 5
        return f"{self.name} has {self.energy} energy"
    def sleep(self):
        energy += 10
        return f"{self.name} has {self.energy} energy"
    def talk(self):
        energy -= 5
        return f"{self.name} has {self.energy} energy"
    def walk(self):
        energy -= 10
        return f"{self.name} has {self.energy} energy"
    def make_homework(self):
        energy -=90
        return f"{self.name} has {self.energy} energy"
    def energy_count(self):



human1 = Human(name='Ben', lastname='Black', birth_date='15.02.77', sex='male', energy=100)
human2 = Human(name='John',
                   lastname='Mask',
                   birth_date='07.04.35',
                   sex='male',
                   energy=100)
human3 = Human(name='Karlos',
                   lastname='Mex',
                   birth_date='22.11.96',
                   sex='male',
                   energy=100)

human4 = Human(name='Bella',
                   lastname='Monroe',
                   birth_date='14.09.53',
                   sex='female',
                   energy=100)

human5 = Human(name='Maria',
                   lastname='Bend',
                   birth_date='03.08.81',
                   sex='female',
                   energy=100)



print()
