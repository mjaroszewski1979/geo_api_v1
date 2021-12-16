## <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/login.png">  &nbsp; Geo Api
### This is a Django Rest Framework API project powered by JSON Web Token authentication mechanism to provide convenient access to the IP geolocation database from applications written in the Python language. Its main function is to take full advantage of the custom models and serializers, to make it possible for the users to create, view and delete geolocation records.

--------------------------------------------------

### Features:
* Using Bulma CSS framework to implement its built-in frontend components
* Working with template inheritance mechanism to build a base “skeleton” template that contains all the common elements and defines blocks that child templates can override
* Implementing secure user authentication system which handles user accounts, manages cookies, user groups, and sessions, and keeps track of permissions
* Taking full advantage of Django's built-in features like cross-site request forgery protection to ensure safe data transfer in web forms to a database
* Associating multiple records in a table with multiple records in another table ( many-to-many relationship ) to achieve optimal ORM performance
* Breaking logic into smaller parts by adding various new Django applications to an existing project 
* Writing as much functionality as possible in models or utility files instead of views 
* Serving static files with WhiteNoise to accomplish high performance and efficiency without depending on nginx, Amazon S3 or any other external service
* Relying on Cloudinary to provide a secure and comprehensive API for easily uploading media files from server-side code
* Storing app’s secure credentials in environment variables
* Utilizing setUpModule() to handle especially expensive setup operations for all of the tests within a module


--------------------------------------------------

### Docker info:
* Pull an image from my Docker Hub - click on the icon below
* Create and start a container 
* Pass environment variables to your container
  * with the -e flag or using .env file

```
docker run -p 8000:8000 -e STRIPE_PUB_KEY="<your stripe public key>" -e STRIPE_SECRET_KEY="<your stripe secret key>" -e EMAIL_HOST_USER="<your email host user>" -e EMAIL_HOST_PASSWORD="<your email host password>" <imagename>

```
```
docker run -p 8000:8000 --env-file .env <imagename>

```


![caption](https://github.com/mjaroszewski1979/django-eshop-v2/blob/main/urban_style.gif)
  
  Live | Code | Docker | Technologies
  ---- | ---- | ------ | ------------
  [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/heroku1.png">](https://drf-geo-api.herokuapp.com/) | [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/github1.png">](https://github.com/mjaroszewski1979/geo_api_v1) | [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/docker.png">](https://hub.docker.com/r/maciej1245/drf_geo_api) | <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/python1.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/django.png">   &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/bulma.png"> 
