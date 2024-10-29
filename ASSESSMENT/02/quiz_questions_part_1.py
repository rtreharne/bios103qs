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
    for i in range(201, 301):

        

        group = np.random.choice(["0%", "1.5%", "2%", "2.5%"])
        stat = np.random.choice(["mean", "median", "standard deviation", "variance", "minimum", "maximum"])

        answer = get_answer(i, group, stat)

        question_text = f"""
            <p>You perform an experiment to investigate the effects of Zebrafish embryo development under different ethanol concentrations. You measure the lengths of embryos treated with 0% (control group), 1.5%, 2% and 2.5% concentrations of ethanol solution.</p>
            <br>
            <p>Your resultant data has the following headers:</p>
            <ul>
                <li>'id' column: unique identifier</li>
                <li>'conc_pc' column: ethanol concentration (%)</li>
                <li>'length_micron' column: Embryo Length (microns)</li>
            </ul>
            <br>
            <p>[<a href='https://canvaswizards.org.uk/dataspell/zebrafish/{i}'>Download the data</a>] | <a target="_blank" href='https://raw.githubusercontent.com/rtreharne/qs/main/data/02/zebrafish_{i}.csv'>Backup link to data file</a></p>
            <p>Import the .csv into Excel.</p>
            <p>Generate a summary table that includes the following statistics, by group, for the 'length_micron' column:</p>
            <ul>
                <li>Mean</li>
                <li>Median</li>
                <li>Standard deviation</li>
                <li>Variance</li>
                <li>Minimum</li>
                <li>Maximum</li>
            </ul>
            <p>What is the {stat} of the length values for the {group} ethanol concentration group?</p>
            <p>Express your answer to <strong>1 decimal place</strong>.</p>
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
                        'answer_error_margin': 0.1
                    }, 
                ]
            }
        )

def get_answer(unique_id, group, stat):

    
    np.random.seed(unique_id)
    df = pd.read_csv('data.csv')
    sample = df.sample(n=160)



    group_map = {
        "0%" : 0.0,
        "1.5%" : 1.5,
        "2%" : 2.0,
        "2.5%" : 2.5
    }

    if stat == "mean":
        return round(sample[sample["conc_pc"] == group_map[group]]["length_micron"].mean(), 1)
    elif stat == "median":
        return round(sample[sample["conc_pc"] == group_map[group]]["length_micron"].median(), 1)
    elif stat == "standard deviation":
        return round(sample[sample["conc_pc"] == group_map[group]]["length_micron"].std(), 1)
    elif stat == "variance":
        return round(sample[sample["conc_pc"] == group_map[group]]["length_micron"].var(), 1)
    elif stat == "minimum":
        return round(sample[sample["conc_pc"] == group_map[group]]["length_micron"].min(), 1)
    elif stat == "maximum":
        return round(sample[sample["conc_pc"] == group_map[group]]["length_micron"].max(), 1)



if __name__ == "__main__":
    canvas = Canvas(CANVAS_URL, CANVAS_TOKEN)
    course = canvas.get_course(COURSE_ID)

    quiz = get_quiz(course)

    # create part 1
    quiz_group = quiz.create_question_group(quiz_groups=[{'name': 'Group 1', 'pick_count': 1, 'question_points': 1}])

    create_group_questions(quiz_group)



