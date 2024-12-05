from True_data import question_data

# Define the Question class
class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0  

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_question(self):
        # Return True if there are more questions, otherwise False
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        # Compare user's answer and correct answer (case-insensitive)
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        # Print correct answer and score
        print(f"The correct answer was {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}.\n")

# Initialize an empty list to store questions
question_bank = []

# Loop through the question data and create Question objects
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Initialize the quiz and call next_question method
quiz = QuizBrain(question_bank)

# Continue asking questions while there are questions remaining
while quiz.still_has_question():
    quiz.next_question()
 