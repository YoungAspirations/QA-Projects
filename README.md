# Personal Game Archive README
***
## Introduction<a name= "header"></a>
[//]: # "Write an introduction to the project and your motives."
This README.md is documentation for my DevOps core fundamental project where I was tasked to create a
fully functional Create Read Update Delete (CRUD) application. It must utilise the specified tools and skills
prior to starting the project.

## Table of Contents
1. [Introduction](#header)
2. [Requirements](#header2)
3. [Installation](#header3)
4. [Design](#header4)
8. [Entity Relationship Diagram](#header8)
16. [CI Pipeline](#header16)
7. [Trello Board](#header7)
10. [Risk Assessment](#header10)
9. [Testing](#header9)
17. [Front-End Design](#header17)
5. [Troubleshooting](#header5)
6. [Additional Improvements](#header6)
11. [Author](#header14)
12. [Acknowledgements](#header13)
13. [Contributors](#header12)
14. [Author](#header15)
15. [Licensing](#header11)


I will detail all phases of the project, from why specific tools were used, up to Jenkins for software
automation and testing. In addition, some additional thoughts for extra improvements will be stated towards the
end of the document.

## Requirements<a name= "header2"></a>
[//]: # "Add requirements to run app "
Here is a brief section on the skills and output requirements of the project that were not mentioned in the introduction.

### Skills
- Project Management - Planning, time management, and agile working
- Python Fundamentals - Basic Python Skills
- Python Testing - To check if the code works how we expect it to
- Git - Version Control
- Basic Linux - Commands to operate Linux machines
- Python Web Development - To build a web-based application
- Continuous Integration (CI) - CI through Jenkins 
- Cloud Fundamentals - The ability to use and configure Google Cloud Platforms (GCP) to generate virtual machines (VM) and databases
- Databases - Create databases and store inputs

### Output
- Risk Assessment - An analysis on potential risk factors in the project
- Relational Database - A relational database with at least 2 tables in it that can be used to store data
- Front-end website - Functional front-end website that uses Flask's integrated API's
- Trello Board - Kanban list-making tool used for project management
- Architecture - Documentation of database design
- Automated test suite - A test suite that runs automatically with Git webhooks 
- Feature-Branch Model - Use of Git branching feature throughout development cycle

## Installation<a name= "header3"></a>
[//]: # "Add installation procedure and alternatives to run app"

This section will detail the installation process of the application. If any issues arise make sure you check out the troubleshooting section first.

1. Fork the repository so that it is connected to your account. This will be necessary if you wish to integrate Jenkins or other CI tools

2. Click the green code button, choose SSH, and copy the text.

3. Go to VM and clone repository.

4. Next, enter the following commands in succesion

       sudo apt udate
       sudo apt install python3 python3-venv python3-pip
       python3 -m venv venv
       source venv/bin/activate
       pip3 install -r requirements.txt
       export DATABASE_URI=mysql+pymysql://username:password@host/database_name
       python3 create.py
       python3 app.py

For the line starting with 'export', substitute; username, password, host, and database with your credentials.

The app should now be running. But, if any issues persist, check out the troubleshooting section.

## Design<a name= "header4"></a>
Here is the design of the app functionality that I wished to create for the users.

- Create a user :
    - Username
    - First Name
    - Last Name
    - Password 
    - Email

- Add a game to their list with some details:
    - Game Title
    - Platform - The system that they play the game on
    - Rating - What score do they give the game
    - Status - They can state whether they plan to play the game or if it is completed etc.

- Add additional details about the game:
    - Publisher - What company published the game
    - Genre - Specify what type of game it is
    - Units Sold - How many copys of the game were sold
    - ESRB Rating - What age rating was given to the game
    - Engine - What development software was the game built on

- Users can view their games list with the additional details on the read page
- Users can update or delete games in their games list

Additional features that I would like the users to be able to do:

- A search feature to look for games through genre or publisher
- Write reviews and have them be able to update or delete them
- Be able to add friends
- View friends lists 

## Entity Relationship Diagram<a name= "header8"></a>
[//]: # "ER Diagram defining relationships of tables"

The diagram below is an entity relationship diagram for the database that I was aiming to create. It is an optional many to optional many relationship as shown by the cardinality lines between the users and games tables. This shows that users can have anywhere from 0 to multiple games, and vice-versa, a game can be associated to many users. Whereas, for the games and games details tables, games can only have 1 set of game details but game details may be associated with many games.

![Imgur](https://imgur.com/pReeMcC.png) 

## CI Pipeline<a name= "header16"></a>
![Imgur](https://imgur.com/qh2s3ku.png)

## Trello Board<a name= "header7"></a>
[//]: # "Trello board defining tasks"
Below is a Trello board (https://trello.com/b/DZAfzoB5/qa-crud-project) that I used for project management throughout the project.

![Imgur](https://imgur.com/UezbcN9.png)

The board was created to help with the development cycle while completing the project. The board follows a linear progression of the project from left to right with the following lists;

* Epic - The overall goal of the project
* User Story - Thoughts told by the end user of any functionality that they want in the product and why they may desire it
* In Progress - Where aspects of the project are being implementation in to the project
* Testing - Check to see if code from the previous section works within the constraints of the build
* Complete - This list shows all of the completed tasks

## Risk Assessment<a name= "header10"></a>
[//]: # "Self explanitory"
Here is an image of my risk assessment detailing the internal and external risk factors to the project.

![Imgur](https://imgur.com/Vvdp7eg.png)
## Testing<a name= "header9"></a>
[//]: # "Python code that was tested and why"
The testing on the application was done using unit testing to check specific outcomes of the application were coming out correctly and returned errors if not true. In addition, pytest-cov was used to give coverage reports for the application to see how much was tested. My results are shown below are for the pytest coverage report and pytest results from Jenkins respectively.

![Imgur](https://imgur.com/kSIQCsk.png)

![Imgur](https://imgur.com/vI5Altn.png)

## Front-End Design<a name= "header17"></a>

## Troubleshooting<a name= "header5"></a>
[//]: # "Any issues that can be troubleshooted should be listed here"
Here I will state any issues that I had regarding this project that may be applicable to you too.

### Connect machine to your Github account:

1. First open up a terminal in VS Code or in another place
2. Enter the first line just underneath and click enter until all prompts are gone. Next, enter the second line to view the public key and copy everything.
  
        ssh-keygen
        cat ~/.ssh/id_rsa.pub

3. Now, sign in to your Github and go to settings.
4. Finally, move to SSH and GPG keys under access and create new SSH key with a suitable name. You should receive an email.  

Configuration of global name and email on bash for Github usage:

Use the command below to set up global name and user when using Git for the first time on a new system.

    git config --global user.name "Your name"  
    git config --global user.email "Your_email@example.com" 

### Connecting to VM error:

If you follow best practices and delete a VM whenever you are finished for the day, then you may run into an error where you cannot connect to hosts after changing the external IP in the config file. A solution to this can be to view known hosts in the .ssh directory and delete the values. The command can be seen below. 

    nano ~/.ssh/known_hosts

Next, attempt to connect to remote host again and the problem should be solved.

Note: Thia can also happen whenever a VM is turned off.  

### Syntax:

Make sure that you use correct indentation and spell everything correctly as incorrect syntax or spelling may not show up as issue leading to a long troubleshooting session. 
## Additional Imporovements<a name= "header6"></a>

- Add a login/ account feature - as this was not part of the minimum viable product (MVP) I left it out
- A recommendation tool that gives users suggestions on games depending on their games list
- A filter feature by genre, rating etc.
- Password encrption







## Known Issues<a name= "header11"></a>
[//]: # "Known issues of the project"
Issues known to be causing to be causing complications for the app:

- When adding a game to the list, a game and user id is needed to input to store the game in the database 
- There is no use of email validators on the user account database, but that is an easy fix
- There is no password confimation to make sure that the user is entering the correct password
- Passwords are not being encrtypted before entering the database
- There is currently no protection from SQL Injections

## Acknowledgements<a name= "header12"></a>
[//]: # "Acknowledge contributors to the project; Victoria, Ryan, Harry etc."

I would like to acknowledge Ryan Wright, Harry Volker, Victoria Sacre, and Luke Benson for their teachings and support leading into and throughout this project.

Thank you Ryan for your Git and database training. Victoria for your Python knowledge. Harry for the Flask skills while Ryan was sick. And, lastly Luke for your amazing support and problem solving skills throughout the project week.

Without their support this project would not have been a success.

## Contributors<a name= "header13"></a>

The contributor to this project is Christopher Pierre-Samuel with a link given below. 

<a href="https://github.com/YoungAspirations/QA-Projects/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=YoungAspirations/QA-Projects" />
</a>

## Author<a name= "header14"></a>

Christopher Pierre-Samuel <c.pierre-samuel@hotmail.co.uk> 

## Licensing & Copyright<a name= "header15"></a>

© Christopher Pierre-Samuel, QA Academy

The DevOps Core Fundamental Project is licensed under the [MIT License](LICENSE).