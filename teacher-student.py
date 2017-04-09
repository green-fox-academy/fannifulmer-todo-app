class Student():
    def learn(self):
        print('Learn: I am working on my todo app!')
    def question(self, teacher):
        teacher.answer()
class Teacher():
    def teach(self, student):
        student.learn()        
    def answer(self):
        print('Answer: Everything will be fine!')

Fanni = Student()
Margo = Teacher()
print("Will my code works?")
Fanni.question(Margo)
print("What are you studying right now?")
Margo.teach(Fanni)