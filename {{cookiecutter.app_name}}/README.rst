{{ cookiecutter.project_name }}
================================

{{ cookiecutter.project_short_description}}

Quickstart
----------

Run the following commands to setup your environment:

::

    git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.app_name}}
    cd {{cookiecutter.app_name}}
    pip install virtualenv # optional
    virtualenv venv or pyvenv venv # optional
    pip install -r requirements.txt
    python app.py

You will see the following in your browser:

::

    $
