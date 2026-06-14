class Dog:
    species = "Canine"  # Class attribute

    def init__(self, name, age):
      self.name = name  # Instance attribute
      self.age = age  # Instance attribute

 #Creating an object of the Dog class
dog1 = Dog("Buddy", 3)
print(dog1.name) 
print(dog1.age)


from abc import ABC
class Animal(ABC):
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Bark")
    def sound(self):
        print("meow")
    

dog = Dog()
cat = Cat()
dog.sound()
cat.sound()

class student:
    def _init_(self,name,admission_no,cgpa):
        self.name=name
        self.admission_no=admission_no
        self.__cgpa=cgpa
      
    def get_cgpa(self):
        return self.__cgpa
    def set_cgpa(self,cgpa):
        if cgpa<0 or cgpa>10:
            print("invalid cgpa")
        else:
            self.__cgpa=cgpa


prashant = student("prashant",1333,8.7)
print(prashant.name)
print(prashant.admission_no)
print(prashant.get_cgpa())
prashant.set_cgpa(9.0)
print(prashant.get_cgpa())
