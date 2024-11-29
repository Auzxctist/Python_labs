def priv_user(name):
    print(f"Привет, {name}!")

priv_user("Алексей")

class Animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} говорит: {self.sound}")

cat = Animal("кошка", "мяу")

cat.make_sound()

class Dog(Animal):
    def __init__(self,name,sound,breed):    
        super().__init__(name,sound)
        self.breed = breed
    
    def show_breed(self):
        print(f"Это порода - {self.breed}")

dog = Dog("собака", "гав", "лабрадор")

dog.make_sound() 

dog.show_breed()