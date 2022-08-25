# TheYogaApp
Yoga exercise assistant and diet recommendation app.

## Run Locally

Clone the project
```bash
 git clone https://github.com/evilemperor07/TheYogaApp.git
```

Open terminal in the directory and create a virtual environment
```bash
 py -m venv venv
```

Activate virtual environment
```bash
 venv\Scripts\activate
```

Install requirements
```bash
 pip install -r requirements.txt
```

Make migrations and migrate
```bash
 cd TheYogaApp
 py manage.py makemigrations
 py manage.py migrate
```

Run application on localhost
```bash
 py manage.py runserver
```
