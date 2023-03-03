## Geo Api
### This project is built on the Django Rest Framework API platform and uses the JSON Web Token authentication mechanism to enable easy access to an IP geolocation database for Python applications. The project's primary purpose is to take full advantage of custom models and serializers to facilitate the creation, viewing, and deletion of geolocation records by users.

#### By leveraging the power of the Django Rest Framework API and the convenience of JWT authentication, developers can quickly and easily create powerful applications that make use of IP geolocation data. Whether you're building a simple web app or a complex enterprise application, this project can help you get started quickly and easily.

The Django Rest Framework API is a powerful tool for developers who want to create web APIs quickly and easily using the Django framework. With its built-in support for serialization, authentication, and validation, the Django Rest Framework API makes it easy for developers to create robust and secure APIs that can be used by a wide range of applications.

JSON Web Tokens (JWTs) are a popular mechanism for securing web APIs. JWTs allow developers to authenticate users without the need for session tokens or cookies, making them a great choice for modern web applications.

The IP geolocation database provides developers with a wealth of information about the location of an IP address, including the country, city, and region. This information can be incredibly useful for a wide range of applications, including online advertising, e-commerce, and security.

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

### Code Coverage:

<img src="https://github.com/mjaroszewski1979/geo_api_v1/blob/main/html-report.png">

-------------------------------------------------

![caption](https://github.com/mjaroszewski1979/geo_api_v1/blob/main/geo_mockup.png)

  
 Code | Docker | Technologies
 ---- | ------ | ------------
[<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/github_g.png">](https://github.com/mjaroszewski1979/geo_api_v1) | [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/docker_g.png">](https://hub.docker.com/r/maciej1245/geo_api_drf) | <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/python_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/django_g.png">   &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/drf.png"> &nbsp; &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/bulma_g.png"> 
