# Capstone Commands Project- Little Tech Helper(LTH)

This is a Capstone project for Udacity Full Stack Web Development Nano Degree Program.
I have created a project that will show users various shortcuts or commands used in different languages like 'python','java','sql' by developers.


## Getting Started

### Virtual Environment
Little tech helper has been deployed on Heroku. The link to that is:-
https://dashboard.heroku.com/apps/capstone-command-project

### PIP Dependencies
No need to install anything if you are running the app on heroku.
To run the app locally, you need to install the dependencies using requirements.txt.
```bash
pip install -r requirements.txt
```

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.


## Running the server

To run the server on heroku you just have to go to the link above.
To run the server locally, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```
Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application.


## API Reference

### Roles
This project has two roles:- 

- anyone can see all the commands in the database. 

- ###### Manager
    who can add,delete,update commands. Also can see and delete suggestions given by users.
    Permissions:-
        get:categorised-commands
        get:categories
        post:commands
        delete:commands
        patch:commands
        add:suggestions
        get:suggestions
        delete:suggestions

    Manager Bearer Token:- eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImdnQ2dQckVyUEhkTklvLXAwS3VTOCJ9.eyJpc3MiOiJodHRwczovL3ByYW5pdGEtcGQudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmNWUzZGFjYzBlNTllMDA3NmYxNzY4ZCIsImF1ZCI6IkNvZGluZ19jb21tYW5kcyIsImlhdCI6MTYwMDUzMDc4MCwiZXhwIjoxNjAwNjE3MTgwLCJhenAiOiJnYVVuM1BOOGp1dDlXWUk3UGZvYlFyelN6ZjZoUDF5QSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiYWRkOnN1Z2dlc3Rpb25zIiwiZGVsZXRlOmNvbW1hbmRzIiwiZGVsZXRlOnN1Z2dlc3Rpb25zIiwiZ2V0OmNhdGVnb3JpZXMiLCJnZXQ6Y2F0ZWdvcmlzZWQtY29tbWFuZHMiLCJnZXQ6c3VnZ2VzdGlvbnMiLCJwYXRjaDpjb21tYW5kcyIsInBvc3Q6Y29tbWFuZHMiXX0.h0EZ2GVVvj1bGHAiZX7ochSe2OWmas3g9S2wW6zgiq7MCZ2l3iKkwKieEh_Y-Y7xD6euEY8hyy4togrBZCtE7Gj6p2gb6lOXj5GBGU_0zXrVeq-qLcFyb2uuMNOkODNPFeGBaY1FtFilpt7IxsMlsv1cZdMfmvXMhnZQwTip4Cn09i4YBPVyObDm2iydW9qVDi6ms1M-7V2omMgvvkPg2GY-wG0i6ZgxjW0YsdcArt4OKdX0HMoAEp7Q2iYAU5chZ01Wdo9EqoPqBTMeygNzaeq8VjNKHhJJVnypSrUKwTKDepQ0pCeBrSqW7wqU27dovvc12WM3FY9aZnCrn0uI2A

- ###### User
    who can add suggestions and see the commands with or without categories.
    Permissions:-
        get:categorised-commands
        get:categories
        add:suggestions

    User Bearer Token:-
    eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImdnQ2dQckVyUEhkTklvLXAwS3VTOCJ9.eyJpc3MiOiJodHRwczovL3ByYW5pdGEtcGQudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmNWUzZTEzY2I3ZGU3MDA2OTc4NWNiMSIsImF1ZCI6IkNvZGluZ19jb21tYW5kcyIsImlhdCI6MTYwMDUzNjc5NCwiZXhwIjoxNjAwNjIzMTk0LCJhenAiOiJnYVVuM1BOOGp1dDlXWUk3UGZvYlFyelN6ZjZoUDF5QSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiYWRkOnN1Z2dlc3Rpb25zIiwiZ2V0OmNhdGVnb3JpZXMiLCJnZXQ6Y2F0ZWdvcmlzZWQtY29tbWFuZHMiXX0.qdaybf5Gq437Zq-k3Eqlnf5yDtK8zWve4-tHP1rRRfgaAAr4OJQMu-mNExNiox3a9CjfTEhbOlUAJZ4YtqI4zwNTIlw_pShgI91bfke8kao87GA9IBR9XmD-6J_DaHrBpKGlIpHZZ4BQ4W2Y4aWzc-5KTdIludbp49BsQkhVKkq5G0Jp7TG5iw_pEHn64VCgxiyK4PvB86VQq8tCcZtNwUzpHsqr3GeVXxzPYpROYGWnXffshbBu-O9maX_TRud-zY7hyhfBLKgfs2dXjKmN-qyoQaMu5Hd1PZEEHYBEiUoRfxBV4qBHIiN2HddrkCb7cTXY3i7gN7ODwyDst6arVA

### Error Handling

Error are handled in following format-
{
  "error": 404,
  "message": "resource not found",
  "success": false
}

Errors handled are of following types:-
- 400: Bad Request
- 404: Resource Not Found
- 405: method not allowed

### Endpoints
I ran the following commands on postman and for the app deploed on heroku.
- Sample: GET https://capstone-command-project.herokuapp.com/categories
- Output:
{
    "categories": [
        {
            "category": "java",
            "id": 1
        },
        {
            "category": "script",
            "id": 2
        },
        {
            "category": "python",
            "id": 3
        },
        {
            "category": "sql",
            "id": 4
        }
    ],
    "success": true
}

- Sample: GET https://capstone-command-project.herokuapp.com/commands
- Output:
{
    "all_commands": [
        {
            "category": 1,
            "command": "System.out.println(\"Hello World\");",
            "explanation": "print something on console",
            "id": 1
        },
        {
            "category": 2,
            "command": "vi filename",
            "explanation": "edit the file",
            "id": 2
        },
        {
            "category": 3,
            "command": "python filename",
            "explanation": "run a python file",
            "id": 3
        },
        {
            "category": 4,
            "command": "SELECT * FROM TABLENAME",
            "explanation": "print every value in all the columns",
            "id": 4
        }
    ],
    "success": true
}

- Sample: GET https://capstone-command-project.herokuapp.com/suggestions
- Output:
{
    "success": true,
    "suggestions": [
        {
            "category": 1,
            "id": 1,
            "suggestion": "Please add a command for reading file in java"
        }
    ]
}

- Sample: (categorised commands)GET https://capstone-command-project.herokuapp.com/commands/1
- Output:
{
    "commands": [
        {
            "category": 1,
            "command": "System.out.println(\"Hello World\");",
            "explanation": "print something on console",
            "id": 5
        }
    ],
    "success": true
}

- Sample: PATCH https://capstone-command-project.herokuapp.com/commands/4
- Raw Json data supplied:
{
    "explanation": "SELECT * FROM TABLENAME;"
}
- Output:
{
    "commands": [
        {
            "category": 2,
            "command": "vi filename",
            "explanation": "edit the file",
            "id": 2
        },
        {
            "category": 3,
            "command": "python filename",
            "explanation": "run a python file",
            "id": 3
        },
        {
            "category": 1,
            "command": "System.out.println(\"Hello World\");",
            "explanation": "print something on console",
            "id": 5
        },
        {
            "category": 2,
            "command": ":q",
            "explanation": "quit file",
            "id": 6
        },
        {
            "category": 4,
            "command": "\"SELECT * FROM TABLENAME\"",
            "explanation": "\"SELECT * FROM TABLENAME;\"",
            "id": 4
        }
    ],
    "success": true,
    "updated_command": {
        "category": 4,
        "command": "\"SELECT * FROM TABLENAME\"",
        "explanation": "\"SELECT * FROM TABLENAME;\"",
        "id": 4
    }
}

- Sample: POST : https://capstone-command-project.herokuapp.com/commands
- Raw Json data supplied:
{
    "command":":q",
    "category":2,
    "explanation":"quit file"
}
- Output:
{
    "all_commands": [
        {
            "category": 2,
            "command": "vi filename",
            "explanation": "edit the file",
            "id": 2
        },
        {
            "category": 3,
            "command": "python filename",
            "explanation": "run a python file",
            "id": 3
        },
        {
            "category": 4,
            "command": "SELECT * FROM TABLENAME",
            "explanation": "print every value in all the columns",
            "id": 4
        },
        {
            "category": 1,
            "command": "System.out.println(\"Hello World\");",
            "explanation": "print something on console",
            "id": 5
        },
        {
            "category": 2,
            "command": ":q",
            "explanation": "quit file",
            "id": 6
        }
    ],
    "new_command": {
        "category": 2,
        "command": ":q",
        "explanation": "quit file",
        "id": 6
    },
    "success": true
}

- Sample:DELETE https://capstone-command-project.herokuapp.com/commands/1
- Output:
{
    "all_commands": [
        {
            "category": 2,
            "command": "vi filename",
            "explanation": "edit the file",
            "id": 2
        },
        {
            "category": 3,
            "command": "python filename",
            "explanation": "run a python file",
            "id": 3
        },
        {
            "category": 4,
            "command": "SELECT * FROM TABLENAME",
            "explanation": "print every value in all the columns",
            "id": 4
        }
    ],
    "success": true
}

- Sample: DELETE https://capstone-command-project.herokuapp.com/suggestions/1
- Output:
{
    "success": true,
    "suggestions": [
        {
            "category": 2,
            "id": 2,
            "suggestion": "add,something"
        }
    ]
}


