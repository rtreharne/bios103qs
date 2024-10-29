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
    for i in range(200,300):

        question_text = f"""
            <h1>MegaMush Data Analysis Report</h1>
            <h3>Background</h3>
            <p>
                <strong><em>MegaMush<sup>TM</sup></em></strong>, a mushroom compost company based in the Netherlands, is trying to identify an issue with its pre-pasteurisation composting process across its five operational production sites.
            </p>
            
            <h3>Task Overview</h3>
            <p>
                You have been hired as an independent bioscience data consultant and have been tasked with summarising and visualising a dataset compiled over a period of 1 year and consolidated from each location.
            </p>
            
            <h3>Data Acquisition</h3>

            <p>Download your unique dataset from [<a href='https://canvaswizards.org.uk/dataspell/compost/{i}'>here.</a>] | <a target="_blank" href='https://raw.githubusercontent.com/rtreharne/qs/main/data/05/compost_{i}.csv'>Backup link to data file</a><p>
   
            
            <h32>Specific Tasks</h3>
            <p>
                Specifically, you have been asked to generate the following for incorporation into a report that will be presented by the chief technical officer of the company to the extended board of directors:
            </p>
            <ul>
                <li>A summary table that shows the mean and standard deviations of the composting temperature, moisture, and viable colony counts at each site.</li>
                <li>A histogram showing the distribution of estimated viable bacterial counts, VBC (cfu.g<sup>-1</sup>) from across all samples.</li>
                <li>A grouped boxplot showing the distributions of estimated VBC for each site.</li>
                <li>A scatterplot that shows the relationship between temperature and estimated VBC.</li>
                <li>A final plot (histogram, boxplot or scatterplot) of any other feature you find interesting in the data.</li>
            </ul>
            
            <h3>Dataset Generation Information</h3>
            <p>
                You have also been provided with the following information on how the dataset was generated:
            </p>
            <p>
                The compost temperature and moisture content were measured directly during the sampling process using calibrated thermometers and moisture probes.
            </p>
            <p>
                After collection, samples were immediately placed into sterile containers to prevent cross-contamination and transported to the central laboratory under refrigerated conditions at 4°C. To ensure the integrity of microbial counts, all samples were processed within 24 hours of collection.
            </p>
            <p>
                In the laboratory, 0.5g each compost sample was dissolved in 10mL of sterile reagent and mixed thoroughly to create the starting solution for subsequent serial dilution. In each case, a 1/1000 serial dilution was performed and 0.1mL of the diluted sample was plated onto selective agar media. Plates were incubated for 48 hrs at 30°C before the number of viable colonies were counted.
            </p>
            <p>
                This procedure was performed regularly for each site, ensuring consistent data collection on microbial counts, temperature, and moisture content across all locations over the course of a year.
            </p>
            
            <h3>Submission Instructions</h3>
            <p>
                Submit your work as a single .docx file according to <a href="https://canvas.liverpool.ac.uk/files/11483464/download?download_frd=1" target="_blank">this template</a>.
            </p>
        """
        question = quiz.create_question(question=
            {
                'question_name': f'Question #{i}',
                'question_text': question_text,
                'points_possible': 1, 
                'question_type': 'file_upload_question',
                'quiz_group_id': quiz_group.id,
                
            }
        )



if __name__ == "__main__":
    canvas = Canvas(CANVAS_URL, CANVAS_TOKEN)
    course = canvas.get_course(COURSE_ID)

    quiz = get_quiz(course)

    # create part 1
    quiz_group = quiz.create_question_group(quiz_groups=[{'name': 'Question 9. Compost.', 'pick_count': 1, 'question_points': 4}])

    create_group_questions(quiz_group)



