## <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/login.png">  &nbsp; Geo Api
### This is a Django Rest Framework API project powered by JSON Web Token authentication mechanism to provide convenient access to the IP geolocation database from applications written in the Python language. Its main function is to take full advantage of the custom models and serializers, to make it possible for the users to create, view and delete geolocation records.

--------------------------------------------------

### Features:
* Using Bulma CSS framework to implement its built-in frontend components
* Implementing secure user authentication system which handles user accounts, manages cookies, sessions, and keeps track of permissions
* Taking full advantage of Django's built-in features like cross-site request forgery protection to ensure safe data transfer in web forms to a database
* Breaking logic into smaller parts by adding various new Django applications to an existing project 
* Writing as much functionality as possible in models or utility files instead of views 
* Serving static files with WhiteNoise to accomplish high performance and efficiency without depending on nginx, Amazon S3 or any other external service
* Relying on JSON Web Token - an open standard used to share security information between two parties — a client and a server, to ensure that sensitive data signed using a  cryptographic algorithm cannot be altered after the token is issued
* Storing app’s secure credentials in environment variables
* Utilizing setUpModule() to handle especially expensive setup operations for all of the tests within a module

--------------------------------------------------

### How it works:
* Create an account on https://ipstack.com/ to obtain your free api key
* Firstly navigate to the index page and fill out the form to create an account
* Next make a post request to 'api/token/' endpoint with your username and password credentials
* After acquiring the necessary access token you can now authorize yourself and start creating, viewing and removing geolocation data by using these three endpoints:
  * 'geo-create/' to add records to the database
  * 'geo-detail/<str:pk>/' to view records based on provided ip address (pk)
  * 'geo-delete/<str:pk>/' to remove records based on provided ip address (pk)
* Make sure to set application/x-www-form-urlencoded as content type when sending user credentials and bearer token in the authorization header for your access JWT respectively

--------------------------------------------------
  


### Docker info:
* Pull an image from my Docker Hub - click on the icon below
* Create and start a container 
* Pass environment variables to your container
  * with the -e flag or using .env file

```
docker run -p 8000:8000 -e API_KEY="<your api key>" <imagename>

```
```
docker run -p 8000:8000 --env-file .env <imagename>

```

--------------------------------------------------

![caption](https://github.com/mjaroszewski1979/geo_api_v1/blob/main/drf_geo_api.gif)

  
  Live | Code | Docker | Technologies
  ---- | ---- | ------ | ------------
  [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/heroku1.png">](https://geo-api-drf.herokuapp.com/) | [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/github1.png">](https://github.com/mjaroszewski1979/geo_api_v1) | [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/docker.png">](https://hub.docker.com/r/maciej1245/geo_api_drf) | <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/python1.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/django.png">   &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/drf.png"> &nbsp; &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/bulma.png"> 
