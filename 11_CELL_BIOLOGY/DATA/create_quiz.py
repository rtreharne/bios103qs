# This script will create a Classic Quiz in Canvas that contains a single question drawn from a bank of 100 questions.
# Each question one of the unique .zip files containing 100 hemocytometer images.


import requests
from canvasapi import Canvas
import pandas as pd
import random

# Create a quiz
def create_quiz(canvas, course_id, quiz_name):
    course = canvas.get_course(course_id)
    quiz = course.create_quiz(quiz={
        'title': quiz_name,
        'points': 100,
        'shuffle_answers': True,
        'quiz_type': 'assignment',
        'allowed_attempts': 1,
        'scoring_policy': 'keep_highest',
        'hide_results': 'always',
        'show_correct_answers': True,
        'show_correct_answers_last_attempt': True,
        'show_correct_answers_at': 'available',
        'hide_correct_answers_at': 'never',
        'allowed_attempts': -1,
        'one_question_at_a_time': True,
        'cant_go_back': True,
    })
    return quiz
        

# Create a question group
def create_question_group(course_id, quiz_id):
    course = canvas.get_course(course_id)
    quiz = course.get_quiz(quiz_id)

    question_group = quiz.create_question_group(quiz_groups=[{
        'name': 'Cell Counting',
        'pick_count': 1,
        'question_points': 1
    }])
    return question_group

def create_question(quiz, 
                    question_group_id,
                    question_name,
                    question_text,
                    answers):

    question = quiz.create_question(question={
        'question_name': question_name,
        'question_text': question_text,
        'points_possible': 1,
        'question_type': 'multiple_choice_question',
        'quiz_group_id': question_group_id,
        'answers': answers
    })
    return question

def prepare_answers(fname):
    df = pd.read_csv(fname)
    df["answer"] = df["means"] * df["stds"]
    df["answer"] = df["answer"].astype(int)
    
    print(df["zip_paths"].tolist())

    url = "https://github.com/rtreharne/bios103qs/blob/main/"

    url_list = []
    for file in df["zip_paths"].tolist():
        path = file.split("BIOS103QS/")[1]
        url_list.append(url + path)
    
    df["url"] = url_list

    return df

if __name__ == '__main__':

    # Ask for URL and token
    CANVAS_URL = input("Enter your Canvas URL: ")
    CANVAS_TOKEN = input("Enter your Canvas API Toekn: ")

    # Initialize a new Canvas object
    canvas = Canvas(CANVAS_URL, CANVAS_TOKEN)

    # Get the course ID
    course_id = input("Enter your course ID: ")

    # Get the Course object
    course = canvas.get_course(course_id)

    # Create a quiz
    quiz = create_quiz(canvas, course_id, "Cell Biology Quiz")

    # Create a question group
    question_group = create_question_group(course_id, quiz.id)

    df = prepare_answers("results.csv")

    for i, row in df.iterrows():
        question_name = "Question"
        question_text = f"""
            Download this <a href='{row['url']}'>data</a><br><br>
            The .zip file contains 100 hemocytometer images.<br><br>
            Use your 'count_zip.R' script to calculate the mean number of viable cells and standard deviation of the data.<br><br>
            What is the product of the mean and standard deviation?<br><br>
            Select the correct answer from the list below.
            """
        answers = {}
        answers['0'] = {
            'text': row["answer"],
            'weight': 100
        }
        all_answers = df["answer"].tolist()
        incorrect_answers = [x for x in all_answers if x != row["answer"]]
        incorrect_answers = random.sample(incorrect_answers, 4)
        for j, answer in enumerate(incorrect_answers):
            answers[str(j+1)] = {
                'text': answer,
                'weight': 0
            }

        print("Creating question...", i)
        question = create_question(
            quiz, 
            question_group.id,
            question_name,
            question_text,
            answers
        )
        


    

    



