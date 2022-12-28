# UVAH

A resource hub for learners giving them easy access to the best resources on the internet for any technical domain. The project works on user ratings where the best rated courses for a specific topic are shown at the top.

# Features

- Content rating system
- Users can suggest Recourses
- Admins can accept or reject suggested resources
- Users can bookmark content
- Custom profile page showing the suggested and bookmarked courses for a user
- Login and Signup page using latest authentication practices

![image](https://user-images.githubusercontent.com/45175270/209334209-5b3e4292-8901-4538-bd6f-e48de23976a3.png)

## Tech Stack

**Client:** HTML, CSS, Javascript, Django Templating Language

**Server:** Python, Django

**Database:** SQLite

## Run Locally

*To run this project, you need to install NodeJS on your machine.*

Clone the project

```bash
  git clone https://github.com/aitchessbee/uvah
```

Go to the project directory

```bash
  cd uvah
```

We recommend you to use virtual environment

```bash
  python -m venv env
```

Activate virtual environment   
For Windows PowerShell
```bash
    env/Scripts/activate.ps1
```
For Linux and MacOS
```bash
    source env/bin/activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Add *Security Key* : Go to project's *settings.py* file and change the value of *SECURITY_KEY* variable to desired security key.

Run Migrations

```
 python manage.py makemigrations
```
```
 python manage.py migrate
```

Start the server

```bash
  python manage.py runserver
```

## Endpoints

- / - Landing page
- signup/ - Register for the test
- login/ - Login to portal
- instructions/ - Instructions and Countdown to test time

## Team

- [Harsiddak Singh Bedi](https://github.com/Aitchessbee)
- [Vishist Bhagabati](https://github.com/VishistB)
