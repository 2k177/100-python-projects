from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

q_data_obj_list = []
for data in question_data:
    q_data_obj_list.append(Question(data["text"], data["answer"]))

quiz_obj = QuizBrain(q_data_obj_list)

while quiz_obj.still_has_question():
    quiz_obj.next_question()
print("You've completed the quiz")
print(f"Your final answer is : {quiz_obj.score}/{len(quiz_obj.question_list)}")