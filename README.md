# Django Project

This is a lightweight and easy to setup boilerplate project for Django.

- Easy to setup
- Ready to start dev out of the box
- flexibility to rename
- and some awesome ✨Magic ✨

> Note: `./manage.py startapp <app-name>` Every time we create a new app, we will move it inside the apps package..

## Features

- All Apps managed and maintined under one folder.
- Settings are saperated in Base and Env with modular structure 
- Core APP responsible for:
-- Custom commands
-- Base setup
- Integrated Debug Toolbar


## Tech

This project uses a number of open source projects to work properly:

- [Django] - Python web framework that encourages rapid development
- [Django Debug Toolbar] - configurable set of panels that display various debug information about the current request/response and when clicked, display more details about the panel's content.

## Installation

Requires [Django] v4.0.1 to run.

Step 1 : Create Project root directory
```sh
mkdir <project_name> 
```

Step 2 : Clone the project in you <project_name> directory 
```sh
cd <project_name>
git clone https://github.com/abhi-tupparwar/django_project.git
```

Step 3 : Copy the contents of _config/settings/example.env.py_ to _config/settings/env.py_

Step 4 :Install the dependencies and start the server.

```sh
cd django_project
pip install -r requirements.txt // install requirements
./manage.py collectstatic //collect all static files
./manage.py runserver
```

To rename the project execute following command:
```sh
./manage.py rename_project <project_name> // renames django_project to specified project name
```

## Folder Structure
```
<project_name>
|
|---assets (folder created once static files are collected)
|
|---django_project
|   |---apps
|   |   |---core (core app)
|   |   |---...<other apps>...
|   |   |---urls.py
|   |
|   |---config
|   |   |---settings
|   |   |   |---base.py
|   |   |   |---env.py (ignored by git)
|   |   |   |---env.example.py
|   |   |
|   |   |---asgi.py
|   |   |---urls.py
|   |   |---wsgi.py
|   |   |
|   |   |static_files (all static files we use in development)
|   |   |---base (project as a whole specific static files)
|   |   |   |---css
|   |   |   |---img
|   |   |   |---js
|   |   |---core (my custom app specific)
|   |   |   |---css
|   |   |   |---img
|   |   |   |---js
|   |   |
|   |---templates
|   |   |---core (custom app specific)
|   |   |---<other app specific templates>
|   |   |---base.html (included basics of jquery and bootstrap)
|   |
|   |---.gitignore
|   |---manage.py
|   |---requirements.txt
|
|---media (folder created once items were uploaded)
|---db.sqlite3
```


## License

MIT

   [Django]: <https://www.djangoproject.com/>
   [git-repo-url]: <https://github.com/abhi-tupparwar/django_project>
   [Django Debug Toolbar]: <https://django-debug-toolbar.readthedocs.io/en/latest/>
   
