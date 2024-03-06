![Logo](/documentation/welcome-logo.png)

# Hangman

## Goal for this Project

Welcome to the Hangman. The goal of this project is to create a Python based terminal game of hangman. The words will be randomly selected from an API and if API not available will be selected from a list of words stored locally in program. All user inputs to be validated and feedback to the player if any invalid inputs are made.  

## Table of Contents

- [Hangman](#hangman)
- [Goal for this Project](#goal-for-this-project)
- [Table of Contents](#table-of-contents)
- [UX](#ux)
  - [User Stories](#user-stories)
  - [Design](#design)
    - [Colours](#colours)
- [Flow Chart](#flow-chart)
- [Features](#features)
    - [Existing Features](#existing-features)
    - [Features to be implemented](#features-to-be-implemented)
- [Technologies used](#technologies-used)
    - [Languages](#languages)
    - [Tools](#tools)
- [Testing](#testing)
    - [Code Validation](#code-validation)
    - [Features Testing](#features-testing)
    - [User Stories Testing](#user-stories-testing)
    - [Bugs](#bugs)
    - [Unfixed Bugs](#unfixed-bugs)
- [Deployment](#deployment)
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

## Design

I used the code institite's [Python Essentials template](https://github.com/Code-Institute-Org/python-essentials-template) for my project which included the HTML and JavaScript code. 

### Colours

I installed and used the [Colorama](https://pypi.org/project/colorama/) library to add colour to my project, below are the different colours used:

- I mostly used Yellow throughout my project for the welcome message, prompts for user inputs and Congratulations message if word was guessed correctly.

    <details><summary>Yellow Colour</summary>

    ![Yellow](/documentation/welcome-yellow.png)
    ![Start](/documentation/start-game-yellow.png)
    ![Game](/documentation/game-yellow.png)


- I used green as feedback to the player that their guessed letter was correct.

    <details><summary>Green for Correct Guess</summary>

    ![Correct](/documentation/correct-green.png)

- I used red as feedback to the player that their guess was incorrect, that the game was over and if they made an invalid input.

    <details><summary>Red for Incorrect Guess</summary>

    ![Red Incorrect](/documentation/incorrect-red.png)
    ![Invalid](/documentation/invalid-red.png)
    ![Game Over](/documentation/game-over-red.png)



\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

## Flow Chart

I used [Lucid charts](https://www.lucidchart.com/pages/) to design the flow charts below.

*Initial design*

![Flow chart](/documentation/hangman-flow-chart.png)

*Updated design with game Level options*

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

### Instructions page

- When option 2 is entered the instructions page is displayed with the option to return to main menu once read. Again if an invalid input is made a message in red is displayed to press the enter key.

    <details><summary>Instructions Page</summary>

    ![Instructions](/documentation/instructions-page.png)

### Quit Page

- When option 3 is select the quit game page is displayed with a message that the player has quit game and to press on the Run Program buttom to re-start game.

    <details><summary>Quit Game Page</summary>

    ![Quit Page](/documentation/quit-page.png)

### Game level Page

- When option 1 is selected the select game level page is displayed with the options of 1 for easy level with 4 letter word, 2 for medium level with 6 letter word or 3 for hard level with 8 letter word. Again when an invakid input is made a message highlighted in red is displayed to input a number between 1 and 3.

    <details><summary>Select Game level Page</summary>

    ![Select Level](/documentation/select-level-page.png)

### Game Page

- Depending on the gane level selection the game page is displayed for easy, medium or hard. Using the [Random word API](https://random-word-api.herokuapp.com/home) website a word with 4, 6 or letters is randomly retrived from the api. Once an valid input is made it is checked if it is correct or incorrect. If correct a green correct message is displayed and all attempt remain. If incorrect an attempt is lost and 1 stage of the hangman is displayed.

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

### Game over Page

- If all the letters in the word are quessed correctly a congratulations message is displayed and a message to press return to go back to main menu. If the player runs out of attempts a game over meassage is displyed in red and the correct word is displayed. Again a message to press enter to return to the main menu is displayed. If anything other than return is press an invalid input message to press return is displayed in red.

- If anything other than a single aphabetical letter is entered or has not been already guessed an ivalid input message is displayed in red.

    <details><summary>Game Over Screenshots</summary>

    *Word guessed correctly*

    ![Winner](/documentation/game-over-congrats.png)

    *Game Over, no attempts remaining*

    ![No Attempts left](/documentation/game-over-red.png)

    *Invalid Guess Input*

    ![Invalid input](/documentation/game-invalid-guess.png)

    *Invalid Enter Input*

    ![Invalid Enter](/documentation/game-over-invalid.png)
  

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

## Features to be Implemented

- In the future I would like to implement google sheets as a database to transfer scores and username of player. The score would be calculated based on the amount of attempts used to guess word correctly. Then display that data as a leaderboard for each of the levels. 

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

## Technologies used

### Languages

* [HTML](https://en.wikipedia.org/wiki/HTML "HTML")
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript "JS")
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language) "Python")

### Libraries & Framework

* 

### Tools
* []()


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


### Features Testing


\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;
        
### User Stories Testing

- Table of User Story Testing.

    | User Story | Testing |
    | :--- | :--- | 
    |As a user, I want instructions on how to play the game.|On the home menu page selct number 2 to display the instructions for the game.|
    |As a user, I want to have the option of selecting different levels of difficulty.|Select 1 on main menu to start game and the difficulty level option is display first, select 1 for easy (4 letter word), 2 for medium (4 letter word) or 3 for hard level (8 letter word).|
    |As a user, I want to know if my inputs are valid and get feedback if not.|If you enter anything but a sinle alphabetical letter you will get an invalid iput message highlighted in Red|
    |As a user, I want to know if my input is correct or not.|If letter is in word a correct message in green is displayed and the letter is placed in the secret word.|
    |As a user, I want to know what inputs I have already made.|All your inputs already quessed are displayed in yellow, if you select the same letter again you do not loose an attempy but get a message highlighted in red that you alreay guessed that letter.|
    |As a user, I want do know my current attempt status is during game.|The amount of attempts remaining are displayed at the top of the screen above the hangman stages.|
    |As a user, I want to know correct word if I run out of attempts.|If you run out of attempts you will get a message highlighted in red that the game is over and underneath that is diplayed what the correct word was.|
    |As a user, I want the option to play the game again when finished.|When game is over ther is a message displayed in Yellow to press return to go back to the main menu where you can start the game again.|

&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

### Bugs

- When I installed art ascii for welcome message it worked locally but not on the deployed site. I resolved by running the command  pip3 freeze > requirements.txt in the terminal to update the dependsies installed. Once app was rebuilt by Heroku the art was displayed on deployed site.

    <details><summary>Bug</summary>

    ![Bug]()

- When new py file created I had problems with the run.py not running. This was because I did not have correct path to new files created. I saved new files in src folder so once i put correct path (eg. src.valiadation instead of just validation) in the problem was resolved.

    <details><summary>Bug</summary>

    ![Bug]()




### Unfixed Bugs



\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

## Deployment

The site was deployed using Heroku following the steps below:

- Create a list of requirements using the following command in the terminal (pip3 freeze > requirements.txt).

- Heroku searches for this exact file name as it builds the project. This file contains the list of the packages installed during project development which are called dependencies. We need Heroku to install these dependecies as well in order for the project to run. 

- Activate your Heroku Student Pack account at the following link: [Heroku for Students]( https://www.heroku.com/github-students).

- From Heroku Dashboard click on **Create New App**, enter name of app, choose your region and then click **Create App**.

- Click on the **Settings** tab of the newly created app.

- Go to **Config Vars** section and in the field for KEY enter **PORT**, in the VALUE field enter *8000* and then click **ADD**.

- If your project uses a **creds.json** file you will need to set a config var by adding **CREDS** to KEY field and copying contents of creds.json file into VALUE field.

- Go to Buildpacks section and click on **Add buildpack**.

- Select **python** and click on **Save changes**.

- Click on **Add buildpack** again, select **nodejs** and click on **Save changes**.

- Make sure buildpacks are in order with python on top and nodejs underneath.

- Click on **Deploy** tab at top of screen.

- In **Deployment method** section selct **GitHub** and confirm by clicking **Connect to GitHub**.

- Serach for your GitHub repository name, once found click **Connect**.

- Scroll down on page and select either **Enable Automatic Deploys** which will rebuild your app every time you push a new change to GitHub or **Deploy Branch** which is a manual deployment so has to be selected after each change pushed to GitHub.

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



\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;


