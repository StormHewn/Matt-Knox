class Student:
    def __init__(self, fname: str, lname: str, districtCode: str, credits: int):
        if " " not in (fname := fname.title()):
            self.fname = fname
        else: raise BaseException(f"First name contains spaces: {fname}")

        if " " not in (lname := lname.title()):
            self.lname = lname
        else: raise BaseException(f"Last name contains spaces: {lname}")

        if (upperCode := districtCode.upper()) in ["I", "O"]:
            self.districtCode = upperCode
        else: raise BaseException(f"District code not found: {upperCode}")
        
        self.credits = credits

    def Lastname(self):
        return f"{self.fname} {self.lname}"

    def Tuition(self):
        match (self.districtCode):
            case "I":
                rate = 250
            case "O":
                rate = 500
            case _: raise BaseException(f"The district code \"{self.districtCode}\" sneaked through!")
        return self.credits * rate

inDistrictStudent = Student("Sticky", "Washington", "i", 30)
outOfDistrictStudent = Student("Constance", "Contraire", "o", 2)

print(f"{outOfDistrictStudent.Lastname()} owes ${outOfDistrictStudent.Tuition():.2f}")
print(f"{inDistrictStudent.Lastname()} owes ${inDistrictStudent.Tuition():.2f}")