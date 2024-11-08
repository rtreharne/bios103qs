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
<h2>The Doomscroller Virus Pandemic: Part 1.</h2>

    <p>
        A new virus, dubbed the <em>Doomscroller</em> virus, 
        is affecting young people worldwide, resulting in a drastic 
        drop in productivity. One of the key symptoms of this virus 
        is a reduction in viable red blood cell counts. Labs across 
        the country are overwhelmed and short on costly autocounting 
        equipment. Fortunately, they still have large supplies of 
        hemocytometers and digital microscopes for manual cell counting.
    </p>

    <p>
        You've recently been hired as an expert bio-analyst to help 
        solve this bottleneck. Your team has developed a short script 
        that can analyse digital images of hemocytometer slides and 
        automatically count viable red blood cells.
    </p>

    <p>
        To prove the viability of this solution, you are given a 
        <strong>
            <a href='https://raw.githubusercontent.com/rtreharne/qs/main/data/11/hemo_{i}.zip'>
                zip file
            </a>
         containing 100 hemocytometer images
        </strong>, each representing a slide prepared from suspected infected blood 
        samples. Your task is to run the script on each image and calculate 
        the <strong>average number of viable cells</strong> across all 100 
        images.
    </p>

    <h3>Instructions:</h3>
    <ol>
        <li>Start a new R project</li>
        <li>Start a new script file.</li>
        <li>Download the <a href='https://raw.githubusercontent.com/rtreharne/qs/main/data/11/hemo_{i}.zip'>
            zip file
        </a> containing hemocytometer images and copy it to your project directory.</li>
        <li>Use the <a target='_blank' href='https://raw.githubusercontent.com/rtreharne/qs/main/script/11/hemo-tools.R'>hemo-tools.R</a> script and your R knowledge to extract the viable cell count for each image in the zip file.</li>
        <li>Calculate the average viable cell count across all images.</li>
        <li>Report the result, <strong>to 1 d.p.</strong>, in the box below.</li>
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
                        'answer_error_margin': 0.1
                    }, 
                ]
            }
        )

def get_answer(unique_id):

    with open("results.csv", "r") as f:
        lines = f.readlines()
        for line in lines:
            if f"hemo_{unique_id}.zip" in line:
                return round(float(line.split(",")[1]),1)
   

if __name__ == "__main__":
    canvas = Canvas(CANVAS_URL, CANVAS_TOKEN)
    course = canvas.get_course(COURSE_ID)

    quiz = get_quiz(course)

    # create part 1
    quiz_group = quiz.create_question_group(quiz_groups=[{'name': 'Group 1', 'pick_count': 1, 'question_points': 1}])

    create_group_questions(quiz_group)



