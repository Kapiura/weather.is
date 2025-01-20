# What's the weather - django web app
django app - sprawdza pogode i wyswietla info na jej temat, wszytstko w celach edukacyjnych
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
How it looks

# Home page
![home page](https://github.com/Kapiura/weather.is/blob/0f57101abbb3b300610db3b8c673e8dbd11062e5/readme_images/ss_main.png)

# Weather page - all cities
![weather page](https://github.com/Kapiura/weather.is/blob/0f57101abbb3b300610db3b8c673e8dbd11062e5/readme_images/ss_we.png)

# Weather page - Gdansk
![weather - Gdanks](https://github.com/Kapiura/weather.is/blob/820963a44b8f43aa435b9eb4b467367197b63bbe/readme_images/ss_gd_1.png)
![weather - Gdanks](https://github.com/Kapiura/weather.is/blob/820963a44b8f43aa435b9eb4b467367197b63bbe/readme_images/ss_gd_ap.png)
![weather - Gdanks](https://github.com/Kapiura/weather.is/blob/0f57101abbb3b300610db3b8c673e8dbd11062e5/readme_images/ss_gd_map.png)
