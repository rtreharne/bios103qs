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
    for i in range(100, 200):

        answer = get_answer(i)

        question_text = f"""
            <p>[<a href='https://www.canvaswizards.org.uk/dataspell/calibration/{i}'>Download this .csv file</a>]<p>
            <p>Import the .csv into Excel.</p>
            <p>Transpose the data so that the 'concentration' values are in the first column and the 'absorbance' values are in the second column.</p>
            <p>Header information:</p>

            <p>Generate a scatterplot and add a linear trendline and the equation of the line.</p>
            <p>For an absorbance value of 0.5, estimate the protein concentration?</p>
            <p>Express your answer to <strong>2 decimal places</strong> and in units of mg/mL.</p>
        """
        question = quiz.create_question(question=
            {
                'question_name': f'Question #{i}',
                'question_text': question_text,
                'points_possible': 1, 
                'question_type': 'numerical_question',
                'quiz_group_id': quiz_group.id,
                'correct_comments': 'Correct, well done!',
                'incorrect_comments': 'Incorrect, try again! Did you remember to set your intercept to zero?',
                'answers': [
                    {
                        'text': f'Answer #{i}', 
                        'weight': 100, 
                        'numerical_answer_type': 'exact_answer',
                        'answer_exact': answer,
                        'answer_error_margin': 0.01
                    }, 
                ]
            }
        )

def get_answer(unique_id):

    
    np.random.seed(unique_id)
    df = pd.read_csv('data.csv')
    sample = df.sample(n=1)

    # transpose the data
    sample = sample.T

    sample.reset_index(inplace=True)

    # make row 1 column headers
    sample.columns = sample.iloc[0]

    # drop row 1
    sample = sample.drop(0)

    # create a linear regression model. Set intercept to zero
    model = LinearRegression(fit_intercept=False)

    # fit the model
    model.fit(sample[['Absorbance (Arb. units)']], sample['Protein conc. (mg/mL)'])

    # estimate the protein concentration for an absorbance of 0.5
    answer = model.predict([[0.5]])[0]

    return round(answer, 2)

    

if __name__ == "__main__":
    canvas = Canvas(CANVAS_URL, CANVAS_TOKEN)
    course = canvas.get_course(COURSE_ID)

    quiz = get_quiz(course)

    # create part 1
    quiz_group = quiz.create_question_group(quiz_groups=[{'name': 'Group 1', 'pick_count': 1, 'question_points': 1}])

    create_group_questions(quiz_group)



