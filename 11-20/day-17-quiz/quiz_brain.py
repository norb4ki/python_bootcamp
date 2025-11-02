class QuizBrain:
  def __init__(self, list):
    self.question_list = list
    self.question_number = 0

  def still_has_questions(self):
    return self.question_number < len(self.question_list)

  def next_question(self):
    question = self.question_list[self.question_number]
    self.question_number += 1
    answer = input(f"Q.{self.question_number}: {question.text} (true/false) ").lower()
    
    if answer == question.answer.lower():
      print("You're right")
