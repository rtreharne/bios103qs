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
    for i in range(200, 301):

        answer = get_answer(i)


        question_text = f"""
<p>Below is an example of an R script.<p>
<pre style="background-color: #f4f4f4; border: 1px solid #ddd; border-left: 3px solid #f36d33; color: #666; font-family: monospace; font-size: 15px; line-height: 1.6; margin-bottom: 1.6em; max-width: 100%; overflow: auto; padding: 1em 1.5em; display: block;"><code><span style="color: green;"># create a variable called "seed"</span>
seed = 123

<span style="color: green;"># set the seed</span>
set.seed(seed)

<span style="color: green;"># generate a random number</span>
random_number &lt;- runif(1)

<span style="color: green;"># print the random number</span>
print(random_number)</code></pre>            
<p>Create a new R project in RStudio.</p>
<p>Copy and paste the example script into a new R script file.</p>
<p>Replace the value of the variable "seed" with the number <strong>{i}</strong>.</p>
<p>Run the script and enter the output as your answer.</p>
<p>Express your answer to 4 decimal places.</p>
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

    
    df = pd.read_csv("random_numbers.csv")

    # df has two columns: "seed" and "random_number"
    # get the random_number corresponding to the seed that has value unique_id
    random_number = df[df["seed"] == unique_id]["random_number"].values[0]

    # round random number to 4 decimal places
    answer = round(random_number, 4)

    return answer


if __name__ == "__main__":
    canvas = Canvas(CANVAS_URL, CANVAS_TOKEN)
    course = canvas.get_course(COURSE_ID)

    quiz = get_quiz(course)

    # create part 1
    quiz_group = quiz.create_question_group(quiz_groups=[{'name': 'Group 2', 'pick_count': 1, 'question_points': 1}])

    create_group_questions(quiz_group)



    # create part 2
