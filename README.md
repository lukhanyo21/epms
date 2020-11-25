## Enterprise Performance Management System

Installation / Setup on local machine
# Windows and Unix Like:

- Download Python from the [official Python site](https://www.python.org/downloads/release/python-361/)
- Install Python and add it to environmental variables
- On your develop directory, create a virtual environment. Can follow the this documentation / guidelines:
https://virtualenv.pypa.io/en/stable/userguide/

- Activate the environment, guidelines provided in the link above. Here is an example you would type on the command line:
```
path\to\env\Scripts\activate
```
- It's entirely up to the developer where they wish to place the virtual environment. It's recommend you create a
directory and label something like 'venvs' and create the environments there for each project. Along side the
'venv' directory, will be the project directories.
- Along side the virtual environments directory e.g' 'venvs' clone the project.
- at this step, you should have the virtual environment and it should be activated. Next to the root of the virtual
environments you will have the project you recently cloned.
```
cd enterprise_performance_management
```
- run the following command (it install django and other requirements:
pip install -r requirements/local.txt
- The project is ready. Now you can run it through your IDE or on the command line you run the following command:
cd enterprise_management_suite
python manage.py runserver localserver:8000

