![Logo](/documentation/welcome-logo.png)

# Hangman

## Goal for this Project

The goal of this project is to create a Python based terminal game of hangman. The words will be randomly selected from an API and if API is not available will be selected from a list of backup words file. All user inputs to be validated and feedback to the player if any invalid inputs are made.  

## Table of Contents

- [Hangman](#hangman)
- [Goal for this Project](#goal-for-this-project)
- [Table of Contents](#table-of-contents)
- [UX](#ux)
  - [User Stories](#user-stories)
  - [Design](#design)
    - [Colours & ASCII Art](#colours--ascii-art)
- [Flow Chart](#flow-chart)
- [Features](#features)
    - [Existing Features](#existing-features)
    - [Features to be implemented](#features-to-be-implemented)
- [Technologies used](#technologies-used)
    - [Languages](#languages)
    - [Libraries & Framework](#libraries--framework)
    - [Tools](#tools)
- [Testing](#testing)
    - [Code Validation](#code-validation)
    - [Features Testing](#features-testing)
    - [User Stories Testing](#user-stories-testing)
    - [Browser Compatibility](#browser-compatibility)
    - [Bugs](#bugs)
    - [Unfixed Bugs](#unfixed-bugs)
- [Deployment](#deployment)
    - [Heroku](#heroku)
    - [Fork](#fork)
    - [Clone](#clone)
- [Credits](#credits)

## UX

## User Stories

* As a user, I want instructions on how to play the game. 

* As a user, I want to have the option of selecting diffent levels of difficulty.

* As a user, I want to know if my inputs are valid and get feedback if not.

* As a user, I want to know if my input is correct or not.

* As a user, I want to know what inputs I have already made.

* As a user, I what do know my current attempt status is during game.

* As a user, I want to know correct word if I run out of attempts. 

* As a user, I want the option to play the game again when finished.

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

## Design

I used the code institite's [Python Essentials template](https://github.com/Code-Institute-Org/python-essentials-template) for my project, the template included the HTML and JavaScript code which I did not alter.  

My Python code is seperated into different files called modules and located in a source(src) folder. These modules can then be imported and used in other files. This process design of **modular programming** promotes better code organization, reusability, and maintainability. I ensured that there was no **circular dependencies** which occurs when module A for example imports a function from module B and vice versa. Circular dependencies can lead to errors and make code difficult to manage.

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

### Colours & ASCII Art

I installed and used the [Colorama](https://pypi.org/project/colorama/) library to add colour to my project. I also instaleed [pyfiglet](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/) for the welcome message ascii art font.

- I mostly used Yellow for sharper contrast throughout my project. This includes the welcome message, prompts for user inputs and Congratulations message if word was guessed correctly.

    <details><summary>Colour and ASCII Screenshots</summary>

    *Home page*

    ![Home](/documentation/welcome-yellow.png)

    *Level page*

    ![Game Level](/documentation/start-game-yellow.png)

    *Game page*

    ![Game](/documentation/game-yellow.png)

    *Guessed word correctly*

    ![Winner](/documentation/game-over-congrats.png)

- I used green as feedback to the player that their guessed letter was correct.

    <details><summary>Colour Screenshot</summary>

    *Green for correct guess*

    ![Correct](/documentation/correct-green.png)

- I used red as feedback to the player that their guess was incorrect, that their input was invalid and that the game was over after running out of attempts.

    <details><summary>Colour Screenshots</summary>

    *Incorrect guess*

    ![Red Incorrect](/documentation/incorrect-red.png)

    *Invalid input*

    ![Invalid](/documentation/invalid-red.png)

    *Game over*

    ![Game Over](/documentation/game-over-red.png)

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

## Flow Chart

I used [Lucid charts](https://www.lucidchart.com/pages/) to design the flow charts below for the project.

![Flow chart](/documentation/hangman-flow-chart_2.png)

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

## Features

## Existing Features

### Home Menu Page

- The home menu page includes a welcome message and the option to start game, read instructions or to quit game. 

    <details><summary>Home Menu Page</summary>

    ![Land](/documentation/welcome-yellow.png)

- If the user inputs an invalid option an invalid message is displayed in Red with feedback to player to enter a number between 1 and 3.

    <details><summary>Invalid Input message</summary>

    ![Invalid Input](/documentation/menu-invalid.png)

### Game level Selection Page

- When option 1 is selected the select game level page is displayed with the options of 1 for easy level with 4 letter word, 2 for medium level with 6 letter word or 3 for hard level with 8 letter word to guess. Again when an invalid input is made a message highlighted in red is displayed to input a number between 1 and 3.

    <details><summary>Select Game level Page</summary>

    ![Select Level](/documentation/select-level-page.png)

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

### Instructions page

- When option 2 is selected the instructions page is displayed with the option to return to main menu once read. Again if an invalid input is made a message in red is displayed to press the enter key.

    <details><summary>Instructions Page</summary>

    ![Instructions](/documentation/instructions-page.png)

### Quit Page

- When option 3 is selected the quit game page is displayed with a message that the player has quit game and to press on the Run Program buttom to re-start game.

    <details><summary>Quit Game Page</summary>

    ![Quit Page](/documentation/quit-page.png)

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

### Game Page

- Depending on the game level selection the game page is displayed for easy, medium or hard. Using the [Random word API](https://random-word-api.herokuapp.com/home) website a word with 4, 6 or letters is randomly retrieved from the api. Once an valid input is made it is checked if it is correct or incorrect. If correct a green correct message is displayed and all 7 attempts remain. If incorrect an attempt is lost and the next stage of the hangman is displayed.

- If the random word API website is not available for any reason a rondom word is selected from a list of backup words from the words.py file.

    <details><summary>Game Page Screenshots</summary>

    *Easy Level*

    ![Easy](/documentation/easy-level.png)

    *Medium Level*

    ![Medium](/documentation/medium-level.png)

    *Hard Level*

    ![Hard](/documentation/hard-level.png)

    *Random Word API not available message*

    ![API not available](/documentation/word-api-failure.png)

- If all the letters in the word are quessed correctly a congratulations message is displayed and a message to press return to go back to main menu. If the player runs out of attempts a game over meassage and the last hangman stage is displyed in red and the correct word is displayed. Again a message to press enter to return to the main menu is displayed. If anything other than enter is pressed an invalid input message to press enter key is displayed in red.

- If anything other than a single aphabetical letter is entered or the letter has already been guessed an ivalid input message is displayed in red.

    <details><summary>Game Over Screenshots</summary>

    *Word guessed correctly*

    ![Winner](/documentation/game-over-congrats.png)

    *Game Over, no attempts remaining*

    ![No Attempts left](/documentation/game-over-red.png)

    *Invalid guess input*

    ![Invalid input](/documentation/game-invalid-guess.png)

    *Invalid enter input*

    ![Invalid Enter](/documentation/game-over-invalid.png)
  
\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

## Features to be Implemented

- In the future I would like to implement google sheets as a database to export scores and username of player. The score would be calculated based on the amount of attempts used to guess word correctly. The username and scores would then be imported and displayed on a leaderboard for each of the levels. 

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

## Technologies used

### Languages

* [HTML](https://en.wikipedia.org/wiki/HTML "HTML") Included in CI Template.
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript "JS") Included in CI Template.
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language) "Python")

### Tools & Libraries

* [Colorama](https://pypi.org/project/colorama/)
* [ASCII Generator](https://pypi.org/project/pyfiglet/)
* [API Requests](https://pypi.org/project/requests/)
* [OS](https://pypi.org/project/os-sys/)
* [Math Random](https://www.w3schools.com/python/module_random.asp)
* [pyfiglet](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/)
* [Random words API](https://random-word-api.herokuapp.com/home)
* [Lucid Charts](https://www.lucidchart.com/pages/)
* [Python Validator](https://pep8ci.herokuapp.com/)
* [Heroku](https://dashboard.heroku.com/apps)

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

## Testing

### Code Validation

- I used code institute's [Python Linter](https://pep8ci.herokuapp.com/#) to validate my code. No errors were found during final testing, screenshots of project files below:

    <details><summary>Code Validation Screenshots</summary>

    *run.py file*

    ![Run](/documentation/run-file.png)

    *api.py file*

    ![API](/documentation/api-file.png)

    *ascii_art*

    ![ASCII](/documentation/ascii_art-file.png)

    *game.py file*

    ![Game](/documentation/game-file.png)

    *instructions.py file*

    ![Instructions](/documentation/instructions-file.png)

    *utils*

    ![Utils](/documentation/utils-file.png)

    *validation.py file*

    ![Validation](/documentation/validation-file.png)

    *words.py file*

    ![Words](/documentation/words-file.png)

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

### Features Testing

- Home Menu Page 

    |Items being tested|Actions taken to test|Expected result|Outcome|
    |---|---|---|---|
    |Welcome message|Clicked on [Live Link](https://kevin-flanagan-hangman-6c9777c7535e.herokuapp.com/) in README.|The welcome message in yellow colour is displayed.|:white_check_mark:|
    |Menu options|Clicked on [Live Link](https://kevin-flanagan-hangman-6c9777c7535e.herokuapp.com/) in README.|The options to start game, show instructions or quit game are displayed| :white_check_mark:|
    |Input message|Clicked on [Live Link](https://kevin-flanagan-hangman-6c9777c7535e.herokuapp.com/) in README.|Message to input 1, 2 or 3 is displayed|:white_check_mark:|
    |Validation|Clicked on a number other than 1, 2 or 3, Clicked on letters and spacebar|Invalid input message displayed|:white_check_mark:|

    <details><summary>Home Menu Page Features</summary>

    *Home page*

    ![Home](/documentation/welcome-yellow.png)

    *Invalid input*

    ![Invalid Input](/documentation/menu-invalid.png)

- Game level Page

    |Items being tested|Actions taken to test|Expected result|Outcome|
    |---|---|---|---|
    |Game levels|Entered number 1 on main menu|Game level selection page displayed and options to enter 1, 2 or 3 for easy, medium or hard level|:white_check_mark:|
    |Validation|Clicked on a number other than 1, 2 or 3, Clicked on letters and spacebar|Invalid input message displayed|:white_check_mark:|

    <details><summary>Game Level Page Features</summary>

    *Game levels*

    ![Levels](/documentation/start-game-yellow.png)

    *Invalid input*

    ![Invalid](/documentation/select-level-page.png)

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

- Instructions page

    |Items being tested|Actions taken to test|Expected result|Outcome|
    |---|---|---|---|
    |Instructions|Entered number 2 on main menu|Instructions page displayed with message to press return to go back to main menu|:white_check_mark:|
    |Validation|Pressed keys other than return key|Invalid input message displayed|:white_check_mark:|
    |Return|Pressed return key|Main main page displayed|:white_check_mark:|

    <details><summary>Instructions Page Features</summary>

    *Instructions page*

    ![Invalid](/documentation/instructions-page.png)

- Quit Page

    |Items being tested|Actions taken to test|Expected result|Outcome|
    |---|---|---|---|
    |Quit game|Entered number 3 on main menu|Message quiting game and to press run program button to re-start displayed|:white_check_mark:|

    <details><summary>Quit Page Features</summary>

    *Quit page*

    ![Quit](/documentation/quit-page.png)

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

- Game Page

    |Items being tested|Actions taken to test|Expected result|Outcome|
    |---|---|---|---|
    |Easy Level|Entered 1 on game level page|Easy level with 4 letter word to guess displayed along with 1st hangman stage, word to guess, guessed letters and option to input guess|:white_check_mark:|
    |Medium Level|Entered 2 on game level page|Medium level with 6 letter word to guess displayed|:white_check_mark:|
    |Hard Level|Entered 3 on game level page|Hard level with 8 letter word to guess displayed|:white_check_mark:|
    |Backup Words|Removed URL for random word API|Failed to retrieve words from API message displayed|:white_check_mark:|
    |Invalid Guess|Entered numbers, spaces, 2 letters and letters already guessed|Invalid input message displayed|:white_check_mark:|
    |Guessed word correctly|Successfully guessed word|Congratulations message in Yellow displayed and option to return to main menu|:white_check_mark:|
    |Guessed word Incorrectly|Incorrectly guessed word|Game Over message in Red displayed, final hangman stage displayed in Red, correct word displayed and option to return to main menu|:white_check_mark:|

    <details><summary>Game Page Features</summary>

    *Easy*

    ![Easy](/documentation/easy-level.png)

    *Medium*

    ![Medium](/documentation/medium-level.png)

    *Hard*

    ![Hard](/documentation/hard-level.png)

    *Backup*

    ![Backup](/documentation/word-api-failure.png)

    *Invalid input*

    ![Invalid](/documentation/game-invalid-guess.png)

    *Guessed correctly*

    ![Congrats](/documentation/game-over-congrats.png)

    *Guessed incorrectly*

    ![Game Over](/documentation/game-over-red.png)

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;
        
### User Stories Testing

- Table of User Story Testing.

    | User Story | Testing |
    | :--- | :--- | 
    |As a user, I want instructions on how to play the game.|On the home menu page select number 2 to display the instructions for the game.|
    |As a user, I want to have the option of selecting different levels of difficulty.|Select 1 on main menu to start game and the difficulty level option is displayed. Select 1 for easy (4 letter word), 2 for medium (6 letter word) or 3 for hard level (8 letter word).|
    |As a user, I want to know if my inputs are valid and get feedback if not.|If you enter anything but a sinle alphabetical letter you will get an invalid iput message highlighted in Red|
    |As a user, I want to know if my input is correct or not.|If letter is in word a correct message in green is displayed and the letter is placed in the secret word.|
    |As a user, I want to know what inputs I have already made.|All your inputs already quessed are displayed in yellow, if you select the same letter again you do not lose an attempt but get a message highlighted in red that you alreay guessed that letter.|
    |As a user, I want to know what my current attempt status is during game.|The amount of attempts remaining are displayed at the top of the screen above the hangman stages.|
    |As a user, I want to know correct word if I run out of attempts.|If you run out of attempts you will get a message highlighted in red that the game is over and underneath that is diplayed what the correct word was.|
    |As a user, I want the option to play the game again when finished.|When game is over there is a message displayed in Yellow to press return to go back to the main menu where you can start the game again.|

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

### Browser Compatibility

- Table of Browsers tested, as the project is terminal based mobile device testing was not applicable.

  | Browser | Intented Appearance | Intented Responsiveness | 
    | --------| ------------------- | ----------------------- |
    | Chrome  | Good | Good | 
    | Edge    | Good | Good | 
    | Firefox | Good | Good |

    <details><summary>Browser compatibility Screenshots</summary>

    *Chrome*

    ![Chrome](/documentation/chrome.png) 

    *Edge*

    ![Edge](/documentation/edge.png)

    *Firefox*

    ![Firefox](/documentation/firefox.png)

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

### Bugs

- When I installed art ascii for welcome message it worked locally but not on the deployed site. I resolved problem by running the command  `pip3 freeze > requirements.txt` again in the terminal to update the dependencies installed. Once app was rebuilt by Heroku the art was displayed on deployed site.

- When new py file created I had problems with the run.py not running. This was because I did not have correct path to new files created. I saved new files in src folder so once I put correct path (eg. src.valiadation instead of just validation) in the problem was resolved.

    <details><summary>Incorrect Path</summary>

    ![Incorrect Path](/documentation/incorrect-path-bug.png)

- Following the recommendation in the deployment video of the Love Sanwiches walkthrough project, I added a new line character `\n` to all inputs to avoid potential bug in the software used to create the mock terminal causing the text not to show up in the input terminal.

### Unfixed Bugs

- There are no bugs with the game that I am aware of.

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

## Deployment

### Heroku

The site was deployed using Heroku following the steps below:

- Create a list of requirements using the following command in the terminal (pip3 freeze > requirements.txt).

- Heroku searches for this exact file name as it builds the project. This file contains the list of the packages installed during project development which are called dependencies. We need Heroku to install these dependecies as well in order for the project to run. 

- Activate your Heroku Student Pack account at the following link: [Heroku for Students]( https://www.heroku.com/github-students).

- From Heroku Dashboard click on **Create New App**, enter name of app, choose your region and then click **Create App**.

- Click on the **Settings** tab of the newly created app.

- Go to **Config Vars** section and in the field for KEY enter **PORT**, in the VALUE field enter *8000* and then click **ADD**.

- If your project uses a **creds.json** file you will need to set a config var by adding **CREDS** to KEY field and copying contents of creds.json file into **VALUE** field.

- Go to Buildpacks section and click on **Add buildpack**.

- Select **python** and click on **Save changes**.

- Click on **Add buildpack** again, select **nodejs** and click on **Save changes**.

- Make sure buildpacks are in order with python on top and nodejs underneath.

- Click on **Deploy** tab at top of screen.

- In **Deployment method** section selct **GitHub** and confirm by clicking **Connect to GitHub**.

- Serach for your GitHub repository name, once found click **Connect**.

- Scroll down on page and select either **Enable Automatic Deploys** which will rebuild your app every time you push a new change to GitHub or **Deploy Branch** which is a manual deployment so has to be selected after each change pushed to GitHub.

- Once app is built you can click on **Open app** at top of page which will open app on new page where you can copy URL. 

### Fork

To make a copy of a repository or to fork it using Github follow below steps:

- Go to **Github repository** to be copied.
- Click on the **Fork** button in upper right corner of page to copy.

### Clone

To copy the repository to your local machine in Github follow steps below:

- Go to **Github repository** to be cloned.
- Click on the **Code** button above the list of files.
- Select to clone using either  **HTTPS**, **SSH**, or **Github CLI** and click the **copy** button to copy the URL to clipboard.
- Open **Git Bash**.
- Change the current working directory to the one where you want the cloned directory.
- Type **git clone** and paste the URL from the clipboard. 
- Press **Enter** to create your local clone.

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

## Credits

For help and advice:

- [Simen Daehlin](https://github.com/Eventyret "Simen Daehlin")

Code inspiration:

- [Love Sandwichwes and LMS from Codeinstitute](https://codeinstitute.net "Love Sandwiches Project")

Code inspiration for guessing letters in game:

- [Youtube CodeFather Tutotial](https://www.youtube.com/watch?v=gJBeYcqHNCM&t=1044s "Youtube")

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;
