## Creating a virtual Environment: 
- Open terminal
- Run `python -m venv env` => env is the name of your virtual environment
- acivate the virtual envrionment: 
    - for linux users: `source env/bin/activate`
    - for windows users: 
        - switch terminal to `command prompt`
        - now run `./env/Scripts/activate.bat` => this works is your slashes resember */* else run `.\env\Scripts\activate.bat`

Advantages of using virtual environments:
- Project isolation
- consistency in dependencies making it easier to reproduce the project in any machine/ environment 
- prevents the "it works on my machine"

Create an `requirements.txt` file which will hold all out dependencies:
- run `pip freeze >> requirements.txt`
- when your collaborator gets this project they are going to run `pip install -r requirements.txt` s as to get the particular dependencies

Create `.gitignore` file & add env inside it