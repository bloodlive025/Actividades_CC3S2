class Question:
    def __init__(self, description, options, correct_answer):
        self.description = description  # Descripción de la pregunta
        self.options = options          # Opciones posibles de respuesta
        self.correct_answer = correct_answer  # Respuesta correcta

    def is_correct(self, answer):
        # Compara la respuesta dada con la respuesta correcta
        return self.correct_answer == answer


class Quiz:
    def __init__(self):
        self.questions = []  # Lista para almacenar preguntas del cuestionario
        self.current_question_index = 0  # Índice de la pregunta actual

    def add_question(self, question):
        # Añade una pregunta al cuestionario
        self.questions.append(question)

    def get_next_question(self):
        # Devuelve la siguiente pregunta en el cuestionario
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        return None  # Devuelve None si no hay más preguntas
