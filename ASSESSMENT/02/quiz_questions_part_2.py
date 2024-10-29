from canvasapi import Canvas
from config import CANVAS_TOKEN, CANVAS_URL, COURSE_ID
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

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

        

        group = np.random.choice(["0%", "1.5%", "2%", "2.5%"])
        stat = np.random.choice(["mean", "median", "standard deviation", "variance", "minimum", "maximum"])

        answer = get_answer(i, group, stat)

        question_text = f"""
            <p>You repeat your Zebrafish experiment and generate a new set of data. To answer this question DO NOT use the data from the previous question.</p>
            <br>
            <p>[<a href='https://canvaswizards.org.uk/dataspell/zebrafish/{i}'>Download this .csv file</a>] | <a target="_blank" href='https://raw.githubusercontent.com/rtreharne/qs/main/data/02/zebrafish_{i}.csv'>Backup link to data file</a></p>
            <p style="color: red;">Warning! This not the same data as in the previous question.</p>
            <p>Import the .csv into Excel.</p>
            <p>Header information:</p>
            <ul>
                <li>'id' column: unique identifier</li>
                <li>'conc_pc' column: ethanol concentration (%)</li>
                <li>'length_micron' column: Embryo Length (microns)</li>
            </ul>
            <p>Create a pivot table that converts the data to "wide" format.</p>
            <p>Perform a one-way ANOVA test to determine if there is a significant difference in the length values between the ethanol concentration groups.</p>
            <p>What is the F statistic of the ANOVA test?</p>
            <p>Express your answer to <strong>2 decimal places</strong>.</p>
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

def get_answer(unique_id, group, stat):

    
    np.random.seed(unique_id)
    df = pd.read_csv('data.csv')
    sample = df.sample(n=160)

    model = ols('length_micron ~ C(conc_pc)', data=sample).fit()
    anova_results = anova_lm(model)
    return round(anova_results['F'][0], 2)

    



if __name__ == "__main__":
    canvas = Canvas(CANVAS_URL, CANVAS_TOKEN)
    course = canvas.get_course(COURSE_ID)

    quiz = get_quiz(course)

    # create part 1
    quiz_group = quiz.create_question_group(quiz_groups=[{'name': 'Group 1', 'pick_count': 1, 'question_points': 1}])

    create_group_questions(quiz_group)



