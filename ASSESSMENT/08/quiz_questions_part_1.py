from canvasapi import Canvas
from config import CANVAS_TOKEN, CANVAS_URL, COURSE_ID
import pandas as pd
import numpy as np
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd


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
    for i in range(100, 101):

        answer = get_answer(i)

       
        question_text = f"""
            <p>Create a new R project.</p>
            <p>Create a new R script file.</p>
            <p>[<a href='https://canvaswizards.org.uk/dataspell/activity/{i}'>Download the data</a>] | <a target="_blank" href='https://raw.githubusercontent.com/rtreharne/qs/main/data/08/activity_{i}.csv'>Backup link to data file</a></p>
            <p>Move the downloaded file to your project directory.</p>
            <p>Read the file to a variable called "data" using <code style='background-color: #f5f5f5; border: 1px solid #ccc; padding: 2px 4px; border-radius: 4px;'>data &lt;- read.csv('pantheria_{i}.csv')</code>.</p>
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
                        'answer_error_margin': 0.0001
                    }, 
                ]
                
            }
        )

def get_answer(unique_id):

    
    np.random.seed(unique_id)
    df = pd.read_csv('activity.csv')
    sample = df.sample(n=200)

    activity_data = sample

    # Convert 'activity' column to numeric
    activity_data['activity'] = pd.to_numeric(activity_data['activity'], errors='coerce')

    # Replace negative values in 'activity' with NaN
    activity_data.loc[activity_data['activity'] < 0, 'activity'] = np.nan

    # Remove rows with NaN values
    activity_data.dropna(inplace=True)

    # Convert 'ph' and 'temperature' columns to categorical (similar to factor in R)
    activity_data['ph'] = activity_data['ph'].astype('category')
    activity_data['temperature'] = activity_data['temperature'].astype('category')

    print("Tukey Results:")


    tukey_result = pairwise_tukeyhsd(endog=activity_data['activity'], groups=activity_data['ph'])

    print(tukey_result)


    return round(tukey_result.pvalues[1], 4)

    

if __name__ == "__main__":
    canvas = Canvas(CANVAS_URL, CANVAS_TOKEN)
    course = canvas.get_course(COURSE_ID)

    quiz = get_quiz(course)

    # create part 1
    quiz_group = quiz.create_question_group(quiz_groups=[{'name': 'Group 1', 'pick_count': 1, 'question_points': 1}])

    create_group_questions(quiz_group)



