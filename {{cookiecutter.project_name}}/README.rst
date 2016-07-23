{{ cookiecutter.project_name }}
================================

{{ cookiecutter.project_short_description}}

Quickstart
----------

Run the following commands to setup your environment:

::

    $ git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}
    $ cd {{cookiecutter.project_name}}
    $ virtualenv venv or pyvenv venv # optional
    $ pip install -r requirements.txt
    $ python {{cookiecutter.app_name}}/app.py

You will see the following in your browser:

::

    $ * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    $ * Restarting with stat
    $ * Debugger is active!
    $ * Debugger pin code: 323-437-031
