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

### Home Page

- The home page 

    <details><summary>Home Page</summary>

    *Home Page*

    ![Land](/documentation/landing-mobile.png)

    

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
* [CSS](https://en.wikipedia.org/wiki/CSS "CSS")
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

- 


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


