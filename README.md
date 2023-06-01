# weather.is
weather is a website that checks and displays info about air pollution in poland cities 


Make a directory for website and go into it
```
mkdir PJS
cd PJS
```

Clone files to this directory
```
git clone https://github.com/Kapiura/weather.is.git .
```

Create a virtual envoriment
```
virtualenv -p python3 .
```

Activate an virtual env
```
source bin/activate
```

Install all packages u need to run app
```
pip install -r requirements.txt
```

Go to src and run django app
```
cd src
python3 manage.py runserver
```
