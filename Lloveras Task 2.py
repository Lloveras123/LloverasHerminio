class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hi, I am {self.name}. I am {self.age} years old and I am studying {self.course}.")

# Create three student objects
student1 = Student("Herminio", 22, "Information Technology")
student2 = Student("Ronnel", 25, "Information Tungaw")
student3 = Student("Patrick", 22, "PhyLosopong")

# Call their introduce method
student1.introduce()
student2.introduce()
student3.introduce()
