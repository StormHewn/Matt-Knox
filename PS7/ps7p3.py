class Student:
    @staticmethod
    def codes():
        return {
            "I": 250,
            "O": 500,
            "X": 800,
            "G": 250
        }
    
    def __init__(self, fname: str, lname: str, districtCode: str, credits: int):
        if " " not in (fname := fname.title()):
            self.fname = fname
        else: raise BaseException(f"First name contains spaces: {fname}")

        if " " not in (lname := lname.title()):
            self.lname = lname
        else: raise BaseException(f"Last name contains spaces: {lname}")

        if (upperCode := districtCode.upper()) in self.codes():
            self.districtCode = upperCode
        else: raise BaseException(f"District code not found: {upperCode}")

        self.credits = credits

    def Fullname(self):
        return f"{self.fname} {self.lname}"

    def Tuition(self):
        rate = Student.codes()[self.districtCode]
        return self.credits * rate

students: list[Student] = []
students.append(Student("Reynie", "Muldoon", "i", 13))
students.append(Student("Sticky", "Washington", "g", 30))
students.append(Student("Kate", "Weatherall", "x", 7))
students.append(Student("Constance", "Contraire", "o", 2))

for student in students:
    print(f"{student.Fullname()} owes ${student.Tuition():.2f}")