# Weather_Report

Sprint information: https://github.com/ianballou/mini-project-EC463/projects/1<br>
Demo website: http://128.31.24.130:5000

# Pre-requirements

C compiler, general development tools installed, Python

# Steps to run:

- `cd` into the root directory of this project
- Install `python-virtualenv`
- Run `virtualenv .venv`
- Run `source .venv/bin/activate`
- Run `pip install flask`
- Run `export FLASK_APP=miniproject.py`
- Run `pip install flask-wtf`
- Run `pip install flask-sqlalchemy`
- Run `pip install flask-migrate`
- Run `pip install flask-login`
- Run `pip install flask-login`
- Run `pip install matplotlib`
- Create `~/.config/matplotlib/matplotlibrc`
- Run `echo "backend: Agg" > ~/.config/matplotlib/matplotlibrc`
- Install the python tkinter library with a package manager: `apt-get`, `yum`, `dnf`, etc
- Run `flask db upgrade`
- Start the site by running `flask run --host=0.0.0.0`

# Design choices:
- Web framework: Python Flask<br>
- Database management: SQLAlchemy<br>
- Authentication: Database username/email/password<br>
- Sensor simulation: Upon logging in and loading a user's homepage, sensor data is randomly (but realistically) generated and plotted.<br>
- Plot display: Plots are generated as PNG files using the Python PyPlot library.  These files are numbered and named based on their graph types and related users.  They are then rendered in a user's homepage.

# Workflow
1) Register with username, email, password, and # of sensors.
2) View graphs of sensor data on personal homepage.

# Contributors
- Ian Ballou (https://github.com/ianballou)
  - VM Hosting
  - Front-end design & implementation
  - Web server API design & implementation
  - Database layout
- Lin Ma (https://github.com/linma18)
  - Sensor simulation design & implementation
  - Sensor data display design & implementation
  - Application workflow architecture
  - Database research
  
  # Acknowledgements
  The Flask Mega-Tutorial (https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

