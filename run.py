import os

DATA_DIRECTORY = "data/"
QUESTIONS_FILE_PATH = f"{DATA_DIRECTORY}questions.txt"


def get_questions() -> list:
    try:
        with open(QUESTIONS_FILE_PATH) as f:
            return [x.replace("\n", "") for x in f.readlines()]
    except FileNotFoundError:
        return []


if __name__ == "__main__":
    questions = get_questions()
    answers = []

    new_questions = False
    if questions == []:
        new_questions = True

    current_question_index = 0
    while True:
        current_question = ""
        try:
            current_question = questions[current_question_index]
            print(current_question)
        except IndexError:
            print("Neue Frage definieren: ('exit' um beantwortung zu beenden)")
            current_question = input()
            if current_question == "exit":
                break
            questions.append(current_question)
            print("Antwort:")

        answers.append(input())
        current_question_index += 1

    print("Fragebogen-ID:")
    fragebogen_id = input()

    if not os.path.exists(DATA_DIRECTORY):
        os.mkdir(DATA_DIRECTORY)

    with open(QUESTIONS_FILE_PATH, "w+") as f:
        for question in questions:
            f.write(question + "\n")

    with open(DATA_DIRECTORY + fragebogen_id + ".txt", "w+") as f:
        for question in questions:
            f.write(question + "\n")
