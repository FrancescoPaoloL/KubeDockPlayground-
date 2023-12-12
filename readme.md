# KubeDockPlayground
This is just a 'hello world' example to demonstrate how containerization works. 
First, we created a Dockerfile and a simple app using Flask. After building an image, we ran it using curl.

We utilized the following:
- Flask: A lightweight and user-friendly micro web framework for Python, suitable for small to medium-sized web applications and services.
- curl: A command-line tool for making HTTP requests, used in this case to send POST requests to your Flask web service for testing purposes.

To containerize your Flask web service with Docker, we've created a Dockerfile. 
The implemented web service is a very basic calculator that accepts two numbers in JSON format through a POST request and returns their sum.

Here are the commands for building, running, and testing the service:

    docker build -t simple-web-service .
    docker run -p 8282:8080 simple-web-service
    curl -X POST -H "Content-Type: application/json" -d '{"value1":"1","value2":2}' http://192.168.0.13:8282

The HTTP address is obtained using the `hostname -I` command on the server where our service is running.
Additionally, in the code, we import HTTPException from werkzeug.exceptions to handle HTTP exceptions.

## Languages and Tools
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 

## Requirements
```
Flask==1.1.4
Werkzeug==1.0.1
```

## Test Coverage
TODO


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

<hr>

## Connect with me
<p align="left">
<a href="https://www.linkedin.com/in/francescopl/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="francescopaololezza" height="20" width="30" /></a>
<a href="https://www.kaggle.com/francescopaolol" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/kaggle.svg" alt="francescopaololezza" height="20" width="30" /></a>
</p>

