# class App:
#     def __init__(self,capacity,user):
#         self.cap = capacity
#         self.usr = user

#     def login(self):
#         if self.usr =="main" :
#             print("hello")
#         else :
#             print("invalid user")

#     def increase_capacity(self,capacity):
#         self.cap += capacity
#         print("total capacity is",self.cap)

# a =App(20,"main")
# a.login()
# a.increase_capacity(20)

# b = App(30,"balaji")
# b.login()
# b.increase_capacity(40)

class OnlineClass:
    def __init__(self,course,instructor):
        self.course = course
        self.instructor = instructor
        self.students = []

    def enroll_student(self,name):
        self.students.append(name)
        print(f"{name} has been enrolled to {self.course} !")
    
    def course_details(self):
        print(f"course :{self.course}")
        print(f"instructor : {self.instructor}")
        print(f"enrolled students = {self.students}")

st1 = OnlineClass("c","balaji")
st1.enroll_student("hari")
st1.course_details()