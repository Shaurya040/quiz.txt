# quiz.txt
Question and Answer Data: The quiz questions and their corresponding answers are stored in dictionaries for each round of the quiz (Round1_data, Round2_data, etc.).
Global Variables: Variables like current_round, current_question, user_score, highest_score, and round_cleared are initialized to keep track of the quiz progress and scores.
GUI Setup: The Tkinter window is created with a title "GFG QUIZ APP". The layout includes labels for the quiz app title and spacing, a start button (start_button), a frame (f1) for displaying questions, and a next button (next_button) to move to the next question.
Quiz Logic:
The start_quiz() function is called when the start button is clicked. It initializes the quiz by hiding the start button, displaying the next button, and resetting the quiz variables.
The next_question() function progresses through the quiz rounds and questions. It checks if there are more questions in the current round and displays them. When a round is completed, it calculates and displays the score, updates the highest score, and moves to the next round.
The check_ans() function checks if the selected answer matches the correct answer and updates the user's score accordingly.
The clear_frame() function clears the contents of the question frame (f1) for displaying the next question.
Main Execution: The script runs the Tkinter event loop to start the GUI application.
