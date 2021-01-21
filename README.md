# Edge Detection API #

The purpose of this README.md file is to explain the steps required to setup this project in your local environment for testing.

<div align='center'>
  <img src='./images/response.png'>
</div>

### How do I get set up? ###

* Summary of set up
* Dependencies
* How to run tests

### Requirements ###
* Python


### Setting up ###

* Create a Virtual environment
```
$ python -m venv env
```
* Clone the project in that directory

* Install dependencies
```
$ pip install -r requirements.txt
```

### Test Locally ###
```
$ python app.py
```
Copy the URL http://127.0.0.1:5000/ on Postman or any other API supply

### API Parameter ###
```
file ==> Image you want to detect edges, Image size must not be greater than 2MB
```
#### Example of Edge Detected ####


<div align='center'>
  <img src='./images/2.png'>
</div>

<br><br><br>

<div align='center'>
  <img src='./images/1.png'>
</div>