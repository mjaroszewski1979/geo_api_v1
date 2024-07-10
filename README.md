## Geo Api
### This project is built on the Django Rest Framework API platform and uses the JSON Web Token authentication mechanism to enable easy access to an IP geolocation database for Python applications. The project's primary purpose is to take full advantage of custom models and serializers to facilitate the creation, viewing, and deletion of geolocation records by users.

#### By leveraging the power of the Django Rest Framework API and the convenience of JWT authentication, developers can quickly and easily create powerful applications that make use of IP geolocation data. Whether you're building a simple web app or a complex enterprise application, this project can help you get started quickly and easily.



### Features
* Data Fetching: Retrieves geographical data from multiple APIs, ensuring comprehensive and up-to-date information.
* Cross-Site Request Forgery (CSRF) Protection: Utilizes Django's built-in CSRF protection to safeguard against CSRF attacks.
* Robust User Authentication: Includes a secure user authentication system that handles user accounts, manages cookies and sessions, and tracks permissions.
* Modular Architecture: Promotes clean and maintainable code by breaking down the logic into smaller, manageable parts.
* Efficient Functionality Distribution: Encourages writing functionality in Django models or utility files instead of views.
* Environment Variable Management: Stores sensitive information such as API keys and database passwords in environment variables.
* Optimized Testing: Utilizes the setUp method in Django tests to handle expensive setup operations, improving the efficiency and reliability of the test suite.


### How it Works
* Create an account on https://ipstack.com/ to obtain your free api key
* Firstly navigate to the index page and fill out the form to create an account
* Next make a post request to 'api/token/' endpoint with your username and password credentials
* After acquiring the necessary access token you can now authorize yourself and start creating, viewing and removing geolocation data by using these three endpoints:
  * 'geo-create/' to add records to the database
  * 'geo-detail/<str:pk>/' to view records based on provided ip address (pk)
  * 'geo-delete/<str:pk>/' to remove records based on provided ip address (pk)
* Make sure to set application/x-www-form-urlencoded as content type when sending user credentials and bearer token in the authorization header for your access JWT respectively

### Installation

1. Clone the repository:
  ```bash
  git clone https://github.com/mjaroszewski1979/geo_api_v1.git
  cd geo_api_v1
  ```  
2. Create a virtual environment:
  ```bash
  python3 -m venv env
  source env/bin/activate
  ```  
3. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```  
4. Set up environment variables:
   Create a .env file and add your API keys and other configurations:
  ```bash
  API_KEY=<your-api-key>
  ```  
4. Apply migrations and start the server:
   Create a .env file and add your API keys and other configurations:
  ```bash
  python manage.py migrate
  python manage.py runserver
  ```  
### Usage
#### Access the application:
Open your browser and go to http://127.0.0.1:8000/.

### Interact with API Endpoints:
Use tools like curl or Postman to interact with the available endpoints and retrieve geographical data.

### Testing

1. Run unit tests:
  ```bash
  python manage.py test
  ```  
2. Code Coverage:
   To combine and view the code coverage of both unit and integration tests:
  ```bash
  coverage run -p manage.py test && coverage combine && coverage html
  ```
<img src="https://github.com/mjaroszewski1979/geo_api_v1/blob/main/html-report.png">

### Docker Info
* Pull an image from my Docker Hub - click on the icon below
* Create and start a container 
* Pass environment variables to your container
  * with the -e flag or using .env file

```sh
docker run -p 8000:8000 -e API_KEY="<your api key>" <imagename>

```
```sh
docker run -p 8000:8000 --env-file .env <imagename>

```

### Technologies Used
* Django: A high-level Python web framework that enables rapid development of secure and maintainable websites.
* Django Rest Framework (DRF): A powerful and flexible toolkit for building Web APIs. DRF includes built-in support for serialization, authentication, and validation, making it easy to create robust and secure APIs.
* JSON Web Tokens (JWT): A popular mechanism for securing web APIs. JWTs provide a stateless authentication method, eliminating the need for session tokens or cookies.
* IP Geolocation Database: Provides detailed information about the location of an IP address, including country, city, and region. 
* Docker: A platform for containerizing applications, ensuring consistency across development, testing, and production environments.
* Bulma CSS Framework: A modern and responsive CSS framework that simplifies frontend development. Bulma includes pre-designed, customizable components such as buttons, forms, tables, and navigation menus.
* WhiteNoise: A Python package that simplifies serving static files directly from the application, enhancing performance without relying on external services.

### Contributing
* Fork the repository.
* Create a new branch (git checkout -b feature-branch).
* Make your changes and commit them (git commit -m 'Add new feature').
* Push to the branch (git push origin feature-branch).
* Open a pull request.

### Contact
For questions or feedback, please contact [mjaroszewski1979.](https://github.com/mjaroszewski1979)


![caption](https://github.com/mjaroszewski1979/geo_api_v1/blob/main/geo_mockup.png)

  Live | Code | Docker | Technologies
  ---- | ---- | ------ | ------------
[<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/pyan1.png">](https://globalmacro.pythonanywhere.com/) | [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/github_g.png">](https://github.com/mjaroszewski1979/geo_api_v1) | [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/docker_g.png">](https://hub.docker.com/r/maciej1245/geo_api_drf) | <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/python_g.png">  &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/drf.png"> &nbsp; &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/bulma_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/ipstack_api.png"> 

