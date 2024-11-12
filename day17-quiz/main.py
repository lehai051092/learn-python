from question_model import QuestionService
from quiz_brain import QuizBrain

question_service = QuestionService()
question_bank = question_service.get_items()
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

quiz.getResult()
