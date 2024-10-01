class Person:
    def __init__(self, name, surname):
        self.name = name 
        self.surname = surname  

    def __add__(self, other):
        if isinstance(other, Person):
            return Person(self.name, other.surname)  
        return NotImplemented

    def __repr__(self):
        return f"{self.name} {self.surname}"
from person import Person

class Group:
    def __init__(self, name, people):
        self.name = name        
        self.people = people    

    def __add__(self, other):
        if isinstance(other, Group):
            combined_people = self.people + other.people 
            return Group(f"{self.name} & {other.name}", combined_people)  
        return NotImplemented

    def __len__(self):
        return len(self.people)

    def __repr__(self):
        return f"Group({self.name}, Members: {len(self.people)})"     
from person import Person
from group import Group

p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3  # p4 = Person('Warren', 'Musk')
first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group
print(len(third_group)) 
third_group = first_group + second_group        