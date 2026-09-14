def ask_question(question_text):
    print(question_text)
    answer = input('Write your answer here:')

    return answer

def check_answer(answer, correct_answer):
    if answer == correct_answer:
        return True
    else:
        return False

def show_feedback(is_correct):
    if is_correct == True:
        print('Correct answer!')
    else:
        print('Wrong answer!')

def run_quiz():
    score = 0
    answer = ask_question("What is the name of the king of Norway?")
    is_correct = check_answer(answer, "Haakon")
    show_feedback(is_correct)
    if is_correct == True:
        score += 1
    answer = ask_question("What is the capital of Norway?")
    is_correct = check_answer(answer, "Oslo")
    show_feedback(is_correct)
    if is_correct == True:
        score += 1
    answer = ask_question("What is the name of our teacher?")
    is_correct = check_answer(answer, "Tomas")
    show_feedback(is_correct)
    if is_correct == True:
        score += 1
    print(f'You got {score} points!')


run_quiz()


