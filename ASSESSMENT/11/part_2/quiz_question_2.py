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
    for i in range(100,200):

    

        answer = get_answer(i)

        question_text = f"""
<h2>The Doomscroller Virus Pandemic: Part Two</h2>

    <p>
        New evidence has come to light that the viable red blood cell count is less
        important than the proportion of non-viable cells. In fact, any sample
        in which there are more than 20% non-viable cells can be interpreted as a positive test for the virus.
    </p>

    <p>
        Problem. Your hemo-tools.R script only counts viable cells. You need to quickly update the script to 
        count non-viable cells and then use it to calculate the percentage of non-viable cells in a sample.
    </p>

    <p>
        You are given ANOTHER
        <strong>
            <a href='https://raw.githubusercontent.com/rtreharne/qs/main/data/11/hemo_{i}.zip'>
                zip file
            </a>
         containing 100 hemocytometer images</strong>, each representing a slide prepared from suspected infected blood 
        samples. Your task is to count the number of positive results identified by a non-viable cell proportion that is greater than 20%. 
    </p>

    <h3>Instructions:</h3>
    <ol>
        <li>Download the <a href='https://raw.githubusercontent.com/rtreharne/qs/main/data/11/hemo_{i}.zip'>
            zip file
        </a> containing hemocytometer images and copy it to your project directory.</li>
        <li>Update the <a target='_blank' href='https://raw.githubusercontent.com/rtreharne/qs/main/script/11/hemo-tools.R'>hemo-tools.R</a> script using your R knowledge to extract the viable AND non-viable cell counts for each image in the zip file. Non-viable cells appear blue.</li>
        <li>Calculate the percentage of non-viable cells in each of the images.</li>
        <li>Report how many samples have a percentage of non-viable cells greater than 20% in the box below.</li>
    </ol>"""
        
        question = quiz.create_question(question=
            {
                'question_name': f'Question #{i}',
                'question_text': question_text,
                'points_possible': 2, 
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
                        'answer_error_margin': 0
                    }, 
                ]
            }
        )

def get_answer(unique_id):

    with open("nv_results.csv", "r") as f:
        lines = f.readlines()
        for line in lines:
            if f"hemo_{unique_id}.zip" in line:
                return round(float(line.split(",")[1]),1)
   

if __name__ == "__main__":
    canvas = Canvas(CANVAS_URL, CANVAS_TOKEN)
    course = canvas.get_course(COURSE_ID)

    quiz = get_quiz(course)

    # create part 1
    quiz_group = quiz.create_question_group(quiz_groups=[{'name': 'Question 2', 'pick_count': 1, 'question_points': 2}])

    create_group_questions(quiz_group)



