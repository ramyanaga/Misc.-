class Employee: 
	def __init__(self,name,salary):
		self.__name = name 
		self.__salary = salary
		#self.__student1 = Student("Jenn",12).printInfo()
		#student1.printInfo()
		

	def printEmployeeInfo(self):
		self.__printName()
		self.__printSalary()

	def printName(self):
		print self.__name

	def printSalary(self):
		print self.__salary



"""
class Student: 
	def __init__(self, Sname, grade): 
		self.__name = Sname 
		self.__grade = grade 
		#self.__printEmployeeInfo()

		
	def printInfo(self):
		print self.__name
		print self.__grade
		self.printEmployeeInfo()
"""





#student1 = Student("Jenn",12)
#student1.printInfo()
#Student("Jenn",12).printInfo()

emp1 = Employee("Ramya",1000)
emp1.printEmployeeInfo()
#Employee("Ramya",1000).printInfo()
#emp1 = Employee("Ramya",1000)
#emp1.printInfo()
#student1 = Student("Jenn",12)
#student1.printInfo()
#emp1.printInfo()