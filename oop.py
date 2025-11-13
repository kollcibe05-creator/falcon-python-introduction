class Student:
    school ="Moringa school" #class attribute
    def __init__(self, name, unit="DSA", cohort=None,grade= 0.0, email =None):
        self.name = name #instance attribute
        self.cohort = cohort
        self.email = email
        self.unit = unit
        self.grade = grade
        
        pass
    
    # def get_grade(self):
    #     return self._grade
    #     pass
    
    # def set_grade(self, value):
    #     if isinstance(value, (int, float)) and 0.0 <= value <= 100.0:
    #         self._grade = float(value)
    #     else:
    #         raise ValueError("Grade must be between 0 and 100")
        
    # grade = property(get_grade, set_grade)
    
    # property and setter decorator
    @property
    def grade(self):
        return self._grade
        pass
    
    @grade.setter
    def grade(self,value):
        if isinstance(value, (int, float)) and 0 <= value >= 100:
            self._grade = float(value)
        else:
            raise ValueError("Grade must be between 0 and 100")
        
    
    
    def greet(self):
        print(f"Hello my name is {self.name} from {self.cohort} cohort and taking {self.unit} unit and scored {self.grade}.")
        
        
    pass

class Lecturer:
    pass

alice = Student("Alice", "SD", "August 2025", 100)
# bob = Student("Bob")

alice.greet()
# bob.greet()
# alice_school = alice.school
# bob_school = bob.school
# print(alice_school)
# print(bob_school)
# Bob.greet()
# alice.study("DSA")

# print(type(alice))
# print(type(1))