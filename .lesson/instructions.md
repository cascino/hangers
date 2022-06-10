# HangMan Instructions  
You are tasked with creating the word guessing game, hangman.   The game is to provide a user with a puzzle that has had all its letters masked or hidden to the user. Only non letters should be shown which includes but is not limited to spaces, apostrophes, dashes, ect.  The user must then try to solve the puzzle by guessing what the hidden letters are.   The game continues until the player correctly guesses the puzzle or accumulates a certain number of errant guesses.  You are encouraged to come up with an alternative representation of the game to communicate how many errors have been made.  

For example you could use a Pokeball that gets ‘hit’ and opens to release a Pokemon each there is a wrong guess.  The game ends when there are no more Pokemon left in the Pokeball.   

  
Generate code that will allow a user to play hangman. Your code must include the following:
- File I/O to store at least 4 puzzle categories which will contain at least 100 separate strings for each category.  There must be puzzles consisting of more than one word.
- The code must be able to process strings up to 50 characters.
- Puzzle words must be selected from the file list at random.
- A puzzle cannot be selected more than once on any given session.
- Puzzle words must be processed as lists, words strings, and guesses as characters.
- The user should get constant feedback as to their progress in the puzzle, what letters have been selected, display the puzzle with the correctly guessed letters in place, and how many wrong guesses they have made.

- You are expected to provide a full graphical user interface which does not require ANY keyboard strokes.  You can still get a passing grade without the use of a full GPU but your mark will be capped at 75%.
- Additional marks will be given for ingenuity and creativity. Adding a feature(s) to your program which enhances game play, adds functionality, and/or  adds a wow factor will be rewarded with a higher evaluation.
- The user interface must be robust and handle common errors gracefully (i.e. the code should not crash)
- The program should end only when the user wishes to by selecting quit.

# Coding Expectations
Use coding styles, methods, and libraries that come from the course material **ONLY**.  The goal of this summative project is to demonstrate what you have learnt from the course material.  It is not primarily about the game.  The use of libraries or method calls that were not explicitly covered in class could lead to mark deductions as they could potentially mask gaps in your understanding or knowledge of the course material. Be sure to OK any code that you have come up with that does not come from the textbook or the chapters provided to you throughout the course.

 
Ensure you demonstrate:
- Code Documentation
 >Make sure your use of function and variable names make it clear what each represents. You are also expected to comment your code, give a brief description of each and every function just above the function definition.

- Code Modularity
>Each function should complete one main task and there should be no unnecessary code duplication. Also make sure that you keep the number of parameters to a minimum. 

- Effective Use of Data Structures
  >including lists, strings, ints, floats, Boolean, etcCode should be as efficient as possible.  Use data types and structures efficiently. Remember, ints should be used as default number representation unless a float is necessary. 

- Efficient File I/O Use
  >and avoid repeated reads.

- Efficient Control Statements
  >Be sure to use the correct control statement(s) given the context of the condition you are trying to capture. For example, avoid using multiple one way conditionals when a single multi-way conditional is more prudent.

- Effective and Robust Error Handling
  >Dummy proof any input from the user and ensure the program starts and stops gracefully. 
  
  >Be sure to eliminate both logical and literal errors in your code by using the techniques learnt in class.
- Run Code From main()
> Use the main() function to control the overall program.  Be sure to include aLL files needed to run your code.
