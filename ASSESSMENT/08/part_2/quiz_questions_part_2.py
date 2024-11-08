from canvasapi import Canvas
from config import CANVAS_TOKEN, CANVAS_URL, COURSE_ID
import pandas as pd
import numpy as np
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import statsmodels.api as sm

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
    for i in range(200, 300):

        answer = get_answer(i)

       
        question_text = f"""
            <p>
                You are overseeing a series of experiments to determine
                the effect of <strong>pH</strong> and <strong>Temperature</strong> on the activity of an enzyme.
                You consolidate the results from 10 independent groups for analysis.
            <ol>  
                <li>Create a new R project.</li>
                <li>Create a new R script file.</li>
                <li>Read the data directly to a variable (without downloading!) using the following url:</li>
                <li><a href="https://raw.githubusercontent.com/rtreharne/qs/main/data/08/activity_{i}.csv" target="_blank">https://raw.githubusercontent.com/rtreharne/qs/main/data/08/activity_{i}.csv</a></li>
                <li><strong>Clean the data.</strong></li>
                <li>Create a two-way ANOVA model.</li>
                <li>Perform a TukeyHSD on the model.</li>

                <li>What is the largest <b>absolute</b> difference in the means of the pairwise comparisons of pH:Temperature groups?</li>
                <li>Express your answer below as a percentage to <strong>4 d.p.</strong></li>
            </ol>
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
    sample = df.sample(n=300)

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


    # Perform ANOVA
    model = ols('activity ~ ph * temperature', data=activity_data).fit()
    anova_result = sm.stats.anova_lm(model, typ=2)

    # Perform Tukey's HSD test
    tukey_result = pairwise_tukeyhsd(activity_data['activity'], activity_data['ph'].astype(str) + ":" + activity_data['temperature'].astype(str))

    tukey_df = pd.DataFrame(data=tukey_result.summary().data[1:], columns=tukey_result.summary().data[0])

    tukey_df['meandiff'] = tukey_df['meandiff'].abs()

    result = round(tukey_df['meandiff'].max(), 4)

    return result

    

if __name__ == "__main__":
    canvas = Canvas(CANVAS_URL, CANVAS_TOKEN)
    course = canvas.get_course(COURSE_ID)

    quiz = get_quiz(course)

    # create part 1
    quiz_group = quiz.create_question_group(quiz_groups=[{'name': 'Group 1', 'pick_count': 1, 'question_points': 1}])

    create_group_questions(quiz_group)



