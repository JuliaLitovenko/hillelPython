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
            self.energy = self.energy + 10
            return f"{self.name} has {self.energy} energy"
 def talk(self):
            self.energy = self.energy - 5
            return f"{self.name} has {self.energy} energy"
 def walk(self):
            self.energy = self.energy - 10
            return f"{self.name} has {self.energy} energy"
 def make_homework(self):
            self.energy = self.energy - 90
            return f"{self.name} has {self.energy} energy"


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

human1.eat()
human2.walk()
human3.talk()
human4.sleep()
human5.make_homework()
print(human1.name,human1.energy,human2.name,human2.energy,human3.name, human3.energy,human4.name , human4.energy,human5.name, human5.energy)
print(f"The biggest energy amount is {max(human1.energy,human2.energy,human3.energy,human4.energy,human5.energy)}")
