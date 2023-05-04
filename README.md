# Sciqzz
A Science Quiz(Prototype)

    #### Author: Siri Shivakumar
    #### Video Demo:  <URL HERE>
    #### Description:
    Sciqzz is a Science Quiz that has simple and easy UI for any age group to play.
    It had 3 difficulty levels easy, medium and hard, from which it picks the questions.
    When the quiz starts, the user is asked to enter their name only in alphabets (no number or special character accepted).
    The first level is "Easy". Once all questions in the easy list is exhausted, and the user hasn't yet failed 3 questions in a row the quiz proceeds with next level until all questions in all 3 levels are exhausted.
    User is asked to enter option for the answer and is validated and asked to enter valid input until entered.
    The game ends when the user gives 3 wrong answers in a row or when all the quiz questions are exhausted. 
    The final score is displayed for the player.

## Levels
    ### Easy level questions hold 5 or less points.
    ### Medium level question holds 6 to 10 points.
    ### Hard level questions holds more than 10 points.

## How to End the game before all questions are done?
    ### Press <Ctrl-D> to exit the game abruptly.
    ### 3 wrong answers in a row.

## Implementation Details.

    -> The questions for the quiz are stored in a CSV file for ease of manageability and extensibility. 
    
    -> To add new questions to the quiz, they need to be simply added to the CSV meeting all the field requirements.
    
    -> CSV dict reader is used to load the questions onto the dictionary with keys "Easy", "Medium" and "Hard". Each entry in the dict has a list of questions as key-value pairs.
    
    -> Each list in the dict is shuffled to randomize the order of questions asked to the user every time.
    
    -> Player is appropriately informed to enter only the options "A", "B", "C" or "D" as their choice if entered otherwise and prompted back. The choice is case in-sensitive.
    
    -> Player is also informed the result of their answer for each question with a score tally before moving on to next question.
    
    -> Player has 2 non-penalised try's to enter wrong answer, but the third subsequent wrong answer terminates the game. Displays Game Ends message with final score so far.
    
    -> If the player gives 2 wrong answer and third turns out to be correct, then the fails is reset to 0 again, allowing 2 more wrong choices in future safely that costs only points and not the game itself.
    
    -> pyfiglet is used to display the Game Ends and Score of the player.
    
    -> random is used to shuffle the questions list.
    
    -> 4 tests have been written in pytest to unit test shuffling, levels, mock user choice and read CSV

### Space Complexity: 
    dictionary provides efficient storing and accessing of key-value pairs essential in this scenario to store the questions list in 3 levels.
    O(n) where n is the number of CSV entries aka questions or rows in the CSV file.
    score, name and all other variables consume constant space.

### Time Complexity: 
    excluding user inputs, O(n+n) = O(2n), to read rows from CSV and make an entry in the dictionary and to iterate the same dictionary to ask questions to the player.
    Player's answers are compared with the answer key that is in the dictionary already so no computations required except for integer addition to add on the score.
    2 for loops, one for valid name entry, other for valid option for the answer entry gets triggered only when the user is not entering compatible inputs.
    




    