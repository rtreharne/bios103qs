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
    for i in range(200, 300):

        answer = get_answer(i)

        if answer is not None:

            answers = [{
                'text': a,
                'weight': 100,
            } for a in answer]



            question_text = f"""
                <p>This question uses a subset of the PANTHERIA dataset - a global species-level dataset of ecological traits of all known extant and recently extinct mammals compiled from the literature.</p>
                <p>Create a new R project.</p>
                <p>Create a new R script file.</p>
                <p>[<a href='https://canvaswizards.org.uk/dataspell/pantheria/{i}'>Download the data</a>] | <a target="_blank" href='https://raw.githubusercontent.com/rtreharne/qs/main/data/04/pantheria_{i}.csv'>Backup link to data file</a></p>
                <p>Move the downloaded file to your project directory.</p>
                <p>Read the file to a variable called "data" using <code style='background-color: #f5f5f5; border: 1px solid #ccc; padding: 2px 4px; border-radius: 4px;'>data &lt;- read.csv('pantheria_{i}.csv')</code>.</p>
                <p>What Family has the most rows in the dataset?</p>
                <p>Enter your answer below in the format FAMILY99 where 99 is the number of rows.</p>
                <p>Make sure that the family name is in uppercase and that there are no spaces between the family name and the number.</p>
            """

            question = quiz.create_question(question=
                {
                    'question_name': f'Question #{i}',
                    'question_text': question_text,
                    'points_possible': 1, 
                    'question_type': 'short_answer_question',
                    'quiz_group_id': quiz_group.id,
                    'correct_comments': 'Correct, well done!',
                    'incorrect_comments': 'Incorrect.',
                    'answers': answers
                    
                }
            )

def check_max_unique(series):
    
    mx = series.max()

    # how many times does mx occur in series?
    count = series[series == mx].count()

    if count > 1:
        return False
    else:
        return True

def get_answer(unique_id):

    
    np.random.seed(unique_id)
    df = pd.read_csv('pantheria_limited.csv')
    sample = df.sample(n=2000)

    family_counts = sample.groupby('Family').size().sort_values(ascending=False)
    family_counts.head(10)

    if check_max_unique(family_counts):
        for family, count in family_counts.items():
            string_list = [
                f'{family}{count}'.upper(),
                f'{family}{count}'.lower(),
                f'{family}{count}'.capitalize(),

            ]   
            break

        return string_list

    

if __name__ == "__main__":
    canvas = Canvas(CANVAS_URL, CANVAS_TOKEN)
    course = canvas.get_course(COURSE_ID)

    quiz = get_quiz(course)

    # create part 1
    quiz_group = quiz.create_question_group(quiz_groups=[{'name': 'Group 1', 'pick_count': 1, 'question_points': 1}])

    create_group_questions(quiz_group)



