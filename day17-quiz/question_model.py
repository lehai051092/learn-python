from data import question_data


class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


class QuestionService:

    def __init__(self):
        self.question_data = question_data

    def get_items(self):
        items = []

        for question in self.question_data:
            item = Question(question['text'], question['answer'])
            items.append(item)

        return items
