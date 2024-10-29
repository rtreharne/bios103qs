from canvasapi import Canvas
from config import CANVAS_TOKEN, CANVAS_URL, COURSE_ID
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def get_quiz(course):
    quizzes = [x for x in course.get_quizzes()]
    for i, quiz in enumerate(quizzes):
        print(f"{i}: {quiz.title}")

    quiz = input("Enter the number of the quiz you want to use: ")

    try:
        quiz = quizzes[int(quiz)]
        return quiz
    except:
        print("Invalid quiz number")

def create_group_questions(quiz_group):
    for i in range(200, 301):

        answer = get_answer(i)



        question_text = f"""
            <p>You are required to investigate the relationship between the mass and estimated volumes for a sample of snails.<p>
            <p>[<a href='https://canvaswizards.org.uk/dataspell/snails/{i}'>Download this .csv file</a>] | <a target="_blank" href='https://raw.githubusercontent.com/rtreharne/qs/main/data/01/snails_{i}.csv'>Backup link to data file</a><p>
            <p>Import the .csv into Excel.</p>
            <p>Calculate a third column called 'Volume V (mm<sup>3</sup>)' using the formula:</p>
            <p>V = (4/3) &pi; r<sup>3</sup></p>
            <p>where r is the half the 'Height L (mm)' column.</p>
            <p>Add a linear trendline, including the equation on the chart.</p>
            <p>Using the equation of the trendline, calculate an estimate for the volume of a snail with a mass of 10g.</p>
            <p>Express your answer in <strong>cm<sup>3</sup></strong> to <strong>1 decimal place</strong>.</p>
        """
        question = quiz.create_question(question=
            {
                'question_name': f'Question #{i}',
                'question_text': question_text,
                'points_possible': 1, 
                'question_type': 'numerical_question',
                'quiz_group_id': quiz_group.id,
                'correct_comments': 'Correct, well done!',
                'incorrect_comments': 'Incorrect, try again!',
                'answers': [
                    {
                        'text': f'Answer #{i}', 
                        'weight': 100, 
                        'numerical_answer_type': 'exact_answer',
                        'answer_exact': answer,
                        'answer_error_margin': 0.1
                    }, 
                ]
            }
        )

def get_answer(unique_id):

    
    np.random.seed(unique_id)
    df = pd.read_csv('week_1_snail_data.csv')
    sample = df.sample(n=160)

    sample['Volume V (mm^3)'] = (4/3) * np.pi * (0.5 * sample['Height L (mm)']) ** 3

    x = sample[['Snail mass M (g)']]
    y = sample[['Volume V (mm^3)']]

    model = LinearRegression().fit(x, y)

    m, c = model.coef_[0][0], model.intercept_[0]
    print("coeffs", m, c, "unique_id", unique_id)

    answer = m * 10 + c

    answer = answer / 1000

    # round to 1 decimal place
    answer = round(answer, 1)

    return answer


if __name__ == "__main__":
    canvas = Canvas(CANVAS_URL, CANVAS_TOKEN)
    course = canvas.get_course(COURSE_ID)

    quiz = get_quiz(course)

    # create part 1
    quiz_group = quiz.create_question_group(quiz_groups=[{'name': 'Group 1', 'pick_count': 1, 'question_points': 1}])

    create_group_questions(quiz_group)



    # create part 2
