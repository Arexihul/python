# Question

class Question:
     def __init__(self, text, choices, answer):
          self.text = text
          self.choices = choices
          self.answer = answer

     def checkAnswer(self, answer):
          return self.answer == answer

# Quiz

class Quiz:
     def __init__(self, questions):
          self.questions = questions
          self.score = 0
          self.questionIndex = 0
          print(f"Test {len(questions)} sorudan oluşmaktadır ve her soru 20 puandır. Başarılar!")

     def getQuestion(self):
          return self.questions[self.questionIndex]

     def displayQuestion(self):
          question = self.getQuestion()
          print(f"Soru {self.questionIndex + 1}: {question.text}")

          for q in question.choices:
               print(q)
          
          answer = input("Cevabınız: ")
          self.guess(answer)
          self.loadQuestion()

     def guess(self, answer):
          question = self.getQuestion()

          if question.checkAnswer(answer):
               self.score += 20
          self.questionIndex += 1

     def loadQuestion(self):
          if len(self.questions) == self.questionIndex:
               self.showScore()
          else: 
               self.displayQuestion()
               
     def showScore(self):
          print(f"Test sona erdi. Skorunuz: {self.score}")


q1 = Question("En iyi programlama dili hangisidir?", ["a) C#", "b) Python", "c) Javascript", "d) Java"], "b")
q2 = Question("En popüler programlama dili hangisidir?", ["a) C#", "b) Javascript", "c) Java", "d) Python"], "d")
q3 = Question("En çok kazandıran programlama dili hangisidir?", ["a) Python", "b) Java","c) C#", "d) Javascript"], "a")
q4 = Question("En basit programlama dili hangisidir?", ["a) Java", "b) Javascript","c) C#", "d) Python"], "d") 
q5 = Question("En temel programlama dili hangisidir?", ["a) Javascript", "b) C#","c) Python", "d) Java"], "c") 
questions = [q1,q2,q3,q4,q5]

quiz = Quiz(questions)

quiz.displayQuestion()

