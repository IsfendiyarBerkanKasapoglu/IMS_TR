# PiriReis - IMS_TR


Open terminal:

Clone repository in your machine:
```
git clone https://github.com/IsfendiyarBerkanKasapoglu/IMS_trr.git
```

Change directory to the location:
```
cd IMS_TR
```

Create a virtual environment:
``` 
python3 -m venv env
```

Start the virtual environment:
```
source env/bin/activate
```
Install PIP:
```
python3 -m pip install --upgrade pip
```

Install all imports using requirements.txt
```
pip3 install -r requirements.txt 
```

Before start the server change directory to the inventorySystem
```
cd inventorySystem
```

Before run the server create an account
```
python manage.py createsuperuser
```

Run the server:
```
python manage.py runserver
```

