# Instructions for deploying the application:

### 1. To run the application, create a directory and clone the files from the repository there using the ***git clone*** command
### 2. Create a virtual environment using the command ***pip install requirements.txt***
### 3. Go to the root directory and use the command ***python manage.py runserver*** to start the django application
### 4. Follow the directions in the app

## GET REQUESTS TO API

in order to get data on all users who answered the question, you need to send a GET request with the / Users parameters

or using the browser in the url strings specify http: // localhost: 8000 / api / v1 / Users

in order to get data on all polls, you need to send a GET request with the / Poll parameters

or using the browser in the url strings specify http: // localhost: 8000 / api / v1 / Poll

in order to get data on all question, you need to send a GET request with the / Question parameters

or using the browser in the url strings specify http: // localhost: 8000 / api / v1 / Question

in order to get data on all answer, you need to send a GET request with the / Answer parameters

or using the browser in the url strings specify http: // localhost: 8000 / api / v1 / Answer

## POST REQUESTS TO API

to create a record in api, specify the fields for the record corresponding to the fields that you want to create in the database

## DELETE REQUESTS TO API

...
