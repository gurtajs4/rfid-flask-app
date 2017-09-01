# rfid-flask-app

Web application for supervising and managing keys in School and Faculty institutions using RFID hardware technology for automatic identification and data tracking.
This application is complementary to a concept of keys management system for School and Faculty institutions devised by me, Matija Čvrk, for a student project.

## RFID hardware used

- Raspberry Pi Model B Rev 2 with 512MB of RAM.
- MFRC522 RFID contactless reader/writer module
- RFID tags and cards

## Middleware (prerequisites)

[Broadcom BCM 2835](http://www.airspayce.com/mikem/bcm2835/index.html) library - provides access to GPIO on Raspberry Pi.

[SPI-Py](https://github.com/lthiery/SPI-Py) - hardware SPI as C extension for Python.

## Web and other software related technologies used

[Flask](http://flask.pocoo.org/) |
[AngularJS](https://angularjs.org/) |
[Bootstrap3](http://getbootstrap.com/) |
[MFRC Py-Lib: Rasplay](https://github.com/rasplay/mfrc522-python) |
[xlutils](https://pypi.python.org/pypi/xlutils) |
[xlrd](https://pypi.python.org/pypi/xlrd) |
[xlwt](https://pypi.python.org/pypi/xlwt) |
[pip](https://pypi.python.org/pypi/pip) |
[bower](https://bower.io/) |
[npm](https://www.npmjs.com/)

## Install

Install dependancies for backend side with pip and client side dependancies with bower and npm first.

Backend (Flask) side: run `pip install -r requirements.txt` from root of project.

Client (AngularJS) side:
- navigate to inner src folder (rfid-flask-app/src/src/) and run `bower install`
- navigate to static folder (rfid-flask-app/src/src/static/) and run `npm install`

## Web layout
![lander:mobile](https://github.com/traVaulta/rfid-flask-app/blob/master/docs/responsive.mobile-home-hero.png) ![navbar:mobile](https://github.com/traVaulta/rfid-flask-app/blob/master/docs/responsive.mobile-home-nav.png) ![register:mobile](https://github.com/traVaulta/rfid-flask-app/blob/master/docs/responsive.mobile-user-register.png)

## Read the docs
Checkout [getting started]() for a quickstart on how to use.

For further usage, read the [documentation.](https://github.com/traVaulta/rfid-flask-app/blob/master/docs/)

Tutorial - [maybe some day]().
