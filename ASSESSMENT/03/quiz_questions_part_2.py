from canvasapi import Canvas
from config import CANVAS_TOKEN, CANVAS_URL, COURSE_ID
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from scipy import stats

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
    for i in range(200,300):

        answer = float(get_answer(i))

        print("ANSWER: ", answer)

        question_text = f"""
            <p>You have measured the daily growth of a sunflower and also recorded the number ofhours of direct sunlight that the sunflower receives.</p>
            <p>Header information:</p>
            <ul>
                <li>Column 1: Number of hours of direct sunlight that sunflower receive in 24 hrs.</li>
                <li>Column 2: Measured growth (in mm) over 24 hrs.</li>
            </ul>
            <p>[<a href='https://canvaswizards.org.uk/dataspell/sunflowers/{i}'>Download the data</a>] | <a target="_blank" href='https://raw.githubusercontent.com/rtreharne/qs/main/data/03/part_2/sunflowers_{i}.csv'>Backup link to data file</a><p>
            <p>Import the data into Excel.</p>
            <p>Perform a linear regression analysis to determine the relationship between the number of hours of direct sunlight and the growth of the sunflowers.</p>
            <p>Calculate the margin of error (ME) for your regression. Remember: ME = t * SE, where:</p>
            <ul>
              <li>t is a value drawn from the student's t-test distribution.</li>
              <li>SE is the standard error as calculated by the regression.</li>
            <p>Express your answer in units of mm/day and to <strong>1 decimal places</strong>.</p>
        """
        
        question = quiz.create_question(question=
            {
                'question_name': f'Question #{i}',
                'question_text': question_text,
                'points_possible': 1, 
                'question_type': 'numerical_question',
                'quiz_group_id': quiz_group.id,
                'correct_comments': 'Correct, well done!',
                'incorrect_comments': 'Incorrect.',
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
    df = pd.read_csv('sunflowers.csv')
    sample = df.sample(n=24)

    # create a linear regression model. Set intercept to zero
    model = LinearRegression()

    # fit the model
    y = sample[['mm_growth_per_day']]
    X = sample[['hours_direct_sunlight_per_day']]

    # Fit the model
    model = LinearRegression().fit(X, y)

    # Predict the values
    predictions = model.predict(X)

    # Calculate residuals
    residuals = y - predictions

    # Compute the sum of squared residuals
    SSR = np.sum(residuals**2)

    # Calculate the degrees of freedom (n - p - 1)
    # n is the number of observations, p is the number of predictors
    degrees_of_freedom = len(y) - X.shape[1] - 1

    # Calculate the standard error of the regression
    SER = np.sqrt(SSR / degrees_of_freedom)

    ME = stats.t.ppf(1-0.05/2,degrees_of_freedom)*SER

    return round(ME, 1)

if __name__ == "__main__":
    canvas = Canvas(CANVAS_URL, CANVAS_TOKEN)
    course = canvas.get_course(COURSE_ID)

    quiz = get_quiz(course)

    # create part 1
    quiz_group = quiz.create_question_group(quiz_groups=[{'name': 'Group 1', 'pick_count': 1, 'question_points': 1}])

    create_group_questions(quiz_group)



