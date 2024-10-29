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

        question_text = f"""
            <p>This question uses another subset of the PANTHERIA dataset - a global species-level dataset of ecological traits of all known extant and recently extinct mammals compiled from the literature.</p>
            <p>Create a new R project.</p>
            <p>Create a new R script file.</p>
            <p>[<a href='https://canvaswizards.org.uk/dataspell/pantheria/{i}'>Download the data</a>] | <a target="_blank" href='https://raw.githubusercontent.com/rtreharne/qs/main/data/04/pantheria_{i}.csv'>Backup link to data file</a></p>
            <p style="color: red;">Warning! This not the same data as in the previous question.</p>
            <p>Move the downloaded file to your project directory.</p>
            <p>Read the file to a variable called "data" using <code style='background-color: #f5f5f5; border: 1px solid #ccc; padding: 2px 4px; border-radius: 4px;'>data &lt;- read.csv('pantheria_{i}.csv')</code>.</p>
            <p>Filter out any rows with -999 values in the <strong>AdultBodyMass_g</strong> column.</p>
            <p>Generate a summary table to show the mean, median, minimum, maximum, standard deviation and count of the <strong>AdultBodyMass_g</strong> column by Order. </p>
            <p>What is the median Adult Body Mass of the order that has been recorded the most frequently in the dataset?</p>
            <p>Express your answer <strong>in g</strong> to <strong>1 decimal place</strong>.</p>
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

def get_answer(unique_id):

    
    np.random.seed(unique_id)
    df = pd.read_csv('pantheria_limited.csv')
    sample = df.sample(n=2000)

    # Filter out rows with BasalMetRate_mLO2hr value of -999
    data_filtered = sample[sample['AdultBodyMass_g'] != -999]

    # Find the most common Order
    most_common_order = data_filtered['Order'].value_counts().idxmax()

    # Find the median AdultBodyMass_g of the most common Order
    median_mass = data_filtered[data_filtered['Order'] == most_common_order]['AdultBodyMass_g'].median()

    return round(median_mass, 1)

    

if __name__ == "__main__":
    canvas = Canvas(CANVAS_URL, CANVAS_TOKEN)
    course = canvas.get_course(COURSE_ID)

    quiz = get_quiz(course)

    # create part 1
    quiz_group = quiz.create_question_group(quiz_groups=[{'name': 'Group 1', 'pick_count': 1, 'question_points': 1}])

    create_group_questions(quiz_group)



