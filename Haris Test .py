class Greeting:
    Greeting = 'BMW'

    def __init__(self, name, classes, Rollno):
        self.name = name
        self.classes = classes
        self.Rollno = Rollno

    def __str__(self):
        return f'Name: {self.name} \nClass: {self.classes} \nRollno: {self.Rollno} '


std = Greeting('Haris', 11, 322162)
print(std)
