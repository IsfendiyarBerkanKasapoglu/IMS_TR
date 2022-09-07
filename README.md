# Inventory Management System - Turkish

<img width="1438" alt="Screen Shot 2022-09-07 at 15 33 34" src="https://user-images.githubusercontent.com/84452695/188880062-f1c9cbfb-6148-4b11-b3af-f7e0783b612a.png">
<img width="1436" alt="Screen Shot 2022-09-07 at 15 34 45" src="https://user-images.githubusercontent.com/84452695/188880140-c0a8c09e-be2b-47fd-ae9f-0506b2878007.png">
<img width="1435" alt="Screen Shot 2022-09-07 at 15 35 24" src="https://user-images.githubusercontent.com/84452695/188880182-8b125ffe-13e1-4257-b115-dd4dc155f93b.png">
<img width="1436" alt="Screen Shot 2022-09-07 at 15 36 10" src="https://user-images.githubusercontent.com/84452695/188880220-a148c0eb-d2a7-4fb4-bb13-25e78e4292a9.png">
<img width="1435" alt="Screen Shot 2022-09-07 at 15 36 21" src="https://user-images.githubusercontent.com/84452695/188880252-2a774025-a9e4-4fe0-a16f-9e1ea2e9f2ba.png">
<img width="1435" alt="Screen Shot 2022-09-07 at 15 36 34" src="https://user-images.githubusercontent.com/84452695/188880259-a52adfe8-5442-485d-81bd-68a79648b4da.png">


Open terminal:

Clone repository in your machine:
```
git clone https://github.com/IsfendiyarBerkanKasapoglu/IMS_TR.git
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


