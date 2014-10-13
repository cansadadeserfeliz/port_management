Port Management
===============

We manage the Rotterdam port. Ships arrive daily. Every ship has a unique
identifier, composed of letters and digits.

A ship is loaded with containers. Every container has a unique number.
It is known if the contents of a container imply a fire and/or chemical hazard.

A ship may enter a dock. A dock can contain only one ship at a time.
On every dock, several people are employed, of which some are supervisors.
The first name, last name, address and bank account number of each employee
is known. Employees are assigned to a ship in the dock.

* An overview page that lists docks with their occupancy, and cargo hazards.

* A dock detail page with for example the employees, current ship, containers
and cargo hazards and a historic overview of ships

Installation
------------

    git clone https://github.com/ctrl-alt-delete/port_management.git
    pip install -r requirements.txt
    touch app/local_settings.py

Define your local settings in ``local_settings.py``, for example,

    DEBUG = True

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'port_management',
        }
    }

Run migrations:

    python manage.py migrate

Run server:

    python manage.py runserver


Screenshots
-----------

![Screenshot: Home](http://vero4ka.info/images/docs/port102.png)

![Screenshot: List od docks](http://vero4ka.info/images/docs/port103.png)

![Screenshot: Dock detail](http://vero4ka.info/images/docs/port104.png)

![Screenshot: Settings](http://vero4ka.info/images/docs/port101.png)

![Screenshot: Admin](http://vero4ka.info/images/docs/port105.png)
