# Elegimos

###### 
It is a website with information on the candidates of the 2021 Peruvian elections.

In Elegimos webpage you can find a filter tool which you can apply as many filters as you want to the presidential and congressional candidates.
There are two types of filters, the ones that limit your candidates, such as if they were born in a certain Peruvian city or not, if they had any police records, maybe if they are in a certain age range and more, and, there are filters that order your results, such as anual income, properties and so on.
![image](https://user-images.githubusercontent.com/40151035/125700833-7d34e5ff-7c8e-45c3-9609-cb2d877f639b.png)
![image](https://user-images.githubusercontent.com/40151035/125701007-64c1d1fe-3466-4f31-9891-2ea19900d41a.png)

 You can check your candidates curriculum vitae too!.
![image](https://user-images.githubusercontent.com/40151035/125700890-608f3193-e028-4ee6-b634-d053d725ba81.png)
![image](https://user-images.githubusercontent.com/40151035/125700912-25bd2b00-6627-4b74-9390-057fee153c79.png)


### Guía de instalación

Dependencias

`pip3 install -r requirements`

### Migraciones

`python3 manage.py makemigrations elecciones`

`python3 manage.py migrate`

### Ejecutar la aplicación

`python3 manage.py runserver`



## Deployment

1. Change the DEBUG line on **settings.py** to False.

2. Run this command
    `python3 manage.py collectstatic`

###### Made with :heart: by

[@mistyblunch]( https://github.com/gracenikole)
[@alexandra](https://github.com/Alexandra-SR)
[@Miunmn](https://github.com/Miunmn)
[@Roosevelt](https://github.com/rubaldoch)
