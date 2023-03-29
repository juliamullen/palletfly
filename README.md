A simple Django model for a ToDo. Includes a title field, a description field, and a completed field. Relies on the djangorestframework ModelSerializer and DefaultRouter to automatically generate a full CRUD API. In order to identify myself among other candidates I've also included a test suite that verifies the four requested features: list, create, retrieve, delete.

To run this project first clone the github repo:

```
git clone https://github.com/juliamullen/palletfly.git
cd palletfly
```

Then set up a virtual environment:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Then run the tests and/or the server:

```
python manage.py test
python manage.py runserver
```
